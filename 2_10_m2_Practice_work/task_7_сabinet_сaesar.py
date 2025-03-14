def caesar_cipher(text, shift):
    """
    Шифрует и расшифровывает текст с помощью шифра Цезаря, поддерживая русский алфавит.

    Args:
        text (str): Текст для шифрования/расшифровки.
        shift (int): Величина сдвига (может быть отрицательной).

    Returns:
        tuple: Кортеж из двух строк: зашифрованный текст и расшифрованный текст.
    """
    encrypted_text = ""
    decrypted_text = ""

    for char in text:
        if 'а' <= char <= 'я':  # Обрабатываем строчные русские буквы
            encrypted_char = chr(((ord(char) - ord('а') + shift) % 33) + ord('а'))
            decrypted_char = chr(((ord(encrypted_char) - ord('а') - shift) % 33) + ord('а'))

        elif 'А' <= char <= 'Я':  # Обрабатываем заглавные русские буквы
            encrypted_char = chr(((ord(char) - ord('А') + shift) % 33) + ord('А'))
            decrypted_char = chr(((ord(encrypted_char) - ord('А') - shift) % 33) + ord('А'))

        elif 'a' <= char <= 'z':  # Обрабатываем строчные английские буквы
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            decrypted_char = chr(((ord(encrypted_char) - ord('a') - shift) % 26) + ord('a'))

        elif 'A' <= char <= 'Z':  # Обрабатываем заглавные английские буквы
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            decrypted_char = chr(((ord(encrypted_char) - ord('A') - shift) % 26) + ord('A'))
        else:  # Оставляем символы, не являющиеся буквами, как есть
            encrypted_char = char
            decrypted_char = char

        encrypted_text += encrypted_char
        decrypted_text += decrypted_char

    return encrypted_text, decrypted_text


# Получаем ввод от пользователя
try:
    shift = int(input("Введите смещение: "))
    message = input("Введите сообщение: ")
except ValueError:
    print("Ошибка: Некорректный ввод смещения. Пожалуйста, введите целое число.")
    exit()  # Прекращаем выполнение, если ввод неверный

# Шифруем и расшифровываем
encrypted_message, decrypted_message = caesar_cipher(message, shift)

# Выводим результаты
print("Шифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)