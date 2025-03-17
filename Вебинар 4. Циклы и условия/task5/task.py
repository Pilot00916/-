def josephus_task(num_people, kill_num):
    i = 0
    lst = list(range(1, num_people + 1))
    while len(lst) > 1:
        i = (i + kill_num - 1) % len(lst)
        lst.pop(i)
    return lst[0]