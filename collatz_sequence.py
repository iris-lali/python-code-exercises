def collatz(number):
    if number % 2 == 0:
        # Even case
        result = number // 2
        print(result)
        return result
    else:
        # Odd case
        result = 3 * number + 1
        print(result)
        return result

while True:
    try:
        user_input = int(input("Please Enter a number: "))
        if user_input <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("That's not an integer. please try again.")

while user_input !=1:
    user_input = collatz(user_input)
print("Reached 1 - sequence complete!")