import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Git и случайные окружности')
        self.do_paint = False
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Кнопка')
        self.pushButton.move(200, 450)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_smile(qp)
            qp.end()

    def draw_smile(self, qp):
        for _ in range(5):
            qp.setBrush(QColor(random.randint(0, 255),
                               random.randint(0, 255),
                               random.randint(0, 255)))
            qp.drawEllipse(*(random.randint(0, 500),
                             random.randint(0, 500)),
                           *(random.randint(2, 100),
                             random.randint(2, 100)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())