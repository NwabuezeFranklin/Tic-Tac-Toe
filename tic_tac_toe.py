n = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
print('---------')
print('| '+ n[0] + ' ' + n[1] + ' ' + n[2] + ' |')
print('| '+ n[3] + ' ' + n[4] + ' ' + n[5] + ' |')
print('| '+ n[6] + ' ' + n[7] + ' ' + n[8] + ' |')
print('---------')
attempts = 0
while attempts <= 9:
    m = 0
    j = 0
    try:
        m, j = map(int, input().split())
    except Exception:
       print('You should enter numbers!')
       continue
    m = int(m)
    j = int(j)
    if m > 3 or j > 3:
        print("Coordinates should be from 1 to 3!")
    if attempts % 2 == 0:
        if (m == 1) and (j == 1):
            if n[0] == "_" or n[0] == " ":
                n[0] = 'X'

            else:
                print('This cell is occupied! Choose another one!')
        elif (m == 1) and (j == 2):
            if n[1] == "_" or n[1] == " ":
                n[1] = 'X'

            else:
                print('This cell is occupied! Choose another one!')

        elif (m == 1) and (j == 3):
            if n[2] == "_" or n[2] == " ":
                n[2] = 'X'

            else:
                print('This cell is occupied! Choose another one!')


        elif (m == 2) and (j == 1):
            if n[3] == "_" or n[3] == " ":
                n[3] = 'X'

            else:
                print('This cell is occupied! Choose another one!')
        elif (m == 2) and (j == 2):
            if n[4] == "_" or n[4] == " ":
                n[4] = 'X'

            else:
                print('This cell is occupied! Choose another one!')

        elif (m == 2) and (j == 3):
            if n[5] == "_" or n[5] == " ":
                n[5] = 'X'

            else:
                print('This cell is occupied! Choose another one!')


        elif (m == 3) and (j == 1):
            if n[6] == "_" or n[6] == " ":
                n[6] = 'X'

            else:
                print('This cell is occupied! Choose another one!')

        elif (m == 3) and (j == 2):
            if n[7] == "_" or n[7] == " ":
                n[7] = 'X'

            else:
                print('This cell is occupied! Choose another one!')

        elif (m == 3) and (j == 3 ):
            if n[8] == "_" or n[8] == " ":
                n[8] = 'X'

            else:
                print('This cell is occupied! Choose another one!')

        print('---------')
        print('| ' + n[0] + ' ' + n[1] + ' ' + n[2] + ' |')
        print('| ' + n[3] + ' ' + n[4] + ' ' + n[5] + ' |')
        print('| ' + n[6] + ' ' + n[7] + ' ' + n[8] + ' |')
        print('---------')
    else:
        if (m == 1) and (j == 1):
            if n[0] == "_" or n[0] == " ":
                n[0] = 'O'

            else:
                print('This cell is occupied! Choose another one!')
        elif (m == 1) and (j == 2):
            if n[1] == "_" or n[1] == " ":
                n[1] = 'O'

            else:
                print('This cell is occupied! Choose another one!')

        elif (m == 1) and (j == 3):
            if n[2] == "_" or n[2] == " ":
                n[2] = 'O'

            else:
                print('This cell is occupied! Choose another one!')


        elif (m == 2) and (j == 1):
            if n[3] == "_" or n[3] == " ":
                n[3] = 'O'

            else:
                print('This cell is occupied! Choose another one!')
        elif (m == 2) and (j == 2):
            if n[4] == "_" or n[4] == " ":
                n[4] = 'O'

            else:
                print('This cell is occupied! Choose another one!')

        elif (m == 2) and (j == 3):
            if n[5] == "_" or n[5] == " ":
                n[5] = 'O'

            else:
                print('This cell is occupied! Choose another one!')


        elif (m == 3) and (j == 1):
            if n[6] == "_" or n[6] == " ":
                n[6] = 'O'

            else:
                print('This cell is occupied! Choose another one!')

        elif (m == 3) and (j == 2):
            if n[7] == "_" or n[7] == " ":
                n[7] = 'O'

            else:
                print('This cell is occupied! Choose another one!')

        elif (m == 3) and (j == 3):
            if n[8] == "_" or n[8] == " ":
                n[8] = 'O'

            else:
                print('This cell is occupied! Choose another one!')

        print('---------')
        print('| ' + n[0] + ' ' + n[1] + ' ' + n[2] + ' |')
        print('| ' + n[3] + ' ' + n[4] + ' ' + n[5] + ' |')
        print('| ' + n[6] + ' ' + n[7] + ' ' + n[8] + ' |')
        print('---------')

    check1 = [i for i in range(3) if n[i] == "X"]

    check2 = [i for i in range(3, 6) if n[i] == "X"]

    check3 = [i for i in range(6, 9) if n[i] == "X"]

    check4 = [i for i in range(0, 7, 3) if n[i] == "X"]

    check5 = [i for i in range(1, 8, 3) if n[i] == "X"]

    check6 = [i for i in range(2, 9, 3) if n[i] == "X"]

    check7 = [i for i in range(0, 9, 4) if n[i] == "X"]

    check8 = [i for i in range(2, 7, 2) if n[i] == "X"]

    rcheck1 = [i for i in range(3) if n[i] == "O"]

    rcheck2 = [i for i in range(3, 6) if n[i] == "O"]

    rcheck3 = [i for i in range(6, 9) if n[i] == "O"]

    rcheck4 = [i for i in range(0, 7, 3) if n[i] == "O"]

    rcheck5 = [i for i in range(1, 8, 3) if n[i] == "O"]

    rcheck6 = [i for i in range(2, 9, 3) if n[i] == "O"]

    rcheck7 = [i for i in range(0, 9, 4) if n[i] == "O"]

    rcheck8 = [i for i in range(2, 7, 2) if n[i] == "O"]
    new = [len(check1), len(check2), len(check3), len(check4), len(check5), len(check6), len(check7), len(check8)]
    newer = [len(rcheck1), len(rcheck2), len(rcheck3), len(rcheck4), len(rcheck5), len(rcheck6), len(rcheck7),
             len(rcheck8)]

    if len(rcheck1) == 3 or len(rcheck2) == 3 or len(rcheck3) == 3:
        print("O wins")
        break
    elif len(rcheck4) == 3 or len(rcheck5) == 3 or len(rcheck6) == 3 or len(rcheck7) == 3 or len(rcheck8) == 3:
        print("O wins")
        break
    elif len(check1) == 3 or len(check2) == 3 or len(check3) == 3:
        print("X wins")
        break
    elif len(check4) == 3 or len(check5) == 3 or len(check6) == 3 or len(check7) == 3 or len(check8) == 3:
        print("X wins")
        break

    attempts += 1
    if attempts == 10:
        print("Draw")
        break


