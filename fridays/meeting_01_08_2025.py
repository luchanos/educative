# import multiprocessing
# from multiprocessing import Queue
# import time
# from time import sleep
#
#
# def worker(queue: Queue) -> None:
#     # Рабочий получает данные из очереди
#     print("Рабочий начинает работу")
#     item = queue.get()
#     print(f"Рабочий получил: {item}")
#     sleep(50)
#
# if __name__ == '__main__':
#     q = multiprocessing.Queue()
#
#     p = multiprocessing.Process(target=worker, args=(q,))
#     p.start()
#
#     print("Основной процесс готовит данные...")
#     time.sleep(2)
#     # Основной процесс кладет данные в очередь
#     q.put("Привет из основного процесса!")
#     print("Ещё какая-то полезная работа в основном процессе")
#     time.sleep(50)
#     p.join()


import multiprocessing


def worker(connection):
    # Рабочий получает данные и отправляет ответ
    data = connection.recv()
    print(f"Рабочий получил: {data}")
    connection.send("Ответ от рабочего")
    connection.close()


if __name__ == '__main__':
    # parent_conn используется в основном процессе, child_conn - в дочернем
    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=worker, args=(child_conn,))
    p.start()

    parent_conn.send("Сообщение для рабочего")
    response = parent_conn.recv()
    print(f"Основной процесс получил ответ: {response}")

    p.join()