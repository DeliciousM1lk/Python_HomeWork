import time
import random
from multiprocessing import Pool, cpu_count

def write_random_number_to_file(index):
    time.sleep(1)
    random_number = random.randint(1, 1000)
    file_name = f"random_number_{index}.txt"
    with open(file_name, "w") as file:
        file.write(str(random_number))
    return file_name

if __name__ == "__main__":
    print("\nЗапуск в последовательном режиме...")
    start_time = time.time()
    for i in range(1000):
        write_random_number_to_file(i)
    sequential_time = time.time() - start_time
    print(f"Последовательный запуск занял {sequential_time:.2f} секунд.")

    print("\nЗапуск в параллельном режиме...")
    start_time = time.time()
    with Pool(cpu_count()) as pool:
        pool.map(write_random_number_to_file, range(1000))
    parallel_time = time.time() - start_time
    print(f"Параллельный запуск занял {parallel_time:.2f} секунд.")

    print("\nСравнение времени выполнения:")
    print(f"Последовательный режим: {sequential_time:.2f} секунд")
    print(f"Параллельный режим: {parallel_time:.2f} секунд")
