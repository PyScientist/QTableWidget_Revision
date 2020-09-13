from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from Ui_mainwindow import Ui_Dialog
import sys


class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.push_button_clicked)
        self.pushButton_2.clicked.connect(self.push_button_2_clicked)
        self.pushButton_3.clicked.connect(self.push_button_3_clicked)

    def push_button_clicked(self):
        print(self.textEdit.toPlainText())
        print(self.tableWidget.item(0,0))
        self.tableWidget.setItem(0,0,QTableWidgetItem('item1'))

    def push_button_2_clicked(self):
        print('button two pressed')
        self.tableWidget.item(0, 0).setText(self.textEdit.toPlainText())

    def push_button_3_clicked(self):
        print('button three pressed')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwidow = MainWindow()
    mainwidow.show()
    sys.exit(app.exec_())