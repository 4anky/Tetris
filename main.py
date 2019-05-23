import sys
import random


from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import numpy as np


import gui


class Figures:
    def __init__(self):
        self.point = [5, 0]
        self.color = [QColor(255, 255, 255), QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255),
                      QColor(255, 255, 0), QColor(255, 0, 255), QColor(255, 128, 0), QColor(128, 64, 0),
                      QColor(0, 0, 0)]
        self.vectors_collection = {1: [[0, 1], [0, 2], [0, 3]],
                                   2: [[-1, 1], [0, 1], [1, 1]],
                                   3: [[-1, 0], [-1, 1], [0, 1]],
                                   4: [[-1, 0], [0, 1], [1, 1]],
                                   5: [[1, 0], [0, 1], [-1, 1]],
                                   6: [[0, 1], [0, 2], [1, 2]],
                                   7: [[0, 1], [0, 2], [-1, 2]]}

    @staticmethod
    def fig(vect, point):
        return vect,\
               point,\
               [point[0] + vect[0][0], point[1] + vect[0][1]], \
               [point[0] + vect[1][0], point[1] + vect[1][1]], \
               [point[0] + vect[2][0], point[1] + vect[2][1]]

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__(parent=None)

        self.ui = gui.Ui_Tetris()
        self.ui.setupUi(self)
        self.figures = Figures()

        self.size = 40
        self.score = 0
        self.scene = QGraphicsScene(0, 0, 400, 800)
        self.ui.view_cup.setScene(self.scene)

        self.cup = np.zeros((20, 10), dtype=int)

        self.num = random.randint(1, 7)
        self.tetramino = self.figures.fig(self.figures.vectors_collection[self.num], self.figures.point)
        for i in self.tetramino[1:5]:
            self.cup[i[1]][i[0]] = self.num

        self.ui.text_score.setText(str(self.score))
        self.ui.btn_newgame.clicked.connect(self.game_on)

    def check_down(self):
        self.set_of_down_y = {}
        for i in self.tetramino[1:5]:
            if not (self.set_of_down_y.get(i[0])) or self.set_of_down_y[i[0]] < i[1]:
                self.set_of_down_y[i[0]] = i[1]
        if 19 in self.set_of_down_y.values():
            return False
        self.res = []
        [self.res.append(self.cup[self.set_of_down_y[i] + 1][i]) for i in self.set_of_down_y.keys()]
        if not sum(self.res):
            return True
        else:
            return False

    def check_left(self):
        pass

    def check_right(self):
        pass

    def update_scene(self):
        self.scene.clear()
        [self.scene.addRect(self.size * i, self.size * j, self.size, self.size,
                            self.figures.color[0], self.figures.color[self.cup[j][i]]) for i in range(self.cup.shape[1]) for j in range(self.cup.shape[0])]

    def score_and_delete_line(self):
        for i in range(len(self.cup)):
            if not (0 in self.cup[i]):
                self.cup[i] = np.zeros((1, 10), dtype=int)
                self.cup = np.roll(self.cup, 1, axis=0)
                self.score += 100
                self.ui.text_score.setText(str(self.score))

    def shift_left(self):
        self.update_scene()

    def shift_right(self):
        self.update_scene()

    def shift_down(self):
            for i in self.tetramino[2:5]:
                self.cup[i[1]][i[0]] = 0

            self.tetramino[1][1] += 1
            self.cup[self.tetramino[1][1]][self.tetramino[1][0]] = self.cup[self.tetramino[1][1] - 1][self.tetramino[1][0]]
            self.cup[self.tetramino[1][1] - 1][self.tetramino[1][0]] = 0

            self.tetramino = self.figures.fig(self.figures.vectors_collection[self.num], self.tetramino[1])
            self.cup[self.tetramino[2][1]][self.tetramino[2][0]] = self.num
            self.cup[self.tetramino[3][1]][self.tetramino[3][0]] = self.num
            self.cup[self.tetramino[4][1]][self.tetramino[4][0]] = self.num

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
        if self.check_down():
            self.shift_down()
        else:
            self.score_and_delete_line()
            self.update_scene()

            self.num = random.randint(1, 7)
            self.tetramino = self.figures.fig(self.figures.vectors_collection[self.num], self.figures.point)

            for i in self.tetramino[1:5]:
                self.cup[i[1]][i[0]] = self.num
            self.update_scene()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tetris = Main()
    tetris.show()
    sys.exit(app.exec_())
