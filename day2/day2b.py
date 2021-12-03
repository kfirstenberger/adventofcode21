def position():
    file = open("directions.txt", "r")
    instructions = file.read()
    my_list = instructions.split("\n")
    hor = 0
    ver = 0
    aim = 0 
    
    for i in my_list:

        if "forward" in i:
            current_hor = i.split(" ")
            for i in current_hor:
                if i in ("0 1 2 3 4 5 6 7 8 9"):
                    hor_num = int(i)
                    hor = hor + hor_num
                    ver = ver + (aim * hor_num)

        if "up" in i:
            current_ver = i.split(" ")
            for i in current_ver:
                if i in ("0 1 2 3 4 5 6 7 8 9"):
                    ver_num = int(i)
                    aim = aim - ver_num
        
        if "down" in i:
            current_ver = i.split(" ")
            for i in current_ver:
                if i in ("0 1 2 3 4 5 6 7 8 9"):
                    ver_num = int(i)
                    aim = aim + ver_num
        
        multiply_final = hor * ver
    
    print(multiply_final)
    
position()
