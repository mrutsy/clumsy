# # -*- coding: utf-8 -*-
# import os, sys
# sys.path.insert(0, '/home/mrutsy/Development/work/clumsy')
# sys.path.insert(1, '/home/mrutsy/Development/work/clumsy/venv/lib/python3.10/site-packages')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'configs.settings'
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()


# # -*- coding: utf-8 -*-
# import os, sys
# sys.path.insert(0, '/home/m/mrutsy/zhs/')
# sys.path.insert(1, '/home/m/mrutsy/zhs/venv/lib/python3.11/site-packages')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'configs.settings'
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# -*- coding: utf-8 -*-

# Импортирую библиотеку функций для работы с операционной системой.
# Importing a library of functions to work with the operating system.
import os

# Импортирую библиотеку функций манипуляции путями, создание и удаление папок и файлов.
# I import a library of functions for manipulating paths, creating and deleting folders and files.
import pathlib

# Импортирую библиотеку функций для предоставления доступа к некоторым переменным, используемым или поддерживаемым
# интерпретатором, и к функциям, которые активно взаимодействуют с интерпретатором.
# Importing a library of functions to provide access to some variables used or supported
# by the interpreter, and to functions that actively interact with the interpreter.
import sys

# Устанавливаю переменную с версией Python.
# Setting a variable with the Python version.
PYTHON_VERSION = '3.10'


if __name__ == "__main__":

    path_current_program = os.path.join(
        pathlib.Path(__file__).parent
    )

    path_current_venv = os.path.join(
        pathlib.Path(__file__).parent,
        'venv',
        'lib',
        'python' + PYTHON_VERSION,
        'site-packages'
    )

    # os.system("echo '" + path_current_program + "' >> www.txt")
    # os.system("echo '" + path_current_venv + "' >> www2.txt")

    # Устанавливаю рабочую директорию в корень программы.
    # I install the working directory in the root of the program.
    sys.path.insert(
        # Устанавливаю позицию.
        # Setting the position.
        0,
        # Устанавливаю путь.
        # Setting the path.
        str(os.path.join(
            pathlib.Path(__file__).parent
        )) + "/"
    )

    # Устанавливаю директорию виртуального окружения Python.
    # I'm installing the Python virtual environment directory.
    sys.path.insert(
        # Устанавливаю позицию.
        # Setting the position.
        1,
        # Устанавливаю путь.
        # Setting the path.
        str(os.path.join(
            pathlib.Path(__file__).parent,
            'venv',
            'lib',
            'python' + PYTHON_VERSION,
            'site-packages'
        ))
    )

    # Устанавливаю переменную среды с настройками программы.
    # Setting the environment variable with the program settings.
    os.environ['DJANGO_SETTINGS_MODULE'] = 'configs.settings'

    text_file = open("/home/m/mrutsy/zhs/text.txt", "w")
    text_file.write(str(path_current_venv) + "\n" + str(path_current_program))

    # Импортируем приложение wsgi.
    # Importing the wsgi application.
    from django.core.wsgi import get_wsgi_application

    # Стартуем проект.
    # Starting the project.
    application = get_wsgi_application()
