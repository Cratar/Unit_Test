import requests
import time


def test_delete_pages(url ,date ):
    start_time = time.time()
    # Отправляем GET запрос
    response = requests.delete(url,json=date)
    # Проверяем статус ответа
    if (response.status_code == 200):
        end_time = time.time()
        elapsed_time = end_time - start_time
        return ("GOOD", response, elapsed_time)
    else:
        end_time = time.time()
        elapsed_time = end_time - start_time
        return ("EROR", response, elapsed_time)