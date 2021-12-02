def sum_increase_counter():

    f = open("input.txt", "r")
    data = f.read()
    my_list = data.split("\n")
    my_number_list = []
    my_final_list = []
    my_snl = my_number_list
    count = 0

    for i in my_list:
        number = int(i)
        my_number_list.append(number)
    
    for n in my_number_list[:-2]:
        index = my_snl.index(n)
        second_index = index + 1
        third_index = second_index + 1
        sum_total = my_snl[index] + my_snl[second_index] + my_snl[third_index]
        my_final_list.append(sum_total)
        my_snl.pop(index)
    
    for n in my_final_list[:-1]:
        index_final = my_final_list.index(n)
        second_index_final = index + 1
        if n < my_final_list[second_index_final]:
            count +=1
        my_final_list.pop(index)
    
    print(count)

sum_increase_counter()
