def increase_counter():
    f = open("input.txt", "r")
    data = f.read()
    my_list = data.split("\n")
    my_number_list = []
    my_snl = my_number_list
    count = 0

    for i in my_list:
        number = int(i)
        my_number_list.append(number)

    for n in my_number_list[:-1]:
        index = my_snl.index(n)
        second_index = index + 1
        if n < my_snl[second_index]:
            count +=1
        my_snl.pop(index)
    
    print(count)

increase_counter()
