from error_output import FormattedOutput as FOutput
import random


class CorrectInitialization:
    """
    Класс реализующий методы корректной инициализации вручную и случайным образом.
    """

    @staticmethod
    def input_num(left_value, right_value, input_message, error_message, type_of_number):
        """
        Функция реализующая ввод пользователем корректного числа входящего в заданный диапазон.
        :param left_value: Левая граница диапазона;
        :param right_value: правая граница диапазона;
        :param input_message: сообщение-приглашение на ввод числа;
        :param error_message: сообщение в случае не корректного ввода;
        :param type_of_number: тип числа, которое нужно вводить пользователю.
        :return: Возвращает корректное число введенное пользователем.
        """
        while True:
            while True:
                try:
                    num = type_of_number(input(input_message))
                    break
                except ValueError:
                    print('Введенное значение должно являться числом! '
                          'Попробуйте еще раз.')

            if num < left_value or num > right_value:
                print(error_message)
            else:
                return num

    @staticmethod
    def array_init(array):
        """
        Функция для инициализации массива числами вручную.
        :param array: Массив для инициализации.
        """
        while True:
            elem_or_exit = input('Введите число, которое хотите добавить в массив (для выхода введите - выход): ')
            if elem_or_exit.upper() == 'ВЫХОД':
                return
            else:
                try:
                    elem_or_exit = float(elem_or_exit)
                    array.append(elem_or_exit)
                except ValueError:
                    FOutput.error_message('Введенное значение не является числом или ключевым словом "выход". '
                                          'Попробуйте еще раз.')

    @staticmethod
    def random_array_init(array):
        """
        Функция для инициализации массива случайными числами.
        :param array: Массив для инициализации.
        """
        n = CorrectInitialization.input_num(
            left_value=1,
            right_value=50,
            input_message='Введите размер массива: ',
            error_message='Размер массива должен принимать целочисленное значение и быть больше нуля '
                          'и меньше или равен 50. Попробуйте еще раз.',
            type_of_number=int
        )

        for i in range(n):
            array.append(round(random.random() * 10 * ((-1) ** random.randint(1, 2)), 1))

    @staticmethod
    def array_of_dots_init():
        """
        Функция для инициализации массива точек вручную.
        """
        pass

    @staticmethod
    def auto_array_of_dots_init():
        """
        Функция для инициализации массива случайными точками.
        """
        pass
