def is_prime(number):
    if number <= 1:
        return False

    for num in range(2, number):
        if number % num == 0:
            return False
    return True            

print(is_prime(10))