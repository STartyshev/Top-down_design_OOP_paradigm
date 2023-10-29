from console_ui import ConsoleUI
from error_output import FormattedOutput as FOutput


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
                    pass

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
        Алгоритм решения задачи.
        """
        pass
