from console_ui import ConsoleUI
from correct_initialization import CorrectInitialization as CorrectInit
from error_output import FormattedOutput as FOutput


class DistanceBetweenPoints:
    """
    Класс для задачи №2.
    """
    the_task = (f"Входные данные: два массива с точками и число. "
                f"Требуется вывести точки из первого и второго массивов, "
                f"расстояния между которыми больше заданного числа. "
                f"Расстояния считаются только для соответствующих чисел.")

    def __init__(self):
        # Массивы с точками
        self.__first_array_of_dots = []
        self.__second_array_of_dots = []
        # Словарь в котором ключи - длины отрезков значения, которых больше заданного числа,
        # а значения - пары точек, которые эти отрезки образуют
        self.__dict_of_segments_and_points = dict()
        # Заданное число с которым нужно сравнивать длину отрезков
        self.__max_length = None
        # Флаг состояния
        self.__algorithm_completed = False

    def ui_for_task(self):
        """
        Функция реализующая пользовательский интерфейс в консоли для задачи.
        """
        while True:
            system('CLS')
            main_menu_item = ConsoleUI.main_menu_for_tasks(
                task_name='Расстояние между точками.'
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
                    self.__first_array_of_dots = []
                    self.__second_array_of_dots = []
                    self.__dict_of_segments_and_points = dict()
                    self.__algorithm_completed = False
                    system('CLS')
                    max_length = CorrectInit.input_num(
                        left_value=1,
                        right_value=float('inf'),
                        input_message='Введите значение с которым нужно сравнивать длины отрезков: ',
                        error_message='Значение должно быть положительное. Попробуйте еще раз.',
                        type_of_number=float
                    )
                    while True:
                        system('CLS')
                        initialization_item = ConsoleUI.menu(
                            'Способ инициализации массивов точек.\n'
                            '1. Вручную.\n'
                            '2. Автоматически.'
                        )
                        match initialization_item:
                            # Инициализация массивов точек вручную
                            case 1:
                                system('CLS')
                                print('Инициализация первого массива: ')
                                CorrectInit.array_of_dots_init()
                                print('Инициализация второго массива: ')
                                CorrectInit.array_of_dots_init()
                                break

                            # Инициализация массивов точек случайным образом
                            case 2:
                                system('CLS')
                                print('В каком пространстве будут находиться точки?\n'
                                      '1. На прямой.\n'
                                      '2. На плоскости.\n'
                                      '3. В трехмерном пространстве.')

                                space_selection = CorrectInit.input_num(
                                    left_value=-float('inf'),
                                    right_value=float('inf'),
                                    input_message='Выберите пункт меню: ',
                                    error_message='В меню всего 3 пункта. Попробуйте еще раз.',
                                    type_of_number=int
                                )
                                print('Инициализация первого массива: ')
                                CorrectInit.auto_array_of_dots_init()
                                print('Инициализация второго массива: ')
                                CorrectInit.auto_array_of_dots_init()
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
        Функция реализующая алгоритм решения задачи.
        """
        pass

    def segment_length(self):
        """
        Функция вычисляющая длину отрезка образованного двумя точками.
        """
        pass
