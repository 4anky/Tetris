# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tetris(object):
    def setupUi(self, Tetris):
        Tetris.setObjectName("Tetris")
        Tetris.resize(600, 941)
        Tetris.setMinimumSize(QtCore.QSize(600, 941))
        Tetris.setMaximumSize(QtCore.QSize(600, 941))
        self.centralwidget = QtWidgets.QWidget(Tetris)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 900))
        self.centralwidget.setMaximumSize(QtCore.QSize(600, 900))
        self.centralwidget.setObjectName("centralwidget")
        self.view_cup = QtWidgets.QGraphicsView(self.centralwidget)
        self.view_cup.setGeometry(QtCore.QRect(20, 20, 400, 800))
        self.view_cup.setAcceptDrops(True)
        self.view_cup.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view_cup.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view_cup.setObjectName("view_cup")
        self.text_score = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_score.setGeometry(QtCore.QRect(440, 430, 131, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.text_score.setFont(font)
        self.text_score.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_score.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_score.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_score.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.text_score.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.text_score.setObjectName("text_score")
        self.btn_newgame = QtWidgets.QPushButton(self.centralwidget)
        self.btn_newgame.setGeometry(QtCore.QRect(20, 842, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.btn_newgame.setFont(font)
        self.btn_newgame.setObjectName("btn_newgame")
        self.lbl_score = QtWidgets.QLabel(self.centralwidget)
        self.lbl_score.setGeometry(QtCore.QRect(470, 480, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.lbl_score.setFont(font)
        self.lbl_score.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_score.setObjectName("lbl_score")
        Tetris.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tetris)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        Tetris.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tetris)
        self.statusbar.setObjectName("statusbar")
        Tetris.setStatusBar(self.statusbar)

        self.retranslateUi(Tetris)
        QtCore.QMetaObject.connectSlotsByName(Tetris)

    def retranslateUi(self, Tetris):
        _translate = QtCore.QCoreApplication.translate
        Tetris.setWindowTitle(_translate("Tetris", "Tetris"))
        self.btn_newgame.setText(_translate("Tetris", "New Game"))
        self.lbl_score.setText(_translate("Tetris", "Score"))

