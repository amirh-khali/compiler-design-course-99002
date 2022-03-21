def q2(str):
    lastwords = [" ", "\n", "\t"]
    state = 0
    index = 0
    while index < len(st) and str[index] not in lastwords:
        if str[index] == '1' and state == 0:
            state = 1
        elif str[index] == '1' and state == 1:
            state = 2
        elif str[index] == '1' and state == 2:
            state = 2
        elif str[index] == '0' and state == 0:
            state = 0
        elif str[index] == '0' and state == 1:
            state = 0
        elif str[index] == '0' and state == 2:
            state = 3
        elif (str[index] == '0' or str[index] == '1') and state == 3:
            state = 3
        index += 1

    if state != 3:
        print("reject(lex error)")
    else:
        print("accepted")

st = input()
q2(st)






