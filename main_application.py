from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from PyQt5.QtCore import Qt
from Ui_mainwindow import Ui_Dialog
import sys

def adjust_table(col_names, rows, table):
    table.setRowCount(rows)
    table.setColumnCount(len(col_names))
    table.setHorizontalHeaderLabels(col_names)

    for row in range(rows):
        for column in range(len(col_names)):
            item = QTableWidgetItem('')
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            table.setItem(row, column, item)

def insert_row_in_the_end_of_table(table):
    row_index_to_isert = table.rowCount()+1
    table.setRowCount(row_index_to_isert)

    for column in range(table.columnCount()):
        item = QTableWidgetItem('')
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        table.setItem(row_index_to_isert-1, column, item)



class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        col_names = ['id', 'name', 'surname', 'patronymics', 'age', 'department']
        adjust_table(col_names, 5, self.tableWidget)

        self.pushButton.clicked.connect(self.push_button_clicked)
        self.pushButton_2.clicked.connect(self.push_button_2_clicked)
        self.pushButton_3.clicked.connect(self.push_button_3_clicked)

    def push_button_clicked(self):
        selected_index = self.tableWidget.selectedItems()
        if len(selected_index) == 1:
            text_to_place_in_item = self.textEdit.toPlainText()
            selected_index[0].setText(text_to_place_in_item)

    def push_button_2_clicked(self):
        insert_row_in_the_end_of_table(self.tableWidget)

    def push_button_3_clicked(self):
        current_row = self.tableWidget.currentRow()
        if current_row >= 0:
            self.tableWidget.removeRow(current_row)
        if current_row == -1:
            self.textEdit.setText('Выберете хотябы одну ячейку')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwidow = MainWindow()
    mainwidow.show()
    sys.exit(app.exec_())