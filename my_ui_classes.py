from PyQt5 import QtCore, QtGui, QtWidgets
from src.styles import help_text


class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        label = QtWidgets.QLabel("Выберите:")
        self.rbDir = QtWidgets.QRadioButton('Папку', self)
        self.rbPath = QtWidgets.QRadioButton('Файлы', self)
        btnOk = QtWidgets.QPushButton("Ok", clicked=self.hide)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(label, 0, 0, 1, 3)
        layout.addWidget(self.rbDir, 1, 1, 1, 1)
        layout.addWidget(self.rbPath, 2, 1, 1, 1)
        layout.addWidget(btnOk, 3, 2, 1, 1)


class DialogArchName(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DialogArchName, self).__init__(parent)
        self.namef = ''
        self.pathf = ''
        # +++
        self.close_forcibly = False  # +++
        label = QtWidgets.QLabel("Введите имя архива:")
        self.namefield = QtWidgets.QLineEdit()
        btnchoice = QtWidgets.QPushButton('Выбрать путь', clicked=self.getpath)
        self.rar_arch = QtWidgets.QRadioButton('.rar')
        self.zip_arch = QtWidgets.QRadioButton('.zip')
        btnOk = QtWidgets.QPushButton("Архивировать", clicked=self.getname)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(label, 0, 0, 1, 1)
        layout.addWidget(self.rar_arch, 0, 1, 1, 1)
        layout.addWidget(self.namefield, 1, 0, 1, 1)
        layout.addWidget(self.zip_arch, 1, 1, 1, 1)
        layout.addWidget(btnchoice, 3, 0, 1, 1)  # высота, право
        layout.addWidget(btnOk, 3, 1, 1, 1)

    def closeEvent(self, a0: QtWidgets.QDialog.closeEvent) -> None:
        self.close_forcibly = True

    def getname(self):
        self.namef = self.namefield.text()
        # +++
        self.close_forcibly = False
        self.hide()

    def getpath(self):
        self.pathf = QtWidgets.QFileDialog.getExistingDirectory()


class RequestPasswordDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(RequestPasswordDialog, self).__init__(parent)
        self.password = ''
        layout = QtWidgets.QGridLayout(self)
        label = QtWidgets.QLabel("Введите пароль:")
        self.namefield = QtWidgets.QLineEdit()
        btnOk = QtWidgets.QPushButton("Ок", clicked=self.get_password)
        layout.addWidget(label, 0, 0, 1, 1)
        layout.addWidget(self.namefield, 1, 0, 1, 1)
        layout.addWidget(btnOk, 3, 1, 1, 1)

    def closeEvent(self, a0: QtWidgets.QDialog.closeEvent) -> None:
        self.close_forcibly = True

    def get_password(self):
        self.password = self.namefield.text()
        self.hide()


class HelpDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(HelpDialog, self).__init__(parent)
        layout = QtWidgets.QGridLayout(self)
        text_widget = QtWidgets.QLabel(help_text)
        btnOk = QtWidgets.QPushButton("Ок", clicked=self.hide)
        layout.addWidget(text_widget, 0, 0, 1, 1)
        layout.addWidget(btnOk, 3, 1, 1, 1)

    @staticmethod
    def show_text():
        HelpDialog().exec_()
