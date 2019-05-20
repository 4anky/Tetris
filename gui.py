# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 941)
        MainWindow.setMinimumSize(QtCore.QSize(600, 941))
        MainWindow.setMaximumSize(QtCore.QSize(600, 941))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 900))
        self.centralwidget.setMaximumSize(QtCore.QSize(600, 900))
        self.centralwidget.setObjectName("centralwidget")
        self.view_cup = QtWidgets.QGraphicsView(self.centralwidget)
        self.view_cup.setGeometry(QtCore.QRect(20, 30, 400, 800))
        self.view_cup.setObjectName("view_cup")
        self.view_nextitem = QtWidgets.QGraphicsView(self.centralwidget)
        self.view_nextitem.setGeometry(QtCore.QRect(460, 30, 100, 100))
        self.view_nextitem.setObjectName("view_nextitem")
        self.text_score = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_score.setGeometry(QtCore.QRect(460, 430, 100, 50))
        self.text_score.setObjectName("text_score")
        self.btn_newgame = QtWidgets.QPushButton(self.centralwidget)
        self.btn_newgame.setGeometry(QtCore.QRect(20, 842, 541, 51))
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
        self.lbl_score_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_score_2.setGeometry(QtCore.QRect(480, 130, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.lbl_score_2.setFont(font)
        self.lbl_score_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_score_2.setObjectName("lbl_score_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_newgame.setText(_translate("MainWindow", "New Game"))
        self.lbl_score.setText(_translate("MainWindow", "Score"))
        self.lbl_score_2.setText(_translate("MainWindow", "Next"))

