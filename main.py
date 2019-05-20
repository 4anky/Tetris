from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt5.QtGui import QImage, QGraphicsItem
import numpy as np

import gui


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__(parent=None)

        self.ui = gui.Ui_MainWindow
        self.ui.setupUi(self)

        self.color = ['white', 'blue', 'yellow', 'red', 'green', 'pink', 'orange', 'brown']

        self.ui.btn_newgame.clicked.conect(Logic.game)

class Logic():
    def __init__(self):

        self.cellsize = 40

        self.scene = QGraphicsScene(0, 0, 400, 800)
        self.ui.view_cup.setScene(self.scene)

        self.cup = np.zeros((80, 40))

    def game(self):
#        self.moment = QImage.
        pass

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
