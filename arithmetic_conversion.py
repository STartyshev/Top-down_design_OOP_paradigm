from console_ui import ConsoleUI
from correct_initialization import CorrectInitialization as CorrectInit
from error_output import FormattedOutput as FOutput


class ArithmeticConversion:
    """
    Класс для задачи №3.
    """
    the_task = (f"Входные данные: три массива с числами. "
                f"Требуется проверить можно ли получить число из 3-го массива, "
                f"арифметическими преобразованиями с числами из двух других массивов. "
                f"Числа проверяются последовательно.")

    def __init__(self):
        # Массивы с числами
        self.__first_array = []
        self.__second_array = []
        self.__third_array = []
        # Список результатов
        self.__list_of_results = []

    def ui_for_task(self):
        """
        Функция реализующая пользовательский интерфейс в консоли для задачи.
        """
        while True:
            system('CLS')
            main_menu_item = ConsoleUI.main_menu_for_tasks(
                task_name='Логическое следствие элементов трех массивов.'
            )
            match main_menu_item:
                # Условие задачи
                case 1:
                    system('CLS')
                    print(self.the_task)
                    system('PAUSE')

                # Ввод исходных данных
                case 2:
                    # При вводе новых данных все предыдущие обнуляются
                    self.__first_array = []
                    self.__second_array = []
                    self.__third_array = []
                    self.__list_of_results = []
                    system('CLS')
                    while True:
                        initialization_item = ConsoleUI.menu(
                            'Способ инициализации.\n'
                            '1. Вручную.\n'
                            '2. Автоматически.'
                        )
                        match initialization_item:
                            # Инициализация массивов точек вручную
                            case 1:
                                system('CLS')
                                print('Инициализация первого массива: ')
                                CorrectInit.array_init(self.__first_array)
                                print('Инициализация второго массива: ')
                                CorrectInit.array_init(self.__second_array)
                                print('Инициализация третьего массива: ')
                                CorrectInit.array_init(self.__third_array)
                                break

                            # Инициализация массивов точек случайным образом
                            case 2:
                                system('CLS')
                                print('Инициализация первого массива: ')
                                CorrectInit.random_array_init(self.__first_array)
                                print('Инициализация второго массива: ')
                                CorrectInit.random_array_init(self.__second_array)
                                print('Инициализация третьего массива: ')
                                CorrectInit.random_array_init(self.__third_array)
                                break

                            case _:
                                FOutput.error_message('В меню всего 2 пункта. Попробуйте еще раз.')

                    print('Инициализация массивов прошла успешно.')
                    system('PAUSE')

                # Выполнение алгоритма
                case 3:
                    pass

                # Вывод результатов работы алгоритма
                case 4:
                    pass

                # Выход в главное меню
                case 5:
                    break

                case _:
                    FOutput.error_message('В меню всего 5 пунктов. Попробуйте еще раз.')

    def task_algorithm(self):
        """
        Функция реализующая алгоритм задачи
        """
        pass

    def check_arithmetic_operation(self):
        """
        Функция реализующая проверку: можно ли получить число из 3-го массива, заданным арифметическим преобразованием
        с числами 2-ух других массивов. В случае положительного результата добавляет полученый способ в список результатов.
        """
        pass
