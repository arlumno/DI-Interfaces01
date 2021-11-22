from pruebasUi import *
import sys
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MeuWindo()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    windows= Main()
    windows.show()
    sys.exit(app.exec())
