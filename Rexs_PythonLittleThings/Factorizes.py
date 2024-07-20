# W Wersja Synchroniczna

# import time


# def factorize(numbers):
#     result = []
#     for number in numbers:
#         legit_numbers = [i for i in range(1, number + 1) if number % i == 0]
#         result.append(legit_numbers)
#     return result


# def time_measurement(func, *args):
#     start_time = time.time()
#     result = func(*args)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     return result, elapsed_time


# def main():
#     numbers = [128, 255, 99999, 10651060]

#     sync_result, sync_time = time_measurement(factorize, numbers)

#     print(f"Synchronous result: {sync_result}")
#     print(f"Synchronous execution time: {sync_time:.6f} seconds")


# if __name__ == "__main__":
#     main()


# Wersja Asynchroniczna

import multiprocessing
import time


def factorize_single(number):
    return [i for i in range(1, number + 1) if number % i == 0]


def parallel_factorize(numbers):
    with multiprocessing.Pool() as pool:
        result = pool.map(factorize_single, numbers)
    return result


def time_measurement(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time


def main():
    numbers = [128, 255, 99999, 10651060]

    parallel_result, parallel_time = time_measurement(
        parallel_factorize, numbers)

    print(f"Parallel result: {parallel_result}")
    print(f"Parallel execution time: {parallel_time:.6f} seconds")


if __name__ == "__main__":
    main()
