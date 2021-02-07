import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.dialog = uic.loadUi('dialog.ui')
        self.pushButton.clicked.connect(self.run)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки',
                                                    'молотый/в зернах', 'описание вкуса',
                                                    'цена', 'объем упаковки'])
        self.dialog.pushButton.clicked.connect(self.do)
        self.changed()

    def changed(self):
        with sqlite3.connect('coffee.sqlite') as con:
            cur = con.cursor()
            result = cur.execute(f"""
            select * from coffee
            """).fetchall()
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def run(self):
        self.dialog.show()

    def do(self):
        if self.dialog.lineEdit.text() == ''\
                or self.dialog.lineEdit_2.text() == ''\
                or self.dialog.lineEdit_3.text() == '' \
                or self.dialog.lineEdit_4.text() == '' \
                or self.dialog.lineEdit_5.text() == '' \
                or self.dialog.lineEdit_6.text() == ''\
                or self.dialog.lineEdit_7.text() == '':
            self.dialog.label_5.setText('Неверно заполнена форма')
        else:
            with sqlite3.connect('coffee.sqlite') as con:
                cur = con.cursor()
                result = cur.execute(f"""
                            INSERT INTO coffee (id, name, roast, grind, taste, cost, amount) VALUES (
'{int(self.dialog.lineEdit_7.text())}',
'{self.dialog.lineEdit.text()}',
'{self.dialog.lineEdit_2.text()}',
'{self.dialog.lineEdit_3.text()}',
'{self.dialog.lineEdit_4.text()}',
'{self.dialog.lineEdit_5.text()}',
'{self.dialog.lineEdit_6.text()}')""").fetchall()

            self.dialog.lineEdit.setText('')
            self.dialog.lineEdit_2.setText('')
            self.dialog.lineEdit_3.setText('')
            self.dialog.lineEdit_4.setText('')
            self.dialog.lineEdit_5.setText('')
            self.dialog.lineEdit_6.setText('')
            self.dialog.lineEdit_7.setText('')
            self.dialog.label_5.setText('')
            self.changed()
            self.dialog.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
