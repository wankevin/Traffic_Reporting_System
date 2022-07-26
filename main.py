import sys
from PySide2.QtWidgets import QApplication

from function.ui_template import TrafficReport


class Main(object):
    def __init__(self):
        super(Main, self).__init__()

        # start ui
        app = QApplication(sys.argv)
        window = TrafficReport()
        window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    Main()
