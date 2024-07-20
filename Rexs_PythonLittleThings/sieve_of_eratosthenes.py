from math import sqrt


def sieve_of_eratosthenes_for(n):
    number_list = [1] * (n + 1)
    max_number = int(sqrt(n))

    for index in range(2, max_number + 1):
        if number_list[index]:
            for index_2 in range(index * index, n + 1, index):
                number_list[index_2] = 0

    prime_numbers = []
    for element in range(2, n + 1):
        if number_list[element]:
            prime_numbers.append(element)

    print(prime_numbers)
