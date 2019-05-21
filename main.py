import sys
import random


from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsRectItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

import numpy as np


import gui


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__(parent=None)

        self.ui = gui.Ui_Tetris()
        self.ui.setupUi(self)

        self.x0, self.y0 = 5, 0
        self.size = 40
        self.scene = QGraphicsScene(0, 0, 400, 800)
        self.ui.view_cup.setScene(self.scene)

        self.cup = np.zeros((20, 10), dtype=int)
        self.w = self.cup.shape[1]
        self.h = self.cup.shape[0]
        self.cup[self.y0][self.x0] = random.randint(1, 7)


        self.ui.btn_newgame.clicked.connect(self.game_on)

        self.color = [QColor(255, 255, 255), QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255),
                      QColor(255, 255, 0), QColor(255, 0, 255), QColor(255, 128, 0), QColor(128, 64 ,0),
                      QColor(0, 0, 0)]

    def keyPressEvent(self, event, x0, y0, cup):
        if event.key() == Qt.Key_A and x0:
            x0, y0 = x0 - 1, y0
            cup[y0][x0] = cup[y0][x0 + 1]
            cup[y0][x0 + 1] = 0
            return x0, y0, cup


    def game_on(self):
        self.timer_id = self.startTimer(200, timerType=Qt.PreciseTimer)

    def timerEvent(self, event):
        if self.y0 < 19 and not self.cup[self.y0 + 1][self.x0]:

            self.x0, self.y0 = self.x0, self.y0 + 1
            self.cup[self.y0][self.x0] = self.cup[self.y0 - 1][self.x0]
            self.cup[self.y0 - 1][self.x0] = 0

            self.scene.clear()
            [self.scene.addRect(self.size * i, self.size * j, self.size, self.size,
                            self.color[0], self.color[self.cup[j][i]]) for i in range(self.w) for j in range(self.h)]
        else:
            self.x0, self.y0 = 5, 0
            self.cup[self.y0][self.x0] = random.randint(1, 7)

class Figures():
    def __init__(self):
        pass
    def i_fig(self):
        pass
    def t_fig(self):
        pass
    def z_fig(self):
        pass
    def s_fig(self):
        pass
    def o_fig(self):
        pass
    def l_fig(self):
        pass
    def j_fig(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tetris = Main()
    tetris.show()
    sys.exit(app.exec_())
