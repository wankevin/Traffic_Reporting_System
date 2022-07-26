import os
import threading
import requests
from bs4 import BeautifulSoup

from PySide2.QtGui import QPixmap, QColor, QCursor
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import Qt, QDate, QSize, QUrl, Signal, QTime
from PySide2.QtWidgets import QMainWindow, QMessageBox, QDialog, QTableWidgetItem, QPushButton, QStyle, \
    QSizePolicy, QComboBox, QFrame

from UI.ui_sambo import Ui_MainWindow
from UI.sambo_upload_info import Ui_Dialog

from function.resource import street_list

import Image


class TrafficReport(QMainWindow):
    change_video_label = Signal(QPixmap)

    def __init__(self):
        super(TrafficReport, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__restore_personal_information_area()
        self.__value()

    def __value(self):
        self.setWindowTitle("Traffic Reporting System v1.0.1")
        self.township_list = ["南投市"]

        # init street
        self.street_list = street_list

        # init street listWidget
        for street in self.street_list:
            self.ui.listWidget_sambo_street1.addItem(street)
            self.ui.listWidget_sambo_street2.addItem(street)

        # ----- personal area information and button signal ------
        self.personal_area_parameter = {
            "姓名": {"hide_element": self.ui.lineEdit_personal_name, "label": self.ui.label},
            "身分證字號": {"hide_element": self.ui.lineEdit_personal_id, "label": self.ui.label_14},
            "連絡電話": {"hide_element": self.ui.lineEdit_personal_phone, "label": self.ui.label_15},
            "通訊地址": {"hide_element": self.ui.lineEdit_personal_address, "label": self.ui.label_16},
            "電子信箱": {"hide_element": self.ui.lineEdit_personal_email, "label": self.ui.label_17},
        }
        self.ui.pushButton_personal_name.clicked.connect(self.__personal_area_single_show_hide_control)
        self.ui.pushButton_personal_id.clicked.connect(self.__personal_area_single_show_hide_control)
        self.ui.pushButton_personal_phone.clicked.connect(self.__personal_area_single_show_hide_control)
        self.ui.pushButton_personal_address.clicked.connect(self.__personal_area_single_show_hide_control)
        self.ui.pushButton_personal_email.clicked.connect(self.__personal_area_single_show_hide_control)
        self.ui.pushButton_personal_info.clicked.connect(
            lambda: self.__personal_information_area_show_hide_control(self.ui.frame_2))
        self.ui.pushButton_personal_save.clicked.connect(self.__save_personal_information)
        self.personal_information_area_flag = False

        # ----- violate area information and button signal ------
        self.violate_area_parameter = {
            "違規區域": {"hide_element": self.ui.lineEdit_sambo_violate_town, "label": self.ui.label_13},
            "車種": {"hide_element": self.ui.comboBox_sampbo_car_type, "label": self.ui.label_8},
            "車牌號碼": {"hide_element": self.ui.lineEdit_sambo_car_number, "label": self.ui.label_9},
            "地點簡易說明": {"hide_element": self.ui.frame_9, "element": self.ui.lineEdit_sampbo_position,
                       "label": self.ui.label_10},
            "違規情況": {"hide_element": self.ui.comboBox_sampbo_violate_dest, "label": self.ui.label_6},
            "違規日期": {"hide_element": self.ui.frame_12, "element_date": self.ui.calendarWidget,
                     "element_time": self.ui.timeEdit, "label": self.ui.label_5},

        }
        self.ui.pushButton_sambo_car_town_position.clicked.connect(self.__violation_area_signal_show_hide_control)
        self.ui.pushButton_sambo_car_type.clicked.connect(self.__violation_area_signal_show_hide_control)
        self.ui.pushButton_sambo_car_id.clicked.connect(self.__violation_area_signal_show_hide_control)
        self.ui.pushButton_sambo_car_position.clicked.connect(self.__violation_area_signal_show_hide_control)
        self.ui.pushButton_sambo_event_desc.clicked.connect(self.__violation_area_signal_show_hide_control)
        self.ui.pushButton_sambo_date.clicked.connect(self.__violation_area_signal_show_hide_control)
        self.ui.pushButton_sambo_car_info.clicked.connect(
            lambda: self.__violation_information_area_show_hide_control(self.ui.frame_7))
        self.violate_information_area_flag = False

        # keyword search
        self.ui.lineEdit_sambo_street_1.textChanged.connect(
            lambda: self.__keyword_search(current_street=self.ui.lineEdit_sambo_street_1,
                                          next_street=self.ui.lineEdit_sambo_street_2,
                                          list_widget=self.ui.listWidget_sambo_street1))
        self.ui.lineEdit_sambo_street_2.textChanged.connect(
            lambda: self.__keyword_search(current_street=self.ui.lineEdit_sambo_street_2,
                                          next_street=self.ui.lineEdit_sambo_street_1,
                                          list_widget=self.ui.listWidget_sambo_street2))

        # violation position setting
        self.ui.listWidget_sambo_street1.itemClicked.connect(self.__selected_street)
        self.ui.listWidget_sambo_street2.itemClicked.connect(self.__selected_street)

        # select resource use function
        self.ui.file_exploer.clicked.connect(self.__file_explorer)

        # self.ui.pushButton_upload.clicked.connect(self.__start_upload)

        # videoWidget Setting
        self.videoWidget = QVideoWidget()
        self.videoWidget.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.positionChanged.connect(self.__video_position_changed)
        self.mediaPlayer.durationChanged.connect(lambda x: self.ui.horizontalSlider.setRange(0, x))
        self.ui.gridLayout_8.addWidget(self.videoWidget, 2, 0, 1, 1)
        self.ui.pushButton_video_control.clicked.connect(self.__video_control)
        self.ui.horizontalSlider.sliderMoved.connect(self.__video_set_position)
        self.ui.pushButton_video_control.setIcon(
            self.style().standardIcon(QStyle.SP_MediaPlay))
        self.ui.pushButton_video_control.setEnabled(False)
        self.videoWidget.setVisible(False)

        # 批量執行
        self.uploading_parameter = {}

        # calender setting
        today = QDate.currentDate()
        self.ui.calendarWidget.setMinimumDate(today.addDays(-6))
        self.ui.calendarWidget.setMaximumDate(today.addDays(0))

        for i in range(0, 25):
            self.ui.comboBox_hour.addItem(str(i))

        for i in range(0, 61):
            self.ui.comboBox_minute.addItem(str(i))

        self.ui.comboBox_minute.currentIndexChanged.connect(self.__combo_box_minute_click_func)
        self.ui.comboBox_hour.currentIndexChanged.connect(self.__combo_box_hour_click_func)
        self.ui.comboBox_hour.setCurrentIndex(0)
        self.ui.comboBox_minute.setCurrentIndex(0)
        self.ui.timeEdit.setTime(QTime(0, 0, 0, 0))

        # icon setting
        self.ui.pushButton_personal_save.setIcon(QtGui.QIcon(":icons/cil-save.png"))
        self.ui.pushButton_personal_save.setIconSize(QSize(24, 24))
        self.ui.pushButton_personal_status.setIconSize(QSize(24, 24))
        self.ui.pushButton_sambo_status_2.setIcon(QtGui.QIcon(":icons/cil-plus.png"))
        self.ui.pushButton_sambo_status_2.setIconSize(QSize(24, 24))

    def __restore_personal_information_area(self):
        settings = QtCore.QSettings('report_system', 'QSetting')
        setting_key_list = settings.allKeys()

        self.ui.lineEdit_personal_name.setText(
            settings.value("personal_name")) if "personal_name" in setting_key_list else None
        self.ui.lineEdit_personal_id.setText(
            settings.value("personal_id")) if "personal_id" in setting_key_list else None
        self.ui.lineEdit_personal_phone.setText(
            settings.value("personal_phone")) if "personal_phone" in setting_key_list else None
        self.ui.lineEdit_personal_address.setText(
            settings.value("personal_address")) if "personal_address" in setting_key_list else None
        self.ui.lineEdit_personal_email.setText(
            settings.value("personal_email")) if "personal_email" in setting_key_list else None
        self.open_file_path = settings.value("personal_file_path") if "personal_file_path" in setting_key_list else ""

    def __personal_area_single_show_hide_control(self):
        sender_text = self.sender().text()
        hide_element = self.personal_area_parameter.get(sender_text).get("hide_element")
        label = self.personal_area_parameter.get(sender_text).get("label")

        if hide_element.isVisible():
            hide_element.setVisible(False)
            label.setText(f"({hide_element.text()})")
            self.personal_information_area_flag = False

        else:
            hide_element.setVisible(True)
            label.setText("")
            self.personal_information_area_flag = True

    def __personal_information_area_show_hide_control(self, frame):
        for button in frame.findChildren(QPushButton):
            sender_text = button.text()
            line_edit = self.personal_area_parameter.get(sender_text).get("hide_element")
            label = self.personal_area_parameter.get(sender_text).get("label")
            if not self.personal_information_area_flag:
                line_edit.setVisible(False)
                label.setText(f"({line_edit.text()})")
            else:
                line_edit.setVisible(True)
                label.setText("")

        self.personal_information_area_flag = False if self.personal_information_area_flag else True

    def __violation_area_signal_show_hide_control(self):
        sender_text = self.sender().text()
        hide_element = self.violate_area_parameter.get(sender_text).get("hide_element")
        label = self.violate_area_parameter.get(sender_text).get("label")

        if hide_element.isVisible():
            hide_element.setVisible(False)
            if type(hide_element) == QComboBox:
                label.setText(f"({hide_element.currentText()})")

            elif hide_element.objectName() == "frame_12":
                self.ui.frame_12.setVisible(False)
                date = self.ui.calendarWidget.selectedDate().toString("yyyy/MM/dd")
                time = self.ui.timeEdit.time().toString()
                date_time = date + "  " + time
                self.ui.label_5.setText(date_time)

            elif type(hide_element) == QFrame:
                hide_element = self.violate_area_parameter.get(sender_text).get("element")
                label.setText(f"({hide_element.text()})")

            else:
                label.setText(f"({hide_element.text()})")


        else:
            hide_element.setVisible(True)
            label.setText("")

    def __violation_information_area_show_hide_control(self, frame):
        for button in frame.findChildren(QPushButton):
            sender_text = button.text()
            hide_element = self.violate_area_parameter.get(sender_text).get("hide_element")
            label = self.violate_area_parameter.get(sender_text).get("label")

            if not self.violate_information_area_flag:
                hide_element.setVisible(False)
                if type(hide_element) == QComboBox:
                    label.setText(f"({hide_element.currentText()})")

                elif hide_element.objectName() == "frame_12":
                    self.ui.frame_12.setVisible(False)
                    date = self.ui.calendarWidget.selectedDate().toString("yyyy/MM/dd")
                    time = self.ui.timeEdit.time().toString()
                    date_time = date + "  " + time
                    self.ui.label_5.setText(date_time)

                elif type(hide_element) == QFrame:
                    hide_element = self.violate_area_parameter.get(sender_text).get("element")
                    label.setText(f"({hide_element.text()})")

            else:
                hide_element.setVisible(True)
                label.setText("")

        self.violate_information_area_flag = False if self.violate_information_area_flag else True

    def __keyword_search(self, current_street, next_street, list_widget):
        current_street_text = current_street.text()
        other_street_text = next_street.text()

        if not current_street_text:
            for street in self.street_list:
                list_widget.addItem(street)
            return

        list_widget.clear()
        for street in self.street_list:
            list_widget.addItem(street) if current_street_text in street else None

        if current_street_text and not other_street_text:
            self.ui.lineEdit_sampbo_position.setText(current_street_text + "路口")

        elif current_street_text and other_street_text:
            self.ui.lineEdit_sampbo_position.setText(current_street_text + "與" + other_street_text + "的路口")

    def __selected_street(self, index):
        if not index:
            return

        sender_element_text = self.sender().objectName()

        if sender_element_text == "listWidget_sambo_street1":
            list_widget = self.ui.listWidget_sambo_street1
            line_edit = self.ui.lineEdit_sambo_street_1

        else:
            list_widget = self.ui.listWidget_sambo_street2
            line_edit = self.ui.lineEdit_sambo_street_2

        current_text = list_widget.currentItem().text()
        line_edit.setText(current_text)
        list_widget.clear()

        for town in self.street_list:
            list_widget.addItem(town)

        list_widget.setCurrentRow(self.street_list.index(current_text))

    def __file_explorer(self):
        self.ui.file_type.clear()

        __filename, __type = QtWidgets.QFileDialog.getOpenFileName(None, "Load Data", self.open_file_path,
                                                                   "Video or Image (*.png *.jpg *.mp4)")

        if not __filename:
            return

        self.ui.file_name.setText(__filename)
        extension = str(__filename).split(".")[-1]
        if extension == "png" or extension == "PNG":
            self.ui.file_type.setText("image/png")

        elif extension == "jpg" or extension == "JPG":
            self.ui.file_type.setText("image/jpg")

        if extension == "png" or extension == "jpg" or extension == "PNG" or extension == "JPG":
            self.videoWidget.setVisible(False)
            self.ui.label_sambo_image.setVisible(True)
            self.ui.pushButton_video_control.setEnabled(False)
            pixmap = QtGui.QPixmap(__filename).scaled(self.ui.label_sambo_image.size(),
                                                      aspectMode=Qt.KeepAspectRatio)
            self.ui.label_sambo_image.setScaledContents(True)
            self.ui.label_sambo_image.setPixmap(pixmap)

        elif extension == "mp4" or extension == "MP4":
            self.ui.file_type.setText("video/mp4")
            self.videoWidget.setVisible(True)
            self.ui.label_sambo_image.setVisible(False)
            self.ui.pushButton_video_control.setEnabled(True)
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(__filename)))
            self.mediaPlayer.play()
            self.mediaPlayer.pause()

        self.open_file_path = os.path.dirname(__filename)

    def __video_control(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.ui.pushButton_video_control.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))
        else:
            self.mediaPlayer.play()
            self.ui.pushButton_video_control.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))

    def __video_set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def __video_position_changed(self, position):
        self.ui.horizontalSlider.setValue(position)

    def __save_personal_information(self, *args):
        settings = QtCore.QSettings('report_system', 'QSetting')
        personal_name = self.ui.lineEdit_personal_name.text()
        personal_id = self.ui.lineEdit_personal_id.text()
        personal_phone = self.ui.lineEdit_personal_phone.text()
        personal_address = self.ui.lineEdit_personal_address.text()
        personal_email = self.ui.lineEdit_personal_email.text()

        settings.setValue('personal_name', personal_name)
        settings.setValue('personal_id', personal_id)
        settings.setValue('personal_phone', personal_phone)
        settings.setValue('personal_address', personal_address)
        settings.setValue('personal_email', personal_email)
        settings.setValue('personal_file_path', self.open_file_path)
        if not args:
            QMessageBox.information(self, 'Message', '儲存成功', QMessageBox.Ok)

    def __start_upload(self, **kwargs):
        # for check status
        if kwargs.get("lainformation_parameter"):
            information_parameter = kwargs.get("lainformation_parameter")
            dlg = UploadDialog(information_parameter)
            dlg.ui.pushButton_accept.setVisible(False)
            dlg.ui.pushButton_reject.setVisible(False)
            dlg.exec_()

        # current upload
        else:
            car_type = self.ui.comboBox_sampbo_car_type.currentText()
            date = self.ui.calendarWidget.selectedDate().toString("yyyy/MM/dd")
            _time = self.ui.timeEdit.time().toString()
            date_time = date + "  " + _time
            violate_date = date_time

            information_parameter = {
                "personal": {"name": self.ui.lineEdit_personal_name.text(),
                             "id": self.ui.lineEdit_personal_id.text(),
                             "phone": self.ui.lineEdit_personal_phone.text(),
                             "address": self.ui.lineEdit_personal_address.text(),
                             "email": self.ui.lineEdit_personal_email.text()
                             },
                "sambo": {
                    "car_type": car_type,
                    "car_number": self.ui.lineEdit_sambo_car_number.text(),
                    "violate_town": self.ui.lineEdit_sambo_violate_town.text(),
                    "violate_street_1": self.ui.lineEdit_sambo_street_1.text(),
                    "violate_street_2": self.ui.lineEdit_sambo_street_2.text(),
                    "violate_position": self.ui.lineEdit_sampbo_position.text(),
                    "violate_fact": self.ui.comboBox_sampbo_violate_dest.currentText(),
                    "violate_date": violate_date,
                },
                "file": {
                    "name": self.ui.file_name.text(),
                    "type": self.ui.file_type.text(),
                }
            }
            dlg = UploadDialog(information_parameter)
            result = dlg.exec_()

            if result == 1:
                car_number = information_parameter.get("sambo").get("car_number")
                self.uploading_parameter.update({car_number: information_parameter})
                button = UploadButton(car_number + "   Uploading")
                button.clicked.connect(lambda: self.__start_upload(lainformation_parameter=information_parameter))
                upload_frame_count = self.ui.gridLayout_9.count()
                self.ui.gridLayout_9.addWidget(button, upload_frame_count + 1, 0, 1, 1)
                threading.Thread(target=self.__upload_thread, args=(car_number, button, information_parameter)).start()
                self.__init_element_when_upload_click()

    def __init_element_when_upload_click(self):
        self.ui.comboBox_sampbo_car_type.setCurrentIndex(-1)
        self.ui.comboBox_sampbo_violate_dest.setCurrentIndex(-1)
        self.ui.lineEdit_sambo_car_number.clear()
        self.ui.lineEdit_sambo_street_1.clear()
        self.ui.lineEdit_sambo_street_2.clear()
        self.ui.file_name.clear()
        self.ui.file_type.clear()
        self.ui.lineEdit_sampbo_position.clear()
        self.videoWidget.setVisible(False)
        self.ui.label_sambo_image.setVisible(True)
        self.ui.pushButton_video_control.setEnabled(False)
        self.ui.label_sambo_image.setText("Image/Video Resource")

    def __upload_thread(self, car_number, button, information_parameter):
        self.upload_parameter = {}

        # 獲得所需參數
        personal_name = information_parameter.get("personal").get("name")
        personal_id = information_parameter.get("personal").get("id")
        personal_phone = information_parameter.get("personal").get("phone")
        personal_address = information_parameter.get("personal").get("address")
        personal_email = information_parameter.get("personal").get("email")
        sambo_car_type = information_parameter.get("sambo").get("car_type")
        sambo_car_number = information_parameter.get("sambo").get("car_number")
        violate_town = information_parameter.get("sambo").get("violate_town")
        violate_street_1 = information_parameter.get("sambo").get("violate_street_1")
        violate_street_2 = information_parameter.get("sambo").get("violate_street_2")
        violate_position = information_parameter.get("sambo").get("violate_position")
        violate_fact = information_parameter.get("sambo").get("violate_fact")
        violate_date = information_parameter.get("sambo").get("violate_date")
        file_name_dir = information_parameter.get("file").get("name")
        file_type = information_parameter.get("file").get("type")

        # 上傳用header
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-CN;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "Cookie": "CheckCode=X4B6",
        }

        # get view_state and event_validation **necessary
        requests_session = requests.session()
        result = requests_session.get("https://jiaowei.ncpb.gov.tw/sc11/rwd/rincase3.aspx", verify=False)
        soup = BeautifulSoup(result.text, 'html.parser')
        view_state = soup.find("input", id="__VIEWSTATE").get("value")
        event_validation = soup.find("input", id="__EVENTVALIDATION").get("value")

        self.__update_parameter("__VIEWSTATE", view_state)
        self.__update_parameter("__EVENTVALIDATION", event_validation)

        # add other parameter
        date_time = str(violate_date).split("  ")[0]
        date_time_hour = int(str(violate_date).split("  ")[1].split(":")[0])
        date_time_minute = int(str(violate_date).split("  ")[1].split(":")[1])

        self.__update_parameter('__LASTFOCUS', "")
        self.__update_parameter('__EVENTTARGET', "")
        self.__update_parameter('__EVENTARGUMENT', "")
        self.__update_parameter('__VIEWSTATEGENERATOR', "82C0E329")

        self.__update_parameter('mname', personal_name)
        self.__update_parameter('mpid', personal_id)
        self.__update_parameter('mtel', personal_phone)
        self.__update_parameter('maddr', personal_address)
        self.__update_parameter('memail', personal_email)
        self.__update_parameter('mcarclass', sambo_car_type)
        self.__update_parameter('mcarno', sambo_car_number)
        self.__update_parameter('Loc1', "540")
        self.__update_parameter('Loc2', violate_street_1)
        self.__update_parameter('mcaraddr', violate_position)
        self.__update_parameter('txtDate', date_time)
        self.__update_parameter('mcarhour', date_time_hour)
        self.__update_parameter('mcarmitu', date_time_minute)
        self.__update_parameter('mcarblack', violate_fact)
        self.__update_parameter('mcode', "X4B6")
        self.__update_parameter('Button1', "資料上傳")

        # add image or video
        with open(file_name_dir, "rb+") as file:
            img_binary = file.read()
        file_name = file_name_dir.split("/")[-1]
        self.upload_parameter.update({"FileUpload1": (file_name, img_binary, file_type)})

        result = requests_session.post("https://jiaowei.ncpb.gov.tw/sc11/rwd/rincase3.aspx", verify=False,
                                       headers=header, files=self.upload_parameter)

        if result.url == "https://jiaowei.ncpb.gov.tw/sc11/rwd/rfinish.aspx":
            button.setText(car_number + "   Upload Success")
            button.setStyleSheet("	background-color: rgb(49, 197, 84);")
        else:
            button.setText(car_number + "   Upload Fail")
            button.setStyleSheet("	background-color: color: rgb(255, 255, 255);")

    def __update_parameter(self, key, value):
        parameter = {key: (None, value)}
        self.upload_parameter.update(parameter)

    def __combo_box_hour_click_func(self, index):
        minute = self.ui.timeEdit.time().minute()
        self.ui.timeEdit.setTime(QTime(index, minute, 0, 0))

    def __combo_box_minute_click_func(self, index):
        hour = self.ui.timeEdit.time().hour()
        self.ui.timeEdit.setTime(QTime(hour, index, 0, 0))


class UploadDialog(QDialog):
    def __init__(self, information_parameter):
        super(UploadDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_accept.clicked.connect(self.__accept)
        self.ui.pushButton_reject.clicked.connect(self.__reject)
        self.ui.tableWidget.verticalHeader().setMinimumWidth(105)
        self.information_parameter = information_parameter
        self.__value()

    def __value(self):
        personal_name = self.information_parameter.get("personal").get("name")
        personal_id = self.information_parameter.get("personal").get("id")
        personal_phone = self.information_parameter.get("personal").get("phone")
        personal_address = self.information_parameter.get("personal").get("address")
        personal_email = self.information_parameter.get("personal").get("email")

        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(personal_name))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(personal_id))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(personal_phone))
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem(personal_address))
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem(personal_email))

        sambo_car_type = self.information_parameter.get("sambo").get("car_type")
        sambo_car_number = self.information_parameter.get("sambo").get("car_number")
        violate_town = self.information_parameter.get("sambo").get("violate_town")
        violate_street_1 = self.information_parameter.get("sambo").get("violate_street_1")
        violate_street_2 = self.information_parameter.get("sambo").get("violate_street_2")

        violate_position = self.information_parameter.get("sambo").get("violate_position")
        violate_fact = self.information_parameter.get("sambo").get("violate_fact")
        violate_date = self.information_parameter.get("sambo").get("violate_date")
        file_name = self.information_parameter.get("file").get("name")
        if file_name:
            file_name = str(file_name).split("/")[-1].split(".")[0]
        file_type = self.information_parameter.get("file").get("type")

        self.ui.tableWidget_2.setItem(0, 0, TableItem(sambo_car_type))
        self.ui.tableWidget_2.setItem(0, 1, TableItem(sambo_car_number))
        self.ui.tableWidget_2.setItem(0, 2, TableItem(violate_town))
        self.ui.tableWidget_2.setItem(0, 3, TableItem(violate_position))
        self.ui.tableWidget_2.setItem(0, 4, TableItem(violate_fact))
        self.ui.tableWidget_2.setItem(0, 5, TableItem(violate_date))
        self.ui.tableWidget_2.setItem(0, 6, TableItem(file_name))
        self.ui.tableWidget_2.setItem(0, 7, TableItem(file_type))

        for key, value in self.information_parameter.items():
            for key1, value1 in value.items():
                if not value1 and not key1 == "violate_street_2":
                    self.ui.pushButton_accept.setEnabled(False)
                    break
            else:
                continue
            break

    def __accept(self):
        self.done(1)
        self.close()

    def __reject(self):
        self.done(0)
        self.close()


class TableItem(QTableWidgetItem):
    def __init__(self, text):
        super(TableItem, self).__init__()
        self.setText(text)
        if not text:
            self.setBackgroundColor(QColor("red"))


class UploadButton(QPushButton):
    def __init__(self, button_name):
        super(UploadButton, self).__init__()
        self.setText(button_name)
        self.setCursor(QCursor(Qt.PointingHandCursor))
