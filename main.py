limit = 1000

counter = 1
while counter <= limit:
    if counter % 3 == 0 and counter % 5 == 0:
        print("Fizzbuzz")
    elif counter % 3 == 0:
        print ("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)

