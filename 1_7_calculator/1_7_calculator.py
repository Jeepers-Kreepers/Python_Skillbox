import re
import ast

def calculate_expression(expression):
    """
    Вычисляет математическое выражение.
    Args:
        expression: Строка, содержащая выражение.
    Returns:
        Результат вычисления (число) или None, если произошла ошибка.
    """
    try:
        # Заменяем символы операций на корректные для Python
        expression = expression.replace('×', '*').replace('−', '-')
        # Удаляем лишние пробелы
        expression = re.sub(r'\s+', '', expression)  # Удаляем все пробельные символы
        # result:tuple = ast.literal_eval(expression)
        result: tuple = eval(expression)
        return result
    except Exception as e:
        return None, str(e)

def read_expressions_from_file(filename):
    """
    Читает выражения из файла и возвращает независимо он наличия ошибок.
    Args:       filename: Имя файла с выражениями.
    Returns:    Список выражений.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            expressions = [line.strip() for line in f]
        return expressions
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        return None

def write_results_to_file(filename, results:list):
    """
    Записывает результаты вычислений в файл.
    Args:
        filename: Имя файла для записи результатов.
        results: Список кортежей (номер строки, результат).
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for line_number, result in results:
                f.write(f"{line_number} {result}\n")
    except Exception as e:
        print(f"Ошибка при записи в файл {filename}: {e}")

def write_errors_to_file(filename, errors:list):
    """
    Записывает информацию об ошибках в файл.
    Args:
        filename: Имя файла для записи ошибок.
        errors: Список кортежей (номер строки, сообщение об ошибке).
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for line_number, error_message in errors:
                f.write(f"{line_number} {error_message}\n")
    except Exception as e:
        print(f"Ошибка при записи в файл {filename}: {e}")

def main():
    """
    Основная функция программы.
    """
    input_filename = input("Укажите имя файла с выражениями: ")
    expressions = read_expressions_from_file(input_filename)

    if expressions is None:
        return

    results = []
    errors = []

    for i, expression in enumerate(expressions):
        result = calculate_expression(expression)
        if result is not None and not isinstance(result, tuple):
            results.append((i + 1, result))
        else:
            errors.append((i + 1, result[1]))

    write_results_to_file("results.txt", results)
    write_errors_to_file("errors.txt", errors)

    print("Результаты вычислений записаны в файл results.txt")
    if errors:
        print("Ошибки при вычислениях записаны в файл errors.txt")
        print(f"Всего ошибок: {len(errors)}")

if __name__ == "__main__":
    main()