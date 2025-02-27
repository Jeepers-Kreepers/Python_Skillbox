def analyze_war_and_peace(filename="war_and_peace.txt"):
    print("начало")
    """
    Анализирует файл "Война и мир", подсчитывает статистику символов и выводит предложения с именем Андрей.
    Args:
        filename: Имя файла с романом.
    Returns:
        None (выводит результаты в консоль).
    """

    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        return

    # 1. Статистика по символам
    char_counts = {}
    total_chars = 0
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
        total_chars += 1

    # Вычисление частоты встречаемости
    char_frequencies = {
        char: count / total_chars for char, count in char_counts.items()
    }

    # Сортировка по убыванию частоты и вывод топ-5
    sorted_frequencies = sorted(
        char_frequencies.items(), key=lambda item: item[1], reverse=True
    )
    print("Статистика:")
    for char, frequency in sorted_frequencies[:5]:
        print(f"{char} : {frequency:.2f}")

    # 2. Поиск предложений с "Андрей"
    text = text.replace('? ', '. ').replace('.', '. ').replace('\n', '. ')
    # text = text.replace('.', '. ')
    # text = text.replace('\n', '. ')

    sentences = text.split('. ')

    # Создаем множество вариантов имени "Андрей"
    andrei_variations = {
        "Андрей",
        "Андрея",
        "Андрею",
        "Андреем",
        "Андрее",
    }

    andrei_sentences = []
    for sentence in sentences:
        if any(variation in sentence for variation in andrei_variations):
            andrei_sentences.append(sentence.strip())

    print("\nПредложения со словом «Андрей»:")
    print("\n_______________________________")
    for i, sentence in enumerate(andrei_sentences[:10]):
        print(sentence)


print(analyze_war_and_peace())
