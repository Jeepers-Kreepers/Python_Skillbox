from loguru import logger  # Импортируем модуль loguru для более удобного логирования

# Настройка логирования с loguru (выберите либо loguru, либо logging)
logger.add("logs.log", format="{time} {level} {message}", level="ERROR")
# Эта строка настраивает loguru для записи логов уровня ERROR и выше в файл "logs.log".
#  - "logs.log": Имя файла для записи логов.
#  - format="{time} {level} {message}":  Формат записи логов (время, уровень, сообщение).
#  - level="ERROR":  Уровень логирования (регистрируются только ошибки).

add_l = lambda x, y: x + y  # Сложение
subtract_l = lambda x, y: x - y  # Вычитание
multiply_l = lambda x, y: x * y  # Умножение
divide_l = lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(ZeroDivisionError("Деление на ноль!"))  # Деление

operations = {
    "+": add_l,  # Связываем символ "+" с функцией сложения add_l
    "*": multiply_l,  # Связываем символ "×" с функцией умножения multiply_l
    "−": subtract_l,  # Связываем символ "−" с функцией вычитания subtract_l
    "/": divide_l,  # Связываем символ "/" с функцией деления divide_l
}
#  Словарь, который сопоставляет символы операций с соответствующими функциями.
#  Это позволяет вызывать функции по их строковым представлениям.

def calculate(expression: str, line_number: int, error_list: list):
    """Вычисляет выражение. Возвращает результат или None в случае ошибки."""
    try:  # Начинаем блок try...except для обработки возможных исключений

        expression = expression.strip()  # Удаляем пробелы в начале и конце строки
        parts = []  # Создаем пустой список для хранения операндов (чисел)
        current_number = ""  # Создаем пустую строку для построения числа
        operator = None  # Инициализируем переменную operator значением None (оператор пока не найден)

        for char in expression:  # Перебираем каждый символ в выражении
            if char.isdigit() or char == '.' or (
                    char == '-' and not parts):  # Если символ - цифра, точка или минус (в начале числа)
                current_number += char  # Добавляем символ к текущему числу

            elif char in operations:  # Если символ - оператор
                if operator:  # Проверяем, не был ли оператор уже найден
                    raise ValueError(
                        "Недопустимый формат выражения: несколько операторов.")  # Если оператор уже был найден, вызываем исключение
                if current_number:  # Если текущее число не пустое
                    parts.append(current_number)  # Добавляем текущее число в список операндов
                    current_number = ""  # Сбрасываем текущее число
                operator = char  # Запоминаем найденный оператор

            elif char.isspace():  # Если символ - пробел
                if current_number:  # Если текущее число не пустое
                    parts.append(current_number)  # Добавляем текущее число в список операндов
                    current_number = ""  # Сбрасываем текущее число

            else:  # Если символ - что-то другое (не цифра, не точка, не оператор, не пробел)
                raise ValueError(f"Недопустимый символ: {char}")  # Вызываем исключение, указывая недопустимый символ

        if current_number:  # Если после обработки всех символов осталось текущее число
            parts.append(current_number)  # Добавляем его в список операндов

        if len(expression) == 0:  # Если количество операндов не равно 2 или оператор не найден
            raise ValueError("Пустая строка.")  # Вызываем исключение

        if len(parts) != 2 or operator is None:  # Если количество операндов не равно 2 или оператор не найден
            raise ValueError("Неверное количество операндов или отсутствует оператор.")  # Вызываем исключение

        num1 = float(parts[0])  # Преобразуем первый операнд в число с плавающей точкой
        num2 = float(parts[1])  # Преобразуем второй операнд в число с плавающей точкой

        # Вызываем соответствующую функцию операции на основе найденного оператора
        result = operations[operator](num1, num2)
        return result  # Возвращаем результат вычисления


    except (ValueError, ZeroDivisionError, Exception) as e:
        error_messages = {
            ValueError: f"Строка {line_number}: Ошибка значения: {e}",
            ZeroDivisionError: f"Строка {line_number}: Ошибка деления на ноль: {e}",
            Exception: f"Строка {line_number}: Непредвиденная ошибка: {e}"
        }
        # Сообщение об ошибке на основе ключа:типа исключения
        error_message = error_messages[type(e)]
        log_and_append_error(error_message, error_list)
        return


def log_and_append_error(error_message, error_list):
    logger.error(error_message)  # Записываем сообщение об ошибке в лог
    error_list.append(error_message)  # Добавляем сообщение об ошибке в список ошибок
    # print(error_message)  # Выводим сообщение об ошибке в консоль


def process_expressions(filename):
    """Обрабатывает выражения из файла."""
    errors = []  # Создаем пустой список для хранения сообщений об ошибках
    # print(id(errors))
    results = []  # Создаем пустой список для хранения результатов

    try:  # Начинаем блок try...except для обработки FileNotFoundError
        with open(filename, "r") as f:  # Открываем файл для чтения
            lines = f.readlines()  # Читаем все строки из файла в список lines
    except FileNotFoundError:  # Обрабатываем исключение FileNotFoundError, если файл не найден
        print(f"Файл '{filename}' не найден.")  # Выводим сообщение об ошибке
        return  # Завершаем функцию

    for i, line in enumerate(lines):  # Перебираем строки файла вместе с их номерами (начиная с 0)
        line = line.strip()  # Удаляем пробелы в начале и конце строки
        #if not line:  # Если строка пустая
            #continue  # Переходим к следующей строке


        result = calculate(line, i + 1, errors)  # Вызываем функцию calculate для вычисления выражения в строке
        #  - line:  Сама строка выражения.
        #  - i + 1:  Номер строки (начинается с 1, а не с 0).
        #  - errors:  Список, в который будут добавлены сообщения об ошибках, если они возникнут.

        if result:  # Если вычисление прошло успешно (result не None)
            with open("results.txt", "a") as f:  # Открываем файл "results.txt" для добавления
                f.write(f" {i + 1}: {result}\n")  # Записываем результат в файл, добавляя символ новой строки
            result_message = f"Строка {i + 1}: Результат: {result}"  # Формируем сообщение с результатом
            print(result_message)  # Выводим сообщение с результатом в консоль
            results.append(result_message)  # Добавляем сообщение с результатом в список результатов

    # Запись ошибок в файл errors.txt
    if errors:  # Если список ошибок не пустой
        with open("errors.txt", "w") as f:  # Открываем файл "errors.txt" для записи
            for error in errors:  # Перебираем сообщения об ошибках в списке errors
                f.write(error + "\n")  # Записываем сообщение об ошибке в файл, добавляя символ новой строки

    return


# Пример использования
if __name__ == "__main__":
    # Код внутри этой конструкции выполняется только при непосредственном запуске скрипта.
    # Создаем файл exprs.txt с примерами выражений (или убеждаемся, что он существует)
    with open("exprs.txt", "w") as f:  # Открываем файл "exprs.txt" для записи (если его нет, он будет создан)
        f.write("2 + 3\n")  # Записываем примеры выражений в файл, каждое на новой строке
        f.write("-2−3\n")
        f.write("-5,2  *4\n")
        f.write("-5.2*4\n")
        f.write("\n")
        f.write("a+5\n")
        #f.write("5 + abc\n")  # Неверный ввод (будет ошибка)
        #f.write("10 / 0\n")  # Деление на ноль (будет ошибка)
        #f.write("  12.5   +   7.5  \n")  # Пробелы (пробелы должны обрабатываться)
        #f.write("  2  *  3 \n")  # умножение с пробелами
        #f.write("9 − 1\n")
        #f.write("10 % 2\n")  # Недопустимая операция (будет ошибка)
        #f.write("-5 + 3\n")  # Отрицательное число

    process_expressions(
        "exprs.txt")  # Вызываем функцию process_expressions для обработки выражений из файла "exprs.txt"
