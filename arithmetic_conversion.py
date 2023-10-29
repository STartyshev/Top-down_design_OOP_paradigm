from console_ui import ConsoleUI
from correct_initialization import CorrectInitialization as CorrectInit
from error_output import FormattedOutput as FOutput
from os import system


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
                    system('CLS')
                    if len(self.__first_array) < 1 or len(self.__second_array) < 1 or len(self.__third_array) < 1:
                        FOutput.error_message(
                            'Невозможно выполнить алгоритм, так как один или несколько массивов пустые. '
                            'Заполните массивы и попробуйте еще раз.'
                        )
                    else:
                        self.__list_of_results = self.task_algorithm()
                        print('Алгоритм успешно выполнен!')
                        system('PAUSE')

                # Вывод результатов работы алгоритма
                case 4:
                    system('CLS')
                    if len(self.__list_of_results) > 0:
                        print(
                            f"Результат работы алгоритма.\n"
                            f"Первый массив чисел: {' '.join(map(str, self.__first_array))}\n"
                            f"Второй массив чисел: {' '.join(map(str, self.__second_array))}\n"
                            f"Третий массив чисел: {' '.join(map(str, self.__third_array))}\n"
                            f"Результат проверки: {' '.join(map(str, self.__list_of_results))}"
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
        Функция реализующая алгоритм задачи
        :return: Список со строками в которых будет содержаться описание результатов проверки
        (можно или нельзя преобразовать).
        """
        list_of_results = ['' for i in range(len(self.__third_array))]
        triples_of_numbers = enumerate(zip(self.__first_array, self.__second_array, self.__third_array))
        for index, triple in triples_of_numbers:
            try:
                # Проверка каждой из 6 арифметических операций
                self.check_arithmetic_operation(
                    index, triple[0], triple[1], triple[2], list_of_results,
                    lambda elem1, elem2: elem1 % elem2, '%'
                )
                self.check_arithmetic_operation(
                    index, triple[0], triple[1], triple[2], list_of_results,
                    lambda elem1, elem2: elem1 / elem2, '/'
                )
                self.check_arithmetic_operation(
                    index, triple[0], triple[1], triple[2], list_of_results,
                    lambda elem1, elem2: elem1 ** elem2, '**'
                )
                self.check_arithmetic_operation(
                    index, triple[0], triple[1], triple[2], list_of_results,
                    lambda elem1, elem2: elem1 * elem2, '*'
                )
                self.check_arithmetic_operation(
                    index, triple[0], triple[1], triple[2], list_of_results,
                    lambda elem1, elem2: elem1 - elem2, '-'
                )
                self.check_arithmetic_operation(
                    index, triple[0], triple[1], triple[2], list_of_results,
                    lambda elem1, elem2: elem1 + elem2, '+'
                )
            except ZeroDivisionError:
                pass

        for i in range(len(list_of_results)):
            if list_of_results[i] == '':
                list_of_results[i] = f"Нет способов получить {i + 1}-й элемент."

        return list_of_results

    def check_arithmetic_operation(self, index, elem1, elem2, elem3, list_of_results, func, function_symbol):
        """
        Функция реализующая проверку: можно ли получить число из 3-го массива, заданным арифметическим преобразованием
        с числами 2-ух других массивов. В случае положительного результата добавляет полученый способ в список результатов.
        :param index: Индекс проверяемого элемента;
        :param elem1: элемент из первого массива;
        :param elem2: элемент из второго массива;
        :param elem3: элемент из третьего массива (проверяемый элемент);
        :param list_of_results: список полученных результатов;
        :param func: функция которая будет применяться к elem1 и elem2 (арифметическая операция);
        :param function_symbol: строковое отображение арифметической операции (значок).
        """
        if func(elem1, elem2) == elem3:
            if list_of_results[index] == '':
                list_of_results[index] = (f"Способы получить {index + 1}-й элемент: "
                                          f"{elem1} {function_symbol} {elem2} = {elem3};")
            else:
                list_of_results[index] += f"\n{elem1} {function_symbol} {elem2} = {elem3};"
        elif func(elem2, elem1) == elem3:
            if list_of_results[index] == '':
                list_of_results[index] = (f"Способы получить {index + 1}-й элемент: "
                                          f"{elem2} {function_symbol} {elem1} = {elem3};")
            else:
                list_of_results[index] += f"\n{elem2} {function_symbol} {elem1} = {elem3};"
