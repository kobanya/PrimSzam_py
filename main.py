## taking input from user / bevitel
number = int(input("Enter any number / írj be egy számot: "))

# prime number is always greater than 1 / a prím szám 1-nél mindig nagyobb
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number / nem prím szám")
            break
    else:
        print(number, "is a prime number / prím szám")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number /  Nem prym szám")