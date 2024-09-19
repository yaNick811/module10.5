import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data

def linear_read(file_names):
    start_time = time.time()
    for name in file_names:
        read_info(name)
    end_time = time.time()
    print(f"Линейное чтение заняло: {end_time - start_time} секунд")

def multiprocess_read(file_names):
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, file_names)
    end_time = time.time()
    print(f"Многопроцессное чтение заняло: {end_time - start_time} секунд")

if __name__ == "__main__":
    # Список названий файлов
    file_names = ["file 1.txt", "file 2.txt", "file 3.txt", "file 4.txt"]

    # Линейное чтение
    linear_read(file_names)

    # Многопроцессное чтение
    multiprocess_read(file_names)