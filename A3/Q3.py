def q3(my_str):
    state = 0
    index = 0
    while index < len(my_str) and my_str[index] not in ["\n", "\t"]:
        if my_str[index] == '1' and state == 0:
            state = 1
        elif my_str[index] == '1' and state == 1:
            state = 2
        elif my_str[index] == '1' and state == 2:
            state = 2
        elif my_str[index] == '1' and state == 3:
            state = 4
        elif my_str[index] == '0' and state == 0:
            state = 0
        elif my_str[index] == '0' and state == 1:
            state = 0
        elif my_str[index] == '0' and state == 2:
            state = 3
        elif my_str[index] == '0' and state == 3:
            state = 0
        elif (my_str[index] == '0' or my_str[index] == '1') and state == 4:
            state = 4

        index += 1

    if state == 4:
        print("reject(lex error)")
    else:
        print("accepted")


q3(input())
