# # замыкания
#
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
#
# closure = outer(10)
# result = closure(5)
# print(result)

# import threading
# import time
#
# counter = 0
# lock = threading.Lock() # The key to our shared data
#
# def worker():
#     global counter
#     for _ in range(10):
#         with lock:
#             # Read the value, add 1, write it back
#             current_value = counter
#             new_value = current_value + 1
#             time.sleep(.01)
#             counter = new_value
#
# # Create two "workers" (threads)
# threads = []
# for _ in range(2):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()
#
# # Wait for both threads to finish
# for t in threads:
#     t.join()
#
# print(f"Final count should be 20")
# print(f"Actual final count is: {counter}")


# # Semaphore
# import time
# import random
# import threading
#
# # Bouncer only allows 3 threads in at a time
# semaphore = threading.Semaphore(10)
#
# def access_resource(thread_id):
#     print(f"Thread {thread_id} is waiting to access the resource...")
#     with semaphore:
#         print(f"--> Thread {thread_id} has entered!")
#         time.sleep(random.randint(1, 3))
#         print(f"<-- Thread {thread_id} is leaving...")
#
# # Create 10 threads all trying to get in
# threads = [threading.Thread(target=access_resource, args=(i,)) for i in range(10)]
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()

# # Events
# import time
# import threading
#
# event = threading.Event()
#
# def worker():
#     print("Worker: Waiting for the data to be ready...")
#     event.wait() # Pauses here
#     print("Worker: Data is ready! Starting my work.")
#
# def data_preparer():
#     print("Preparer: Getting data ready...")
#     time.sleep(3) # Simulate work
#     print("Preparer: Data is ready! Firing the signal.")
#     event.set() # Fire the pistol
#
# t1 = threading.Thread(target=worker)
# t2 = threading.Thread(target=data_preparer)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

# # # Barrier
#
# import time
# import random
# import threading
#
# # A barrier for 3 threads
# barrier = threading.Barrier(3)
#
#
# def worker(worker_id):
#     print(f"Worker {worker_id}: Running stage 1...")
#     time.sleep(random.randint(1, 4))  # Simulate work
#
#     print(f"Worker {worker_id}: Reached the barrier, waiting for others...")
#     barrier.wait()  # Everyone waits here
#
#     print(f"Worker {worker_id}: Barrier passed! Running stage 2.")
#
#
# # Create 3 threads
# threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
