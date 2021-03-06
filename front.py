# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 600)
        MainWindow.setMaximumSize(QtCore.QSize(502, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.extract_button = QtWidgets.QPushButton(self.centralwidget)
        self.extract_button.setGeometry(QtCore.QRect(100, 8, 61, 61))
        self.extract_button.setStyleSheet("border-image: url(B:/Python/code/arch_diplom/src/unarchive.png);")
        self.extract_button.setText("")
        self.extract_button.setIconSize(QtCore.QSize(46, 46))
        self.extract_button.setFlat(False)
        self.extract_button.setObjectName("extract_button")
        self.archive_button = QtWidgets.QPushButton(self.centralwidget)
        self.archive_button.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.archive_button.setStyleSheet("border-image: url(B:/Python/code/arch_diplom/src/archive.png);")
        self.archive_button.setText("")
        self.archive_button.setObjectName("archive_button")
        self.name_list = QtWidgets.QListWidget(self.centralwidget)
        self.name_list.setGeometry(QtCore.QRect(0, 140, 171, 441))
        self.name_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name_list.setObjectName("name_list")
        self.size_list = QtWidgets.QListWidget(self.centralwidget)
        self.size_list.setGeometry(QtCore.QRect(170, 140, 81, 431))
        self.size_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.size_list.setObjectName("size_list")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(3, 120, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 120, 47, 16))
        self.label_2.setObjectName("label_2")
        self.extension_list = QtWidgets.QListWidget(self.centralwidget)
        self.extension_list.setGeometry(QtCore.QRect(330, 140, 171, 431))
        self.extension_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extension_list.setObjectName("extension_list")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 120, 61, 16))
        self.label_3.setObjectName("label_3")
        self.compressed_size_list = QtWidgets.QListWidget(self.centralwidget)
        self.compressed_size_list.setGeometry(QtCore.QRect(250, 140, 81, 431))
        self.compressed_size_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.compressed_size_list.setObjectName("compressed_size_list")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 120, 81, 16))
        self.label_4.setObjectName("label_4")
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(430, 20, 71, 51))
        self.help_button.setStyleSheet("border-image: url(B:/Python/code/arch_diplom/src/help.png);")
        self.help_button.setText("")
        self.help_button.setObjectName("help_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 21))
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
        self.label.setText(_translate("MainWindow", "?????? ??????????"))
        self.label_2.setText(_translate("MainWindow", "????????????"))
        self.label_3.setText(_translate("MainWindow", "?????? ??????????"))
        self.label_4.setText(_translate("MainWindow", "???????????? ????????????"))
