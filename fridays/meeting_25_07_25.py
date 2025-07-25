# import multiprocessing
#
# # 'i' means it's a signed integer. This creates a value in shared memory.
# shared_counter = multiprocessing.Value('i', 0)
#
# def worker(counter):
#     for _ in range(100_000):
#         # This is NOT atomic. It involves read, increment, write.
#         counter.value += 1
#
# # --- This will FAIL for the same reason the thread example did ---
# if __name__ == '__main__':
#
#     processes = []
#     for _ in range(2):
#         # We must pass the shared object to the child process
#         p = multiprocessing.Process(target=worker, args=(shared_counter,))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#
#     print(f"Final count should be 200,000")
#     print(f"Actual final count is: {shared_counter.value}")


# import multiprocessing
#
# # Create a shared counter
# shared_counter = multiprocessing.Array('i', [])
# # Create a lock that can be shared between processes
# lock = multiprocessing.Lock()
#
# def worker(counter, lock):
#     for _ in range(100_000):
#         with lock:
#             # This block is now safe and will only be run by one process at a time
#             counter.append(1)
#
# # --- This will now work correctly ---
#
# if __name__ == '__main__':
#     processes = []
#     for _ in range(2):
#         # Pass BOTH the shared value AND the lock to the child process
#         p = multiprocessing.Process(target=worker, args=(shared_counter, lock))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#
#     print(f"Final count should be 200,000")
#     print(f"Actual final count is: {shared_counter.value}") # Always 200,000!

# import multiprocessing
# import time
# import random
#
# def producer(queue):
#     """Produces items and puts them in the queue"""
#     for i in range(10):
#         item = f"item_{i}"
#         print(f"Producer: Putting {item} in the queue.")
#         queue.put(item)
#         time.sleep(random.random()) # Simulate work
#     queue.put("DONE") # A signal to the consumer that we're finished
#
# def consumer(queue):
#     """Consumes items from the queue"""
#     while True:
#         item = queue.get() # This will wait if the queue is empty
#         if item == "DONE":
#             print("Consumer: Got DONE signal. Exiting.")
#             break
#         print(f"Consumer: Processing {item}")
#         time.sleep(random.random() * 2) # Simulate work
#
# if __name__ == "__main__":
#     # Create the queue
#     q = multiprocessing.Queue()
#
#     # Create and start the processes
#     p1 = multiprocessing.Process(target=producer, args=(q,))
#     p2 = multiprocessing.Process(target=consumer, args=(q,))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     print("All work finished.")


# import multiprocessing
# import math
#
#
# def square_numbers(shared_array, start_index, end_index):
#     """A worker function that squares numbers in a specific slice of the array."""
#     print(f"Process {multiprocessing.current_process().name} working on slice [{start_index}:{end_index}]")
#     for i in range(start_index, end_index):
#         shared_array[i] = shared_array[i] * shared_array[i]
#
#
# if __name__ == '__main__':
#     # 1. Setup the shared data
#     data_to_process = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     # Create a shared array of integers from our list
#     shared_arr = multiprocessing.Array('i', data_to_process)
#
#     print(f"Original array: {list(shared_arr)}")
#
#     # 2. Divide the work
#     num_processes = 4
#     # Calculate how many items each process should handle
#     chunk_size = math.ceil(len(shared_arr) / num_processes)
#
#     processes = []
#
#     # 3. Create and start the processes
#     for i in range(num_processes):
#         start = i * chunk_size
#         end = min(start + chunk_size, len(shared_arr))  # Ensure we don't go past the end
#
#         if start >= end:
#             continue  # Skip if there's no work left
#
#         p = multiprocessing.Process(
#             target=square_numbers,
#             args=(shared_arr, start, end)
#         )
#         processes.append(p)
#         p.start()
#
#     # 4. Wait for all processes to finish
#     for p in processes:
#         p.join()
#
#     # 5. View the result
#     # The original shared_arr has been modified in place!
#     print(f"Squared array:  {list(shared_arr)}")

# import threading
#
# # The only change is here!
# rlock = threading.Lock()
#
# def do_something_else():
#     print("  (Inner) Trying to acquire the RLock again...")
#     with rlock: # <-- This works fine now!
#         print("  (Inner) RLock acquired successfully. Inner work done.")
#
# def do_something():
#     print("(Outer) Acquiring RLock...")
#     with rlock:
#         print("(Outer) RLock acquired. Calling another function...")
#         do_something_else()
#     print("(Outer) RLock fully released.")
#
# # This runs to completion without any problems.
# t = threading.Thread(target=do_something)
# t.start()
# t.join()
# print("Script finished.")
