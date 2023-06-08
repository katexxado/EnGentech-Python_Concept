def tt(number):

    print(f"Enter Value: {number}")
    print(f"{number} time_table")
    for a in range (1,13):
        result = number * a
        print(f"{number} x {a} = {result}")

tt(2)