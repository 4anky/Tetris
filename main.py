import sys
import random

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import numpy as np

import gui


class Figures:
    def __init__(self):
        self.point = [5, 1]
        self.color = [QColor(255, 255, 255), QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255),
                      QColor(255, 255, 0), QColor(255, 0, 255), QColor(255, 128, 0), QColor(128, 64, 0)]
        self.vectors = {1: [[0, -1], [0, 1], [0, 2]],
                        2: [[0, -1], [-1, 0], [1, 0]],
                        3: [[0, -1], [0, 1], [1, 1]],
                        4: [[0, -1], [0, 1], [-1, 1]],
                        5: [[0, -1], [1, -1], [-1, 0]],
                        6: [[0, -1], [-1, -1], [1, 0]],
                        7: [[0, -1], [-1, -1], [-1, 0]]}
        self.matrix_turn = np.array(([0, -1], [1, 0]), dtype=int)

    @staticmethod
    def figure(vect, point):
        return vect, \
               point, \
               [point[0] + vect[0][0], point[1] + vect[0][1]], \
               [point[0] + vect[1][0], point[1] + vect[1][1]], \
               [point[0] + vect[2][0], point[1] + vect[2][1]]


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.ui = gui.Ui_Tetris()
        self.ui.setupUi(self)
        self.fig = Figures()

        self.score = 0
        self.matrix = np.array(0)
        self.new_tetramino_flag = True

        self.scene = QGraphicsScene(0, 0, 400, 800)
        self.ui.view_cup.setScene(self.scene)

        self.ui.text_score.setText(str(self.score))
        self.ui.btn_newgame.clicked.connect(self.game_on)

    def cup_set(self, point, num):
        self.matrix[point[1]][point[0]] = num

    def cup_get(self, point):
        return self.matrix[point[1]][point[0]]

    def check_down(self):
        self.down_y = 10 * [-1]
        self.under_down_y = []

        for i in range(1, 5):
            if self.tetramino[i][1] > self.down_y[self.tetramino[i][0]]:
                self.down_y[self.tetramino[i][0]] = self.tetramino[i][1]

        for i in range(10):
            if self.down_y[i] >= 0:
                if self.down_y[i] >= 19:
                    return False
                else:
                    self.under_down_y.append(self.matrix[self.down_y[i] + 1][i])
            else:
                continue

        if not sum(self.under_down_y):
            return True
        else:
            return False

    def check_left(self):
        self.left_x = 20 * [10]
        self.left_left_x = []

        for i in range(1, 5):
            if self.tetramino[i][0] < self.left_x[self.tetramino[i][1]]:
                self.left_x[self.tetramino[i][1]] = self.tetramino[i][0]

        for i in range(20):
            if self.left_x[i] <= 9:
                if self.left_x[i] <= 0:
                    return False
                else:
                    self.left_left_x.append(self.matrix[i][self.left_x[i] - 1])
            else:
                continue

        if not sum(self.left_left_x):
            return True
        else:
            return False

    def check_right(self):
        self.right_x = 20 * [-1]
        self.right_right_x = []

        for i in range(1, 5):
            if self.tetramino[i][0] > self.right_x[self.tetramino[i][1]]:
                self.right_x[self.tetramino[i][1]] = self.tetramino[i][0]

        for i in range(20):
            if self.right_x[i] >= 0:
                if self.right_x[i] >= 9:
                    return False
                else:
                    self.right_right_x.append(self.matrix[i][self.right_x[i] + 1])
            else:
                continue

        if not sum(self.right_right_x):
            return True
        else:
            return False

    def check_turn(self):
        if self.num == 7:
            return False

        self.vect_turn = [np.ndarray.tolist(np.dot(self.fig.matrix_turn, np.array(self.tetramino[0][i]))) for i in
                          range(3)]
        self.tetramino_turn = self.fig.figure(self.vect_turn, self.tetramino[1])

        self.turn_points = []
        for i in self.tetramino_turn[2:5]:
            if i in self.tetramino[2:5]:
                self.turn_points.append(0)
                continue
            if i[0] in range(10) and i[1] in range(20):
                self.turn_points.append(self.cup_get(i))
            else:
                return False

        if not sum(self.turn_points):
            return True
        else:
            return False

    def shift_down(self):
        for i in range(1, 5):
            self.cup_set(self.tetramino[i], 0)
            self.tetramino[i][1] += 1

        for i in range(1, 5):
            self.cup_set(self.tetramino[i], self.num)

    def shift_left(self):
        for i in range(1, 5):
            self.cup_set(self.tetramino[i], 0)
            self.tetramino[i][0] -= 1

        for i in range(1, 5):
            self.cup_set(self.tetramino[i], self.num)

    def shift_right(self):
        for i in range(1, 5):
            self.cup_set(self.tetramino[i], 0)
            self.tetramino[i][0] += 1

        for i in range(1, 5):
            self.cup_set(self.tetramino[i], self.num)

    def turn(self):
        for i in range(1, 5):
            self.cup_set(self.tetramino[i], 0)

        self.tetramino = self.tetramino_turn
        for i in range(1, 5):
            self.cup_set(self.tetramino[i], self.num)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_S and self.check_down():
            self.shift_down()
            self.update_scene()

        if event.key() == Qt.Key_A and self.check_left():
            self.shift_left()
            self.update_scene()

        if event.key() == Qt.Key_D and self.check_right():
            self.shift_right()
            self.update_scene()

        if event.key() == Qt.Key_W and self.check_turn():
            self.turn()
            self.update_scene()

    def update_scene(self):
        self.scene.clear()
        for i in range(10):
            for j in range(20):
                self.scene.addRect(40 * i, 40 * j, 40, 40, self.fig.color[0], self.fig.color[self.matrix[j][i]])

    def score_and_delete_lines(self):
        self.index_full_lines = [i for i in range(20) if not 0 in self.matrix[i]]

        for i in self.index_full_lines:
            self.matrix[i] = np.zeros((1, 10), dtype=int)
            self.matrix[0:i + 1] = np.roll(self.matrix[0:i + 1], 1, axis=0)

        self.score += 100 * 2 ** len(self.index_full_lines) - 100
        self.ui.text_score.setText(str(self.score))

    def game_on(self):
        self.score = 0
        self.ui.text_score.setText(str(0))

        self.matrix = np.zeros((20, 10), dtype=int)
        self.timer_id = self.startTimer(300, timerType=Qt.PreciseTimer)
        self.ui.btn_newgame.setEnabled(False)

    def timerEvent(self, event):
        if self.new_tetramino_flag:
            self.num = random.randint(1, 7)
            self.tetramino = self.fig.figure(self.fig.vectors[self.num], [5, 1])

            if not sum([self.cup_get(self.tetramino[i]) for i in range(1, 5)]):
                [self.cup_set(i, self.num) for i in self.tetramino[1:5]]
                self.update_scene()
                self.new_tetramino_flag = False
            else:
                self.killTimer(self.timer_id)
                self.timer_id = 0
#                print('GAME OVER!!!')
                self.ui.btn_newgame.setEnabled(True)

        if self.check_down():
            self.shift_down()
            self.update_scene()
        else:
            self.new_tetramino_flag = True
            self.score_and_delete_lines()
            self.update_scene()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tetris = Main()
    tetris.show()
    sys.exit(app.exec_())
