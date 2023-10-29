from console_ui import ConsoleUI
from number_of_common_numbers import NumberOfCommonNumbers as Task1
from os import system
from error_output import FormattedOutput as FOutput
from distance_between_points import DistanceBetweenPoints as Task2
from arithmetic_conversion import ArithmeticConversion as Task3


def main():
    """
    Функция старта главного меню.
    """
    while True:
        task_selection_item = ConsoleUI.menu()

        match task_selection_item:
            case 1:
                Task1().ui_for_task()

            case 2:
                Task2().ui_for_task()

            case 3:
                Task3().ui_for_task()

            case 4:
                system('CLS')
                return

            case _:
                FOutput.error_message()


if __name__ == '__main__':
    main()
