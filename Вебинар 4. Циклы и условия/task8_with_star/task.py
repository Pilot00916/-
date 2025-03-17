def max_division_by_3(num):
    str_num = str(num)
    max_number = -1

    for i in range(len(str_num)):
        for digit in '0123456789':
            if str_num[i] != digit:
                new_num_str = str_num[:i] + digit + str_num[i+1:]
                new_num = int(new_num_str)
                if new_num % 3 == 0:
                    max_number = max(max_number, new_num)

    return max_number
