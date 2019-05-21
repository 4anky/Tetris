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

        self.point = [5, 0]
        self.size = 40
        self.scene = QGraphicsScene(0, 0, 400, 800)
        self.ui.view_cup.setScene(self.scene)

        self.score = 0
        self.ui.text_score.setText(str(self.score))

        self.vectors = {'I': [[0, 1], [0, 2], [0, 3]],
                        'T': [[-1, 1], [0, 1], [1, 1]],
                        'O': [[-1, 0], [-1, 1], [0, 1]],
                        'Z': [[-1, 0], [0, 1], [1, 1]],
                        'S': [[1, 0], [0, 1], [-1, 1]],
                        'L': [[0, 1], [0, 2], [1, 2]],
                        'J': [[0, 1], [0, 2], [-1, 2]]}

        self.cup = np.zeros((20, 10), dtype=int)
        self.w = self.cup.shape[1]
        self.h = self.cup.shape[0]
        for i in self.fig_choice[str(random.randint(1, 7))]:
            self.cup[i[1]][i[0]]

        self.ui.btn_newgame.clicked.connect(self.game_on)

        self.color = [QColor(255, 255, 255), QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255),
                      QColor(255, 255, 0), QColor(255, 0, 255), QColor(255, 128, 0), QColor(128, 64 ,0),
                      QColor(0, 0, 0)]

        self.fig_choice = {'1': self.i_fig(),
                           '2': self.t_fig(),
                           '3': self.o_fig(),
                           '4': self.z_fig(),
                           '5': self.s_fig(),
                           '6': self.l_fig(),
                           '7': self.j_fig()}

    def i_fig(self):
        self.i_vect = self.vectors['I']
        return [self.point,
                [self.point[0] + self.i_vect[0][0], self.point[1] + self.i_vect[0][1]],
                [self.point[0] + self.i_vect[1][0], self.point[1] + self.i_vect[1][1]],
                [self.point[0] + self.i_vect[2][0], self.point[1] + self.i_vect[2][1]]]

    def t_fig(self):
        self.t_vect = self.vectors['T']
        return [self.point,
                [self.point[0] + self.t_vect[0][0], self.point[1] + self.t_vect[0][1]],
                [self.point[0] + self.t_vect[1][0], self.point[1] + self.t_vect[1][1]],
                [self.point[0] + self.t_vect[2][0], self.point[1] + self.t_vect[2][1]]]

    def o_fig(self):
        self.o_vect = self.vectors['O']
        return [self.point,
                [self.point[0] + self.o_vect[0][0], self.point[1] + self.o_vect[0][1]],
                [self.point[0] + self.o_vect[1][0], self.point[1] + self.o_vect[1][1]],
                [self.point[0] + self.o_vect[2][0], self.point[1] + self.o_vect[2][1]]]

    def z_fig(self):
        self.z_vect = self.vectors['Z']
        return [self.point,
                [self.point[0] + self.z_vect[0][0], self.point[1] + self.z_vect[0][1]],
                [self.point[0] + self.z_vect[1][0], self.point[1] + self.z_vect[1][1]],
                [self.point[0] + self.z_vect[2][0], self.point[1] + self.z_vect[2][1]]]

    def s_fig(self):
        self.s_vect = self.vectors['S']
        return [self.point,
                [self.point[0] + self.s_vect[0][0], self.point[1] + self.s_vect[0][1]],
                [self.point[0] + self.s_vect[1][0], self.point[1] + self.s_vect[1][1]],
                [self.point[0] + self.s_vect[2][0], self.point[1] + self.s_vect[2][1]]]

    def l_fig(self):
        self.l_vect = self.vectors['L']
        return [self.point,
                [self.point[0] + self.l_vect[0][0], self.point[1] + self.l_vect[0][1]],
                [self.point[0] + self.l_vect[1][0], self.point[1] + self.l_vect[1][1]],
                [self.point[0] + self.l_vect[2][0], self.point[1] + self.l_vect[2][1]]]

    def j_fig(self):
        self.j_vect = self.vectors['J']
        return [self.point,
                [self.point[0] + self.s_vect[0][0], self.point[1] + self.s_vect[0][1]],
                [self.point[0] + self.s_vect[1][0], self.point[1] + self.s_vect[1][1]],
                [self.point[0] + self.s_vect[2][0], self.point[1] + self.s_vect[2][1]]]



    def update_scene(self):
        self.scene.clear()
        [self.scene.addRect(self.size * i, self.size * j, self.size, self.size,
                            self.color[0], self.color[self.cup[j][i]]) for i in range(self.w) for j in range(self.h)]

    def shift_left(self):
        self.point = [self.point[0] - 1, self.point[1]]
        self.cup[self.point[1]][self.point[0]] = self.cup[self.point[1]][self.point[0] + 1]
        self.cup[self.point[1]][self.point[0] + 1] = 0
        self.update_scene()

    def shift_right(self):
        self.point = [self.point[0] + 1, self.point[1]]
        self.cup[self.point[1]][self.point[0]] = self.cup[self.point[1]][self.point[0] - 1]
        self.cup[self.point[1]][self.point[0] - 1] = 0
        self.update_scene()

    def shift_down(self):
        self.point = [self.point[0], self.point[1] + 1]
        self.cup[self.point[1]][self.point[0]] = self.cup[self.point[1] - 1][self.point[0]]
        self.cup[self.point[1] - 1][self.point[0]] = 0
        self.update_scene()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A and self.point[0] and not self.cup[self.point[1]][self.point[0] - 1]:
            self.shift_left()

        if event.key() == Qt.Key_D and self.point[0] < 9 and not self.cup[self.point[1]][self.point[0] + 1]:
            self.shift_right()

        if event.key() == Qt.Key_S and self.point[1] < 19 and not self.cup[self.point[1] + 1][self.point[0]]:
            self.shift_down()

    def game_on(self):
        self.timer_id = self.startTimer(200, timerType=Qt.PreciseTimer)

    def timerEvent(self, event):
        if 0 in [self.point[1] < 19 and not self.cup[self.point[1] + 1][self.point[0]]]:
            self.shift_down()
        else:
            for i in range(len(self.cup)):
                if not (0 in self.cup[i]):
                    self.cup[i] = np.zeros((1, 10), dtype=int)
                    self.cup = np.roll(self.cup, 1, axis=0)
                    self.score += 100
                    self.ui.text_score.setText(str(self.score))

            self.point = [5, 0]
            self.cup[self.point[1]][self.point[0]] = random.randint(1, 7)
            self.update_scene()

class Figures():
    def __init__(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tetris = Main()
    tetris.show()
    sys.exit(app.exec_())
