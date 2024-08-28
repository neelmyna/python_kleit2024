def check_arrangement(input_str):
    open_count = close_count = 0
    arrangement = True # Assume the proper arrangement
    for char in input_str:
        if char == '(':
            open_count += 1
        else:
            close_count += 1
        if close_count > open_count:
            arrangement = False
            break
    if arrangement and open_count == close_count:
        print('Number of pairs = ', open_count)
    else:
        print('Improper Arrangement')