my_list=[42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

var = 0            # доп_переменная

while var < len(my_list):

    print(my_list[var])

    var += 1

    if my_list[var] < 0:

        break


