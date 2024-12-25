import time
import threading

def create_file_with_delay(n):
    time.sleep(1)
    with open(f"file_{n}.txt", 'w') as f:
        f.write(f"This is file number {n}")

if __name__ == "__main__":
    start_time = time.time()

    for i in range(100):
        create_file_with_delay(i)

    end_time = time.time()
    print(f"Time taken for 100 file creations sequentially: {end_time - start_time} seconds")

    start_time = time.time()

    threads = []

    for i in range(100):
        thread = threading.Thread(target=create_file_with_delay, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Time taken for 100 file creations with multithreading : {end_time - start_time} seconds")
