import datetime
import logging

# Настройка логирования
logging.basicConfig(filename='logs.log', level=logging.DEBUG,
                    format='%(asctime)s | %(levelname)s | %(name)s:%(module)s:%(lineno)d - %(message)s')


def calculate_time_spent(filename="data.txt"):
    """
    Рассчитывает время, проведенное спортсменами в бассейне и комплексе, и записывает логи об ошибках.

    Args:
        filename (str): Имя файла с данными.

    Returns:
        None
    """

    athlete_times = {}  # {athlete_id: {location: [in_time, out_time]}}

    try:
        with open(filename, 'r') as f:
            next(f)  # Пропускаем заголовок
            for line in f:
                try:
                    date_str, athlete_id, location, type = line.strip().split('\t')
                    date_time = datetime.datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
                    athlete_id = int(athlete_id)

                    if athlete_id not in athlete_times:
                        athlete_times[athlete_id] = {}
                    if location not in athlete_times[athlete_id]:
                        athlete_times[athlete_id][location] = []

                    if type == 'In':
                        athlete_times[athlete_id][location].append([date_time, None])  # Вход, время выхода пока None
                    elif type == 'Out':
                        # Ищем соответствующую запись о входе и обновляем время выхода
                        found_match = False
                        for i in range(len(athlete_times[athlete_id][location]) - 1, -1, -1):
                            if athlete_times[athlete_id][location][i][1] is None:  # Нашли незакрытый вход
                                athlete_times[athlete_id][location][i][1] = date_time
                                found_match = True
                                break
                        if not found_match:
                            logging.debug(f"Не зафиксировано время входа атлета {athlete_id} в {location}")

                except ValueError as e:
                    logging.error(f"Ошибка при обработке строки: {line.strip()} - {e}")
    except FileNotFoundError:
        logging.error(f"Файл '{filename}' не найден.")
        return

    # Расчет времени и вывод результатов
    for athlete_id, locations in athlete_times.items():
        for location, times in locations.items():
            for in_time, out_time in times:
                if in_time and out_time:
                    time_spent = (out_time - in_time).total_seconds() / 60  # в минутах
                    print(f"Атлет {athlete_id} провёл в {location}: {int(time_spent)} мин.")
                else:
                    if not in_time:
                        logging.debug(f"Не зафиксировано время входа атлета {athlete_id} в {location}")
                    if not out_time:
                        logging.debug(f"Не зафиксировано время выхода атлета {athlete_id} из {location}")


# Создаем файл с данными для примера
data = """Date	Athlete ID	Location	Type
01/01/2023 9:00:00	10012	Center	Out
01/01/2023 9:00:00	10001	Pool-1	Out
01/01/2023 9:00:00	10001	Pool-1	Out
01/01/2023 9:00:00	10011	Pool-2	In
01/01/2023 12:14:59	10011	Pool-1	In
01/01/2023 12:44:59	10011	Pool-2	Out
01/01/2023 12:14:59	10013	Center	Out
01/01/2023 12:14:59	10019	Pool-2	In
01/01/2023 16:14:59	10018	Pool-1	Out
01/01/2023 16:14:59	10020	Pool-2	Out
01/01/2023 16:14:59	10011	Pool-2	In
01/01/2023 18:39:55	10011	Center	In
01/01/2023 19:09:55	10011	Pool-2	Out
01/01/2023 18:39:55	10017	Pool-2	In
01/01/2023 20:41:40	10017	Center	In
01/01/2023 21:11:40	10017	Pool-2	Out"""

with open("data.txt", "w") as f:
    f.write(data)

# Вызываем функцию для обработки данных из файла
calculate_time_spent("data.txt")