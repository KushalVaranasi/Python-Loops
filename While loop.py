def count_down(start_number):
    current = -1
    while (current <= start_number):
        print(start_number)
        start_number -= 1
        current += 1
    print("Zero!")

count_down(-1)