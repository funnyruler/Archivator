import sys
import src.styles
import front
import my_ui_classes
import zipfile
import os
import shutil
import traceback
from pathlib import Path
from unrar import rarfile
from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, front.Ui_MainWindow, my_ui_classes.HelpDialog):
    def __init__(self):
        super().__init__()
        self.wpath = '"C:\\Program Files\\WinRAR\\Rar.exe"'
        self.setupUi(self)
        self.extract_button.clicked.connect(self.browse_arch_for_extraction)
        self.archive_button.clicked.connect(self.browse_arch_for_compression)
        self.help_button.clicked.connect(self.show_text)

    def clearing(self):
        self.name_list.clear()
        self.size_list.clear()
        self.compressed_size_list.clear()
        self.extension_list.clear()

    def browse_arch_for_compression(self):
        self.directory, self.pathFile = '', ''
        self.dialog = my_ui_classes.Dialog()
        self.dialog.exec_()
        self.clearing()
        if self.dialog.rbDir.isChecked():
            self.clearing()
            self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
            if self.directory:
                for file in os.listdir(self.directory):
                    file_name = file.split('.')
                    file_info = os.stat(self.directory+ '/' + file)
                    self.name_list.addItem(file_name[0])
                    self.size_list.addItem(str(file_info.st_size))
                    try:
                        self.extension_list.addItem(f'Файл "{file_name[1].upper()}"')
                    except IndexError:
                        self.extension_list.addItem('Папка')
        elif self.dialog.rbPath.isChecked():
            self.clearing()
            self.pathFile, _ = QtWidgets.QFileDialog.getOpenFileNames(
                self,
                'Open File', './',
            )
            if self.pathFile:
                for i in self.pathFile:
                    file_name = os.path.split(i)[-1].split('.')
                    file_info = os.stat(i)
                    self.name_list.addItem(file_name[0])
                    self.extension_list.addItem(file_name[1])
                    self.size_list.addItem(str(file_info.st_size))
        self.compressing()

    def compressing(self):
        self.arch_dialog = my_ui_classes.DialogArchName()
        dirfiles = []
        if self.pathFile == '':
            if self.directory == '':
                QtWidgets.QMessageBox.information(None, 'Ошибка', 'Выберите папку либо файл')
            else:
                path = Path(self.directory)
                dirfiles = [str(f.absolute()) for f in path.glob("**/*")]
        else:
            pass
        if dirfiles:
            self.arch_dialog.exec_()
            dialogname = self.arch_dialog.namef
            pathname = self.arch_dialog.pathf
            if dialogname:
                if pathname:
                    archive_name = pathname + '/' + dialogname
                else:
                    archive_name = dialogname
            else:
                if pathname:
                    archive_name = pathname + '/' + os.path.split(self.directory)[-1]
                else:
                    archive_name = os.path.split(self.directory)[-1]
            if self.arch_dialog.close_forcibly:
                return
            if self.arch_dialog.zip_arch.isChecked():
                try:
                    shutil.make_archive(archive_name, 'zip', path)
                    QtWidgets.QMessageBox.information(None, 'Успех', 'Архивирование успешно завершено')
                except Exception:
                    print(traceback.format_exc())
                    QtWidgets.QMessageBox.information(None, 'Ошибка', 'Что-то пошло не так')
            elif self.arch_dialog.rar_arch.isChecked():
                os.system(f"{self.wpath} a {archive_name}.rar {path}")
                QtWidgets.QMessageBox.information(None, 'Успех', 'Архивирование успешно завершено')
            else:
                QtWidgets.QMessageBox.information(None, 'Ошибка', 'Выберите тип архива')

        if self.pathFile:
            self.arch_dialog.exec_()
            dialogname = self.arch_dialog.namef
            pathname = self.arch_dialog.pathf
            if dialogname:
                if pathname:
                    archive = zipfile.ZipFile(pathname + '/' + dialogname + '.zip', 'w')
                else:
                    archive = zipfile.ZipFile(dialogname + '.zip', 'w')
            else:
                if pathname:
                    archive = zipfile.ZipFile(pathname + '/' + os.path.split(self.pathFile[0])[-1] + '.zip', 'w')
                else:
                    archive = zipfile.ZipFile(os.path.split(self.pathFile[0])[-1] + '.zip', 'w')
            try:
                if self.arch_dialog.close_forcibly:
                    return
                for i in self.pathFile:
                    if self.arch_dialog.zip_arch.isChecked():
                        try:
                            archive.write(i, arcname=os.path.split(i)[-1], compress_type=zipfile.ZIP_DEFLATED)
                        except Exception:
                            print(traceback.format_exc())
                    elif self.arch_dialog.rar_arch.isChecked():
                        try:
                            os.system(f"{self.wpath} a {dialogname}.rar {os.path.split(i)[-1]}")
                        except Exception:
                            QtWidgets.QMessageBox.information(None, 'Ошибка', 'Что-то пошло не так')
            except Exception:
                QtWidgets.QMessageBox.information(None, 'Ошибка', 'Что-то пошло не так')
            else:
                QtWidgets.QMessageBox.information(None, 'Успех', 'Архивирование успешно завершено')
            archive.close()

    def browse_arch_for_extraction(self):
        self.clearing()
        self.archive = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите архив", filter="Archives (*.zip;*.rar)")
        if self.archive[0] != '':
            self.extension = self.archive[0].split('.')[1]
            if self.extension == 'zip':
                self.zip_arch = zipfile.ZipFile(self.archive[0], 'r')
                for filename in self.zip_arch.namelist():
                    try:
                        file_info = self.zip_arch.getinfo(filename)
                        name_of_file = os.path.split(filename)[-1].split('.')
                        self.name_list.addItem(name_of_file[0])
                        self.compressed_size_list.addItem(str(file_info.compress_size))
                        self.extension_list.addItem(f'Файл "{name_of_file[1].upper()}"')
                        self.size_list.addItem(str(file_info.file_size))
                    except IndexError:
                        break
            elif self.extension == 'rar':
                rar_arch = rarfile.RarFile(self.archive[0], 'r')
                for filename in rar_arch.namelist():
                    file_info = rar_arch.getinfo(filename)
                    name_of_file = os.path.split(filename)[1].split('.')
                    if len(name_of_file) == 1:
                        break
                    self.name_list.addItem(name_of_file[0])
                    self.compressed_size_list.addItem(str(file_info.compress_size))
                    self.extension_list.addItem(f'Файл "{name_of_file[1].upper()}"')
                    self.size_list.addItem(str(file_info.file_size))
            self.extraction()

    def extraction(self):
        if self.archive[0] != '':
            extract_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку для извлечения")
            if extract_path and self.extension == 'zip':
                zip_arch = zipfile.ZipFile(self.archive[0], 'r')
                try:
                    zip_arch.extractall(extract_path)
                except RuntimeError:
                    dialog = my_ui_classes.RequestPasswordDialog()
                    dialog.exec_()
                    if dialog.close_forcibly:
                        return
                    password = bytes(dialog.password, 'utf-8')
                    try:
                        zip_arch.extractall(extract_path, pwd=password)
                        QtWidgets.QMessageBox.information(None, 'Успех', 'Извлечение успешно завершено')
                    except RuntimeError:
                        QtWidgets.QMessageBox.information(None, 'Ошибка', 'Неверный пароль')
                zip_arch.close()
            elif extract_path and self.extension == 'rar':
                rar_arch = rarfile.RarFile(self.archive[0], 'r')
                try:
                    rar_arch.extractall(extract_path)
                except RuntimeError:
                    dialog = my_ui_classes.RequestPasswordDialog()
                    dialog.exec_()
                    if dialog.close_forcibly:
                        return
                    password = dialog.password
                    try:
                        rar_arch.extractall(extract_path, pwd=password)
                        QtWidgets.QMessageBox.information(None, 'Успех', 'Извлечение успешно завершено')
                    except RuntimeError:
                        QtWidgets.QMessageBox.information(None, 'Ошибка', 'Неверный пароль')
        else:
            QtWidgets.QMessageBox.information(None, 'Ошибка', 'Выберите архив')


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(src.styles.main_push_buttons)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
