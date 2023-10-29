from console_ui import ConsoleUI
from error_output import FormattedOutput as FOutput
from correct_initialization import CorrectInitialization as CorrectInit
from os import system


class NumberOfCommonNumbers:
    """
    Класс для задачи №1.
    """
    the_task = (f"Входные данные: два массива с числами. Требуется проверить сколько у массивов общих чисел. "
                f"Также число будет считаться общим если оно входит в один массив, а в другом массиве находится "
                f"его перевернутая версия.")

    def __init__(self):
        # Два массива в которых будет осуществляться поиск общих чисел
        self.__first_array = []
        self.__second_array = []
        # Количество общих чисел двух массивов
        self.__num_of_common_numbers = None

    def ui_for_task(self):
        """
        Функция реализующая пользовательский интерфейс в консоли для задачи.
        """
        while True:
            system('CLS')
            main_menu_item = ConsoleUI.main_menu_for_tasks(
                task_name='Проверка двух массивов на количество общих чисел.'
            )

            match main_menu_item:
                # Условие задачи
                case 1:
                    system('CLS')
                    print(NumberOfCommonNumbers.the_task)
                    system('PAUSE')

                # Ввод исходных данных
                case 2:
                    self.__first_array = []
                    self.__second_array = []
                    system('CLS')
                    while True:
                        initialization_item = ConsoleUI.menu(
                            'Способ инициализации.\n'
                            '1. Вручную.\n'
                            '2. Автоматически.'
                        )
                        match initialization_item:
                            # Инициализация массивов вручную
                            case 1:
                                system('CLS')
                                print('Инициализация первого массива: ')
                                CorrectInit.array_init(self.__first_array)
                                print('Инициализация второго массива: ')
                                CorrectInit.array_init(self.__second_array)
                                break

                            # Инициализация массивов случайным образом
                            case 2:
                                system('CLS')
                                print('Инициализация первого массива: ')
                                CorrectInit.random_array_init(self.__first_array)
                                print('Инициализация второго массива: ')
                                CorrectInit.random_array_init(self.__second_array)
                                break

                            case _:
                                FOutput.error_message('В меню всего 2 пункта. Попробуйте еще раз.')

                    print('Инициализация массивов прошла успешно.')
                    system('PAUSE')

                # Выполнение алгоритма
                case 3:
                    system('CLS')
                    if len(self.__first_array) < 1 or len(self.__second_array) < 1:
                        FOutput.error_message(
                            'Невозможно выполнить алгоритм, так как один или оба массива пустые. '
                            'Заполните массивы и попробуйте еще раз.'
                        )
                    else:
                        self.__num_of_common_numbers = self.task_algorithm()
                        print('Алгоритм успешно выполнен!')
                        system('PAUSE')

                # Вывод результатов работы алгоритма
                case 4:
                    system('CLS')
                    if self.__num_of_common_numbers is not None:
                        print(
                            f"Результат работы алгоритма.\n"
                            f"Первый массива: {' '.join(map(str, self.__first_array))}\n"
                            f"Второй массив: {' '.join(map(str, self.__second_array))}\n"
                            f"Количество общих чисел в обоих массивах: {self.__num_of_common_numbers}"
                        )
                        system('PAUSE')
                    else:
                        FOutput.error_message(
                            'Невозможно вывести результат работы алгоритма, так как алгоритм не был выполнен. '
                            'Запустите работу алгоритма и попробуйте еще раз.'
                        )

                # Выход в главное меню
                case 5:
                    break

                case _:
                    FOutput.error_message('В меню всего 5 пунктов. Попробуйте еще раз.')

    def task_algorithm(self):
        """
        Алгоритм решения задачи.
        :return: Возвращает количество общих чисел двух массивов.
        """
        # Список в который будут добавляться общие числа
        list_of_common_numbers = []
        for elem in self.__first_array:
            # Если число из первого массива или его обратная версия находятся во втором массиве
            # И это число еще не обрабатывалось прежде т. е. его нет в списке общих чисел
            # То оно добавляется в список
            if ((str(elem) in list(map(str, self.__second_array)) or str(elem)[::-1] in
                 list(map(str, self.__second_array))) and elem not in list_of_common_numbers):
                list_of_common_numbers.append(elem)
        return len(list_of_common_numbers)
