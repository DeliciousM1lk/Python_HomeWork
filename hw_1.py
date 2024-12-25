import time
import random
import threading


def create_file_with_random_number(n):
    time.sleep(1)
    random_number = random.randint(1, 100)
    with open(f"file_{n}.txt", 'w') as f:
        f.write(f"Random number: {random_number}")


if __name__ == "__main__":
    start_time = time.time()

    for i in range(1000):
        create_file_with_random_number(i)

    end_time = time.time()
    print(f"Time taken for 1000 file creations sequentially: {end_time - start_time} seconds")

    start_time = time.time()
    threads = []

    for i in range(1000):
        thread = threading.Thread(target=create_file_with_random_number, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Time taken for 1000 file creations with multithreading: {end_time - start_time} seconds")
