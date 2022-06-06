main_push_buttons = """
QPushButton#extract_button:hover {
    background-color: rgb(170, 234, 253);
}
QPushButton#extract_button:pressed {
    background-color: rgb(120, 200, 225);
}
QPushButton#archive_button:hover {
    background-color: rgb(170, 234, 253);
}
QPushButton#archive_button:pressed {
    background-color: rgb(120, 200, 225);
    }
QPushButton#help_button:hover {
    background-color: rgb(170, 234, 253);
}
QPushButton#help_button:pressed {
    background-color: rgb(120, 200, 225);
    }
"""
help_text = """
Эта программа создана для дипломного проекта по теме программное средство архивации данных.
Программа имеет функции архивации файлов и извлечения файлов.
Для сжатия файлов используется алгоритм сжатия Deflate.
Для извлечения поддерживаются форматы архивов zip и rar, есть возможность извлечения архивов, защищенных паролем.
Программа разработана с помощью Qt Designer и языка программирования Python 3.x\n\n
© БГУИР 2022
"""