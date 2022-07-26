# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sambo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1314, 686)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_10 = QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -509, 333, 1177))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents_3)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(333, 0))
        self.frame.setMaximumSize(QSize(333, 16777215))
        self.frame.setStyleSheet(u".QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"text-align : left;\n"
"border:0px;\n"
"}\n"
"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 0, 9, 6)
        self.pushButton_personal_phone = QPushButton(self.frame_2)
        self.pushButton_personal_phone.setObjectName(u"pushButton_personal_phone")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_personal_phone.sizePolicy().hasHeightForWidth())
        self.pushButton_personal_phone.setSizePolicy(sizePolicy2)
        self.pushButton_personal_phone.setMinimumSize(QSize(100, 25))
        self.pushButton_personal_phone.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setFamily(u"\u5fae\u8edf\u6b63\u9ed1\u9ad4")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_personal_phone.setFont(font)
        self.pushButton_personal_phone.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_personal_phone.setFocusPolicy(Qt.NoFocus)
        self.pushButton_personal_phone.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.pushButton_personal_phone, 4, 0, 1, 1)

        self.lineEdit_personal_address = QLineEdit(self.frame_2)
        self.lineEdit_personal_address.setObjectName(u"lineEdit_personal_address")
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8edf\u6b63\u9ed1\u9ad4")
        font1.setPointSize(11)
        self.lineEdit_personal_address.setFont(font1)
        self.lineEdit_personal_address.setTabletTracking(False)

        self.gridLayout_3.addWidget(self.lineEdit_personal_address, 8, 0, 1, 2)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout_3.addWidget(self.label_15, 4, 1, 1, 1)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.gridLayout_3.addWidget(self.label_16, 7, 1, 1, 1)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.gridLayout_3.addWidget(self.label_17, 10, 1, 1, 1)

        self.lineEdit_personal_name = QLineEdit(self.frame_2)
        self.lineEdit_personal_name.setObjectName(u"lineEdit_personal_name")
        self.lineEdit_personal_name.setFont(font1)
        self.lineEdit_personal_name.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout_3.addWidget(self.lineEdit_personal_name, 1, 0, 1, 2)

        self.pushButton_personal_address = QPushButton(self.frame_2)
        self.pushButton_personal_address.setObjectName(u"pushButton_personal_address")
        sizePolicy2.setHeightForWidth(self.pushButton_personal_address.sizePolicy().hasHeightForWidth())
        self.pushButton_personal_address.setSizePolicy(sizePolicy2)
        self.pushButton_personal_address.setMinimumSize(QSize(100, 25))
        self.pushButton_personal_address.setMaximumSize(QSize(100, 16777215))
        self.pushButton_personal_address.setFont(font)
        self.pushButton_personal_address.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_personal_address.setFocusPolicy(Qt.NoFocus)
        self.pushButton_personal_address.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.pushButton_personal_address, 7, 0, 1, 1)

        self.pushButton_personal_email = QPushButton(self.frame_2)
        self.pushButton_personal_email.setObjectName(u"pushButton_personal_email")
        sizePolicy2.setHeightForWidth(self.pushButton_personal_email.sizePolicy().hasHeightForWidth())
        self.pushButton_personal_email.setSizePolicy(sizePolicy2)
        self.pushButton_personal_email.setMinimumSize(QSize(100, 25))
        self.pushButton_personal_email.setMaximumSize(QSize(100, 16777215))
        self.pushButton_personal_email.setFont(font)
        self.pushButton_personal_email.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_personal_email.setFocusPolicy(Qt.NoFocus)
        self.pushButton_personal_email.setStyleSheet(u"border:0px")

        self.gridLayout_3.addWidget(self.pushButton_personal_email, 10, 0, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_3.addWidget(self.label_14, 2, 1, 1, 1)

        self.pushButton_personal_id = QPushButton(self.frame_2)
        self.pushButton_personal_id.setObjectName(u"pushButton_personal_id")
        sizePolicy2.setHeightForWidth(self.pushButton_personal_id.sizePolicy().hasHeightForWidth())
        self.pushButton_personal_id.setSizePolicy(sizePolicy2)
        self.pushButton_personal_id.setMinimumSize(QSize(100, 25))
        self.pushButton_personal_id.setMaximumSize(QSize(100, 16777215))
        self.pushButton_personal_id.setFont(font)
        self.pushButton_personal_id.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_personal_id.setFocusPolicy(Qt.NoFocus)
        self.pushButton_personal_id.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.pushButton_personal_id, 2, 0, 1, 1)

        self.pushButton_personal_name = QPushButton(self.frame_2)
        self.pushButton_personal_name.setObjectName(u"pushButton_personal_name")
        sizePolicy2.setHeightForWidth(self.pushButton_personal_name.sizePolicy().hasHeightForWidth())
        self.pushButton_personal_name.setSizePolicy(sizePolicy2)
        self.pushButton_personal_name.setMinimumSize(QSize(100, 25))
        self.pushButton_personal_name.setMaximumSize(QSize(100, 16777215))
        self.pushButton_personal_name.setFont(font)
        self.pushButton_personal_name.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_personal_name.setFocusPolicy(Qt.NoFocus)
        self.pushButton_personal_name.setStyleSheet(u"")
        self.pushButton_personal_name.setAutoDefault(False)
        self.pushButton_personal_name.setFlat(False)

        self.gridLayout_3.addWidget(self.pushButton_personal_name, 0, 0, 1, 1)

        self.lineEdit_personal_email = QLineEdit(self.frame_2)
        self.lineEdit_personal_email.setObjectName(u"lineEdit_personal_email")
        self.lineEdit_personal_email.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit_personal_email, 11, 0, 1, 2)

        self.lineEdit_personal_id = QLineEdit(self.frame_2)
        self.lineEdit_personal_id.setObjectName(u"lineEdit_personal_id")
        self.lineEdit_personal_id.setFont(font1)
        self.lineEdit_personal_id.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout_3.addWidget(self.lineEdit_personal_id, 3, 0, 1, 2)

        self.lineEdit_personal_phone = QLineEdit(self.frame_2)
        self.lineEdit_personal_phone.setObjectName(u"lineEdit_personal_phone")
        self.lineEdit_personal_phone.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit_personal_phone, 5, 0, 1, 2)


        self.gridLayout_7.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QPushButton{\n"
"	text-align : left;\n"
"	border:0px;\n"
"}\n"
"\n"
".QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_sambo_car_type = QPushButton(self.frame_5)
        self.pushButton_sambo_car_type.setObjectName(u"pushButton_sambo_car_type")
        sizePolicy.setHeightForWidth(self.pushButton_sambo_car_type.sizePolicy().hasHeightForWidth())
        self.pushButton_sambo_car_type.setSizePolicy(sizePolicy)
        self.pushButton_sambo_car_type.setMinimumSize(QSize(0, 25))
        self.pushButton_sambo_car_type.setMaximumSize(QSize(100, 16777215))
        self.pushButton_sambo_car_type.setFont(font)
        self.pushButton_sambo_car_type.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_sambo_car_type.setFocusPolicy(Qt.NoFocus)
        self.pushButton_sambo_car_type.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.pushButton_sambo_car_type)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_8)


        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 1)

        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_sambo_date = QPushButton(self.frame_13)
        self.pushButton_sambo_date.setObjectName(u"pushButton_sambo_date")
        sizePolicy2.setHeightForWidth(self.pushButton_sambo_date.sizePolicy().hasHeightForWidth())
        self.pushButton_sambo_date.setSizePolicy(sizePolicy2)
        self.pushButton_sambo_date.setMinimumSize(QSize(0, 25))
        self.pushButton_sambo_date.setMaximumSize(QSize(100, 16777215))
        self.pushButton_sambo_date.setFont(font)
        self.pushButton_sambo_date.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_sambo_date.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.pushButton_sambo_date)

        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8edf\u6b63\u9ed1\u9ad4")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_5.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_5)


        self.gridLayout_2.addWidget(self.frame_13, 10, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_sambo_car_id = QPushButton(self.frame_6)
        self.pushButton_sambo_car_id.setObjectName(u"pushButton_sambo_car_id")
        sizePolicy2.setHeightForWidth(self.pushButton_sambo_car_id.sizePolicy().hasHeightForWidth())
        self.pushButton_sambo_car_id.setSizePolicy(sizePolicy2)
        self.pushButton_sambo_car_id.setMinimumSize(QSize(0, 25))
        self.pushButton_sambo_car_id.setMaximumSize(QSize(100, 16777215))
        self.pushButton_sambo_car_id.setFont(font)
        self.pushButton_sambo_car_id.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_sambo_car_id.setFocusPolicy(Qt.NoFocus)
        self.pushButton_sambo_car_id.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.pushButton_sambo_car_id)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_9)


        self.gridLayout_2.addWidget(self.frame_6, 4, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_sambo_car_town_position = QPushButton(self.frame_8)
        self.pushButton_sambo_car_town_position.setObjectName(u"pushButton_sambo_car_town_position")
        sizePolicy.setHeightForWidth(self.pushButton_sambo_car_town_position.sizePolicy().hasHeightForWidth())
        self.pushButton_sambo_car_town_position.setSizePolicy(sizePolicy)
        self.pushButton_sambo_car_town_position.setMinimumSize(QSize(0, 25))
        self.pushButton_sambo_car_town_position.setMaximumSize(QSize(100, 16777215))
        self.pushButton_sambo_car_town_position.setFont(font)
        self.pushButton_sambo_car_town_position.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_sambo_car_town_position.setFocusPolicy(Qt.NoFocus)
        self.pushButton_sambo_car_town_position.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.pushButton_sambo_car_town_position)

        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_13)


        self.gridLayout_2.addWidget(self.frame_8, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.gridLayout_11 = QGridLayout(self.frame_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_sambo_street_1 = QLineEdit(self.frame_9)
        self.lineEdit_sambo_street_1.setObjectName(u"lineEdit_sambo_street_1")
        sizePolicy.setHeightForWidth(self.lineEdit_sambo_street_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_sambo_street_1.setSizePolicy(sizePolicy)
        self.lineEdit_sambo_street_1.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit_sambo_street_1)

        self.lineEdit_sambo_street_2 = QLineEdit(self.frame_9)
        self.lineEdit_sambo_street_2.setObjectName(u"lineEdit_sambo_street_2")
        sizePolicy.setHeightForWidth(self.lineEdit_sambo_street_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_sambo_street_2.setSizePolicy(sizePolicy)
        self.lineEdit_sambo_street_2.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit_sambo_street_2)


        self.gridLayout_11.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listWidget_sambo_street1 = QListWidget(self.frame_9)
        self.listWidget_sambo_street1.setObjectName(u"listWidget_sambo_street1")
        sizePolicy.setHeightForWidth(self.listWidget_sambo_street1.sizePolicy().hasHeightForWidth())
        self.listWidget_sambo_street1.setSizePolicy(sizePolicy)
        self.listWidget_sambo_street1.setMinimumSize(QSize(0, 120))
        self.listWidget_sambo_street1.setFont(font1)

        self.horizontalLayout_2.addWidget(self.listWidget_sambo_street1)

        self.listWidget_sambo_street2 = QListWidget(self.frame_9)
        self.listWidget_sambo_street2.setObjectName(u"listWidget_sambo_street2")
        sizePolicy.setHeightForWidth(self.listWidget_sambo_street2.sizePolicy().hasHeightForWidth())
        self.listWidget_sambo_street2.setSizePolicy(sizePolicy)
        self.listWidget_sambo_street2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.listWidget_sambo_street2)


        self.gridLayout_11.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.lineEdit_sampbo_position = QLineEdit(self.frame_9)
        self.lineEdit_sampbo_position.setObjectName(u"lineEdit_sampbo_position")
        sizePolicy.setHeightForWidth(self.lineEdit_sampbo_position.sizePolicy().hasHeightForWidth())
        self.lineEdit_sampbo_position.setSizePolicy(sizePolicy)
        self.lineEdit_sampbo_position.setFont(font1)

        self.gridLayout_11.addWidget(self.lineEdit_sampbo_position, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_9, 7, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_sambo_event_desc = QPushButton(self.frame_11)
        self.pushButton_sambo_event_desc.setObjectName(u"pushButton_sambo_event_desc")
        sizePolicy2.setHeightForWidth(self.pushButton_sambo_event_desc.sizePolicy().hasHeightForWidth())
        self.pushButton_sambo_event_desc.setSizePolicy(sizePolicy2)
        self.pushButton_sambo_event_desc.setMinimumSize(QSize(0, 25))
        self.pushButton_sambo_event_desc.setMaximumSize(QSize(100, 16777215))
        self.pushButton_sambo_event_desc.setFont(font)
        self.pushButton_sambo_event_desc.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_sambo_event_desc.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_7.addWidget(self.pushButton_sambo_event_desc)

        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.gridLayout_2.addWidget(self.frame_11, 8, 0, 1, 1)

        self.comboBox_sampbo_car_type = QComboBox(self.frame_7)
        self.comboBox_sampbo_car_type.addItem("")
        self.comboBox_sampbo_car_type.addItem("")
        self.comboBox_sampbo_car_type.addItem("")
        self.comboBox_sampbo_car_type.addItem("")
        self.comboBox_sampbo_car_type.addItem("")
        self.comboBox_sampbo_car_type.addItem("")
        self.comboBox_sampbo_car_type.addItem("")
        self.comboBox_sampbo_car_type.addItem("")
        self.comboBox_sampbo_car_type.setObjectName(u"comboBox_sampbo_car_type")
        font3 = QFont()
        font3.setFamily(u"\u5fae\u8edf\u6b63\u9ed1\u9ad4")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.comboBox_sampbo_car_type.setFont(font3)
        self.comboBox_sampbo_car_type.setAutoFillBackground(True)
        self.comboBox_sampbo_car_type.setStyleSheet(u"")
        self.comboBox_sampbo_car_type.setEditable(False)
        self.comboBox_sampbo_car_type.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_sampbo_car_type.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox_sampbo_car_type.setMinimumContentsLength(0)

        self.gridLayout_2.addWidget(self.comboBox_sampbo_car_type, 3, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_sambo_car_position = QPushButton(self.frame_10)
        self.pushButton_sambo_car_position.setObjectName(u"pushButton_sambo_car_position")
        sizePolicy2.setHeightForWidth(self.pushButton_sambo_car_position.sizePolicy().hasHeightForWidth())
        self.pushButton_sambo_car_position.setSizePolicy(sizePolicy2)
        self.pushButton_sambo_car_position.setMinimumSize(QSize(0, 25))
        self.pushButton_sambo_car_position.setMaximumSize(QSize(100, 16777215))
        self.pushButton_sambo_car_position.setFont(font)
        self.pushButton_sambo_car_position.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_sambo_car_position.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_6.addWidget(self.pushButton_sambo_car_position)

        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(100, 0))
        self.label_10.setFont(font2)
        self.label_10.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout_6.addWidget(self.label_10)


        self.gridLayout_2.addWidget(self.frame_10, 6, 0, 1, 1)

        self.comboBox_sampbo_violate_dest = QComboBox(self.frame_7)
        self.comboBox_sampbo_violate_dest.addItem("")
        self.comboBox_sampbo_violate_dest.addItem("")
        self.comboBox_sampbo_violate_dest.addItem("")
        self.comboBox_sampbo_violate_dest.addItem("")
        self.comboBox_sampbo_violate_dest.addItem("")
        self.comboBox_sampbo_violate_dest.setObjectName(u"comboBox_sampbo_violate_dest")
        self.comboBox_sampbo_violate_dest.setFont(font3)
        self.comboBox_sampbo_violate_dest.setAutoFillBackground(True)
        self.comboBox_sampbo_violate_dest.setStyleSheet(u"QComboBox::editable{\n"
"	font: 11pt \"\u5fae\u8edf\u6b63\u9ed1\u9ad4\";\n"
"}")
        self.comboBox_sampbo_violate_dest.setEditable(True)
        self.comboBox_sampbo_violate_dest.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox_sampbo_violate_dest.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox_sampbo_violate_dest.setMinimumContentsLength(0)

        self.gridLayout_2.addWidget(self.comboBox_sampbo_violate_dest, 9, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.gridLayout_12 = QGridLayout(self.frame_12)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.calendarWidget = QCalendarWidget(self.frame_12)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QSize(0, 0))
        self.calendarWidget.setMaximumSize(QSize(16777215, 16777215))
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet(u"selection-background-color: rgb(61, 122, 197);\n"
"selection-color: rgb(255, 255, 255);")
        self.calendarWidget.setFirstDayOfWeek(Qt.Sunday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setDateEditAcceptDelay(1501)

        self.gridLayout_12.addWidget(self.calendarWidget, 0, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.frame_12)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setWeight(50)
        self.timeEdit.setFont(font4)
        self.timeEdit.setProperty("showGroupSeparator", False)
        self.timeEdit.setCurrentSection(QDateTimeEdit.HourSection)
        self.timeEdit.setTime(QTime(17, 0, 0))

        self.gridLayout_12.addWidget(self.timeEdit, 1, 0, 1, 1)

        self.frame_19 = QFrame(self.frame_12)
        self.frame_19.setObjectName(u"frame_19")
        self.horizontalLayout_13 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_19)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamily(u"Calibri")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_7.setFont(font5)

        self.horizontalLayout_13.addWidget(self.label_7)

        self.comboBox_hour = QComboBox(self.frame_19)
        self.comboBox_hour.setObjectName(u"comboBox_hour")
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(14)
        self.comboBox_hour.setFont(font6)

        self.horizontalLayout_13.addWidget(self.comboBox_hour)

        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setFont(font5)

        self.horizontalLayout_13.addWidget(self.label_11)

        self.comboBox_minute = QComboBox(self.frame_19)
        self.comboBox_minute.setObjectName(u"comboBox_minute")
        self.comboBox_minute.setFont(font6)

        self.horizontalLayout_13.addWidget(self.comboBox_minute)


        self.gridLayout_12.addWidget(self.frame_19, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_12, 11, 0, 1, 1)

        self.lineEdit_sambo_violate_town = QLineEdit(self.frame_7)
        self.lineEdit_sambo_violate_town.setObjectName(u"lineEdit_sambo_violate_town")
        self.lineEdit_sambo_violate_town.setEnabled(False)
        self.lineEdit_sambo_violate_town.setFont(font1)
        self.lineEdit_sambo_violate_town.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.lineEdit_sambo_violate_town, 1, 0, 1, 1)

        self.lineEdit_sambo_car_number = QLineEdit(self.frame_7)
        self.lineEdit_sambo_car_number.setObjectName(u"lineEdit_sambo_car_number")
        self.lineEdit_sambo_car_number.setFont(font1)

        self.gridLayout_2.addWidget(self.lineEdit_sambo_car_number, 5, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_7, 3, 0, 1, 1)

        self.frame_16 = QFrame(self.frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(98, 98, 98);\n"
"	border:1px solid black;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align : left;\n"
"	border:0px solid black;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_sambo_car_info = QPushButton(self.frame_16)
        self.pushButton_sambo_car_info.setObjectName(u"pushButton_sambo_car_info")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_sambo_car_info.sizePolicy().hasHeightForWidth())
        self.pushButton_sambo_car_info.setSizePolicy(sizePolicy4)
        self.pushButton_sambo_car_info.setMinimumSize(QSize(255, 30))
        font7 = QFont()
        font7.setFamily(u"\u5fae\u8edf\u6b63\u9ed1\u9ad4")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.pushButton_sambo_car_info.setFont(font7)
        self.pushButton_sambo_car_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_sambo_car_info.setFocusPolicy(Qt.NoFocus)
        self.pushButton_sambo_car_info.setStyleSheet(u"text-align : left;\n"
"border:0px solid black;\n"
"")

        self.horizontalLayout_12.addWidget(self.pushButton_sambo_car_info)

        self.pushButton_sambo_status_2 = QPushButton(self.frame_16)
        self.pushButton_sambo_status_2.setObjectName(u"pushButton_sambo_status_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_sambo_status_2.sizePolicy().hasHeightForWidth())
        self.pushButton_sambo_status_2.setSizePolicy(sizePolicy5)
        self.pushButton_sambo_status_2.setMinimumSize(QSize(0, 30))
        self.pushButton_sambo_status_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_sambo_status_2.setFocusPolicy(Qt.NoFocus)
        self.pushButton_sambo_status_2.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.pushButton_sambo_status_2)


        self.gridLayout_7.addWidget(self.frame_16, 2, 0, 1, 1)

        self.frame_15 = QFrame(self.frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(98, 98, 98);\n"
"	border:1px solid black;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align : left;\n"
"	border:0px solid black;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_personal_info = QPushButton(self.frame_15)
        self.pushButton_personal_info.setObjectName(u"pushButton_personal_info")
        self.pushButton_personal_info.setMinimumSize(QSize(200, 30))
        self.pushButton_personal_info.setFont(font7)
        self.pushButton_personal_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_personal_info.setFocusPolicy(Qt.NoFocus)
        self.pushButton_personal_info.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pushButton_personal_info.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_personal_info.setStyleSheet(u"text-align : left;\n"
"border:0px solid black;\n"
"")

        self.horizontalLayout_11.addWidget(self.pushButton_personal_info)

        self.pushButton_personal_save = QPushButton(self.frame_15)
        self.pushButton_personal_save.setObjectName(u"pushButton_personal_save")
        sizePolicy5.setHeightForWidth(self.pushButton_personal_save.sizePolicy().hasHeightForWidth())
        self.pushButton_personal_save.setSizePolicy(sizePolicy5)
        self.pushButton_personal_save.setMinimumSize(QSize(0, 30))
        self.pushButton_personal_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_personal_save.setFocusPolicy(Qt.NoFocus)
        self.pushButton_personal_save.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.pushButton_personal_save)

        self.horizontalSpacer_2 = QSpacerItem(15, 15, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.pushButton_personal_status = QPushButton(self.frame_15)
        self.pushButton_personal_status.setObjectName(u"pushButton_personal_status")
        sizePolicy5.setHeightForWidth(self.pushButton_personal_status.sizePolicy().hasHeightForWidth())
        self.pushButton_personal_status.setSizePolicy(sizePolicy5)
        self.pushButton_personal_status.setMinimumSize(QSize(0, 30))
        self.pushButton_personal_status.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_personal_status.setFocusPolicy(Qt.NoFocus)
        self.pushButton_personal_status.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.pushButton_personal_status)


        self.gridLayout_7.addWidget(self.frame_15, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_10.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy6)
        self.frame_3.setStyleSheet(u".QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_video_control = QPushButton(self.frame_4)
        self.pushButton_video_control.setObjectName(u"pushButton_video_control")
        self.pushButton_video_control.setMinimumSize(QSize(30, 30))
        self.pushButton_video_control.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.pushButton_video_control, 0, 0, 1, 1)

        self.horizontalSlider = QSlider(self.frame_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setFocusPolicy(Qt.NoFocus)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.horizontalSlider, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_4, 3, 0, 1, 1)

        self.pushButton_upload = QPushButton(self.frame_3)
        self.pushButton_upload.setObjectName(u"pushButton_upload")
        font8 = QFont()
        font8.setFamily(u"Calibri")
        font8.setPointSize(25)
        font8.setBold(True)
        font8.setWeight(75)
        self.pushButton_upload.setFont(font8)
        self.pushButton_upload.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_upload.setFocusPolicy(Qt.NoFocus)
        self.pushButton_upload.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border : 1px solid gray;\n"
"border-radius : 15px\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(198, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(255, 85, 0);\n"
"}")

        self.gridLayout_8.addWidget(self.pushButton_upload, 4, 0, 1, 1)

        self.label_sambo_image = QLabel(self.frame_3)
        self.label_sambo_image.setObjectName(u"label_sambo_image")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_sambo_image.sizePolicy().hasHeightForWidth())
        self.label_sambo_image.setSizePolicy(sizePolicy7)
        font9 = QFont()
        font9.setFamily(u"Calibri")
        font9.setPointSize(36)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_sambo_image.setFont(font9)
        self.label_sambo_image.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_sambo_image, 1, 0, 1, 1)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy8)
        self.frame_14.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_6 = QGridLayout(self.frame_14)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, -1, -1, -1)
        self.label_2 = QLabel(self.frame_14)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(130, 0))
        font10 = QFont()
        font10.setFamily(u"Calibri")
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_2.setFont(font10)

        self.horizontalLayout_9.addWidget(self.label_2)

        self.file_name = QLineEdit(self.frame_14)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setEnabled(False)
        font11 = QFont()
        font11.setPointSize(14)
        self.file_name.setFont(font11)
        self.file_name.setCursor(QCursor(Qt.ArrowCursor))
        self.file_name.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.file_name)

        self.file_exploer = QToolButton(self.frame_14)
        self.file_exploer.setObjectName(u"file_exploer")
        self.file_exploer.setMinimumSize(QSize(40, 0))
        self.file_exploer.setFont(font5)
        self.file_exploer.setCursor(QCursor(Qt.PointingHandCursor))
        self.file_exploer.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_9.addWidget(self.file_exploer)


        self.gridLayout_6.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, -1, -1, -1)
        self.label_3 = QLabel(self.frame_14)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(130, 0))
        self.label_3.setFont(font10)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.file_type = QLineEdit(self.frame_14)
        self.file_type.setObjectName(u"file_type")
        self.file_type.setEnabled(False)
        sizePolicy.setHeightForWidth(self.file_type.sizePolicy().hasHeightForWidth())
        self.file_type.setSizePolicy(sizePolicy)
        self.file_type.setSizeIncrement(QSize(300, 0))
        self.file_type.setFont(font11)
        self.file_type.setCursor(QCursor(Qt.ArrowCursor))
        self.file_type.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_10.addWidget(self.file_type)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)


        self.gridLayout_6.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_14, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_18 = QFrame(self.centralwidget)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_18)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, -1, 6, 0)
        self.label_4 = QLabel(self.frame_18)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setFont(font7)
        self.label_4.setStyleSheet(u"background-color: rgb(98, 98, 98);\n"
"border:1px solid black;\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.frame_17 = QFrame(self.frame_18)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(200, 0))
        self.frame_17.setStyleSheet(u"QPushButton{\n"
"	font: 75 14pt \"Calibri\";\n"
"	border : 1px solid grey;\n"
"	background-color: rgb(255, 85, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	height:30px;\n"
"}\n"
"QFrame{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_17)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, -1)

        self.gridLayout.addWidget(self.frame_17, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 601, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_18, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit_personal_name, self.lineEdit_personal_id)
        QWidget.setTabOrder(self.lineEdit_personal_id, self.lineEdit_personal_phone)
        QWidget.setTabOrder(self.lineEdit_personal_phone, self.lineEdit_personal_address)
        QWidget.setTabOrder(self.lineEdit_personal_address, self.lineEdit_personal_email)
        QWidget.setTabOrder(self.lineEdit_personal_email, self.comboBox_sampbo_car_type)
        QWidget.setTabOrder(self.comboBox_sampbo_car_type, self.lineEdit_sambo_car_number)
        QWidget.setTabOrder(self.lineEdit_sambo_car_number, self.lineEdit_sambo_street_1)
        QWidget.setTabOrder(self.lineEdit_sambo_street_1, self.listWidget_sambo_street1)
        QWidget.setTabOrder(self.listWidget_sambo_street1, self.lineEdit_sambo_street_2)
        QWidget.setTabOrder(self.lineEdit_sambo_street_2, self.listWidget_sambo_street2)
        QWidget.setTabOrder(self.listWidget_sambo_street2, self.comboBox_sampbo_violate_dest)
        QWidget.setTabOrder(self.comboBox_sampbo_violate_dest, self.calendarWidget)
        QWidget.setTabOrder(self.calendarWidget, self.timeEdit)
        QWidget.setTabOrder(self.timeEdit, self.scrollArea)

        self.retranslateUi(MainWindow)

        self.pushButton_personal_name.setDefault(False)
        self.comboBox_sampbo_car_type.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_personal_phone.setText(QCoreApplication.translate("MainWindow", u"\u9023\u7d61\u96fb\u8a71", None))
        self.lineEdit_personal_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u901a\u8a0a\u5730\u5740(\u5fc5\u586b)", None))
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.lineEdit_personal_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u59d3\u540d(\u5fc5\u586b)", None))
        self.pushButton_personal_address.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8a0a\u5730\u5740", None))
        self.pushButton_personal_email.setText(QCoreApplication.translate("MainWindow", u"\u96fb\u5b50\u4fe1\u7bb1", None))
        self.label.setText("")
        self.label_14.setText("")
        self.pushButton_personal_id.setText(QCoreApplication.translate("MainWindow", u"\u8eab\u5206\u8b49\u5b57\u865f", None))
        self.pushButton_personal_name.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.lineEdit_personal_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u96fb\u5b50\u4fe1\u7bb1(\u5fc5\u586b)", None))
        self.lineEdit_personal_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u8eab\u5206\u8b49\u5b57\u865f(\u5fc5\u586b)", None))
        self.lineEdit_personal_phone.setText("")
        self.lineEdit_personal_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u9023\u7d61\u96fb\u8a71(\u5fc5\u586b)", None))
        self.pushButton_sambo_car_type.setText(QCoreApplication.translate("MainWindow", u"\u8eca\u7a2e", None))
        self.label_8.setText("")
        self.pushButton_sambo_date.setText(QCoreApplication.translate("MainWindow", u"\u9055\u898f\u65e5\u671f", None))
        self.label_5.setText("")
        self.pushButton_sambo_car_id.setText(QCoreApplication.translate("MainWindow", u"\u8eca\u724c\u865f\u78bc", None))
        self.label_9.setText("")
        self.pushButton_sambo_car_town_position.setText(QCoreApplication.translate("MainWindow", u"\u9055\u898f\u5340\u57df", None))
        self.label_13.setText("")
        self.lineEdit_sambo_street_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u500b\u8def\u53e3", None))
        self.lineEdit_sambo_street_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u500b\u8def\u53e3", None))
        self.pushButton_sambo_event_desc.setText(QCoreApplication.translate("MainWindow", u"\u9055\u898f\u60c5\u6cc1", None))
        self.label_6.setText("")
        self.comboBox_sampbo_car_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u666e\u901a\u91cd\u578b\u6a5f\u8eca", None))
        self.comboBox_sampbo_car_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5c0f\u5ba2\u8eca", None))
        self.comboBox_sampbo_car_type.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5c0f\u8ca8\u8eca", None))
        self.comboBox_sampbo_car_type.setItemText(3, QCoreApplication.translate("MainWindow", u"\u806f\u7d50\u8eca", None))
        self.comboBox_sampbo_car_type.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5927\u5ba2\u8eca", None))
        self.comboBox_sampbo_car_type.setItemText(5, QCoreApplication.translate("MainWindow", u"\u8f15\u578b\u6a5f\u8eca", None))
        self.comboBox_sampbo_car_type.setItemText(6, QCoreApplication.translate("MainWindow", u"\u5927\u8ca8\u8eca", None))
        self.comboBox_sampbo_car_type.setItemText(7, QCoreApplication.translate("MainWindow", u"\u5927\u578b\u91cd\u578b\u6a5f\u8eca", None))

        self.comboBox_sampbo_car_type.setCurrentText(QCoreApplication.translate("MainWindow", u"\u666e\u901a\u91cd\u578b\u6a5f\u8eca", None))
        self.comboBox_sampbo_car_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234", None))
        self.pushButton_sambo_car_position.setText(QCoreApplication.translate("MainWindow", u"\u5730\u9ede\u7c21\u6613\u8aaa\u660e", None))
        self.label_10.setText("")
        self.comboBox_sampbo_violate_dest.setItemText(0, QCoreApplication.translate("MainWindow", u"\u95d6\u7d05\u71c8", None))
        self.comboBox_sampbo_violate_dest.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7d05\u71c8\u5de6\u8f49", None))
        self.comboBox_sampbo_violate_dest.setItemText(2, QCoreApplication.translate("MainWindow", u"\u7d05\u71c8\u53f3\u8f49", None))
        self.comboBox_sampbo_violate_dest.setItemText(3, QCoreApplication.translate("MainWindow", u"\u7d05\u7dda\u505c\u8eca", None))
        self.comboBox_sampbo_violate_dest.setItemText(4, QCoreApplication.translate("MainWindow", u"\u672a\u4f9d\u865f\u8a8c\u898f\u5b9a\u884c\u4f7f", None))

        self.comboBox_sampbo_violate_dest.setCurrentText(QCoreApplication.translate("MainWindow", u"\u95d6\u7d05\u71c8", None))
        self.comboBox_sampbo_violate_dest.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hour", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Minute", None))
        self.lineEdit_sambo_violate_town.setText(QCoreApplication.translate("MainWindow", u"\u5357\u6295\u5e02", None))
        self.lineEdit_sambo_car_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u8eca\u724c\u865f\u78bc(\u5fc5\u586b)", None))
        self.pushButton_sambo_car_info.setText(QCoreApplication.translate("MainWindow", u"  \u4e09\u5bf6\u8cc7\u6599", None))
        self.pushButton_sambo_status_2.setText("")
        self.pushButton_personal_info.setText(QCoreApplication.translate("MainWindow", u"  \u500b\u4eba\u8cc7\u6599", None))
        self.pushButton_personal_save.setText("")
        self.pushButton_personal_status.setText("")
        self.pushButton_video_control.setText("")
        self.pushButton_upload.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_sambo_image.setText(QCoreApplication.translate("MainWindow", u"Image/Video Resource", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Resource Name", None))
        self.file_exploer.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Resource Type", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"  \u6279\u91cf\u4e0a\u50b3\u72c0\u614b\u5217\u8868", None))
    # retranslateUi

