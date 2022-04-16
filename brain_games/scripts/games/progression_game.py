def get_progression(start, total_steps, difference):
    mylist = [start]
    i = 0
    while i <= total_steps:
        mylist.append(start + difference)
        start = start + difference
        i += 1
    return mylist
