# def is_prime(number):
#     if number <= 1:
#         return False
#     if number == 2:
#         return True
#     if number % 2 == 0:
#         return False
#     for i in range(3, int(number**0.5) + 1, 2):
#         if number % i == 0:
#             return False
#     return True

# # Get input from the user
# num = int(input("Enter a number: "))

#  # Determine if the number is prime or composite
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is a composite number.")

# Take user input
num = int(input("Please enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is a composite number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
