
import time
import requests




def test_get_pages(url):
    start_time = time.time()

    # Отправляем GET запрос
    response = requests.get(url)

    # Проверяем статус ответа
    if(response.status_code == 200):

        end_time = time.time()
        elapsed_time = end_time - start_time

        return ("GOOD",response,elapsed_time)
    else:

        end_time = time.time()
        elapsed_time = end_time - start_time

        return ("EROR",response,elapsed_time)

    # Проверяем данные в ответе
    #data = response.json()  # Предположим, что ответ должен быть в формате JSON
    #expected_data = {'gyms': [{'reservation_time': '00:30:00', 'reservation_date': '2024-08-27', 'address': 'Na kykah 32', 'gym_name': 'Far'}]} # Задайте ваши ожидания

    #assert data == expected_data, f"Expected data {expected_data}, got {data} "


def test_get_pages_json(url ,date):
    start_time = time.time()

    # Отправляем GET запрос
    response = requests.get(url,json=date)

    # Проверяем статус ответа
    if(response.status_code == 200):

        end_time = time.time()
        elapsed_time = end_time - start_time

        return ("GOOD",response,elapsed_time)
    else:

        end_time = time.time()
        elapsed_time = end_time - start_time

        return ("EROR",response,elapsed_time)



