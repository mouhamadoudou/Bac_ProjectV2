#!/usr/bin/env python3
##
## Mouhamadou Niang, 2022
## project_main.py
## File description:
## main file
##

import sys

def get_time(av):
    data = av[0].split()
    return (data)

def get_student(av):
    data = []
    data.append(av[1])
    return (data)

def get_file(av):
    doc_file = open(av, "r")
    result = doc_file.read()
    doc_file.close()
    data = result.split("\n")
    data.append(None)
    return (data)

def get_col(av, nb_col):
    result = []
    result2 = []
    data = []
    i = 2
    a = 0

    while av[i + 1] != None:
        result = av[i].split(" ")
        result2.append(result)
        data.append(result2[a][nb_col])
        a += 1
        i += 1
    data.append(None)
    return (data)

def get_list(data_str):
    all_col = []

    all_col.append(get_col(data_str, 0))
    all_col.append(get_col(data_str, 1))
    all_col.append(get_col(data_str, 2))
    return (all_col)

def display_flag_h():
    print("USAGE")
    print("   ./get_potion\n")
    print("A TEXT FILE MUST COMPOSED :")
    print("   The first line: the time in minutes given to each jury, separated by a space")
    print("   On the seconde line: the number of `N` participants in the BAC")
    print("   On the following `N` lines: the correction time of the 3 copies of each participant, separated by a space\n\n")
    print("Return :")
    print(" - False` if one of the juries cannot finish on time\n - True' if all juries can finish on time")

def calc_time(data_time, len_l, time):
    time1 = 0
    time2 = 0
    time3 = 0
    i = 0
    a = 0
    
    while a < len_l:
        time1 = time1 + int(data_time[i][0])
        time2 = time2 + int(data_time[i][1])
        time3 = time3 + int(data_time[i][2])
        a += 1

    time.append (time1)
    time.append (time2)
    time.append (time3)
    return
    
def calc_list(data_l, len_l, result):
    check1 = 0
    check2 = 0
    check3 = 0
    i = 0
    a = 0

    while a < len_l:
        i = 0
        while data_l[0][0][i] != None:
            check1 = check1 + int(data_l[0][0][i])
            check2 = check2 + int(data_l[0][1][i])
            check3 = check3 + int(data_l[0][2][i])
            i += 1
        a += 1
    result.append (check1)
    result.append (check2)
    result.append (check3)
    return (-1)
    
def check_result(result, time):
    if time[0] >= result[0] and time[1] >= result[1] and time[2] >= result[2]:
        print("True")
    else:
        print("False")

def start(data_list, data_time, nb_student, len_s):
    i = 0
    result = []
    time = []

    calc_list(data_list, len_s, result)
    calc_time(data_time, len_s, time)
    check_result(result, time)
    
def main_start(arg, data_time, nb_student, data_list, argc):

    data_s = get_file(arg)
    nb_stud = get_student(data_s)

    if int(nb_stud[0]) == 0:
        argc.append(argc[len(argc) - 1] - 1)
        return 
    data_t = get_time(data_s)
    data_l = get_list(data_s)
    
    data_time.append(data_t)
    nb_student.append(nb_stud)
    data_list.append(data_l)
    return
    
def main():
    argc = []
    argc.append(len(sys.argv) - 1)
    i = 1
    data_list = []
    data_time = []
    nb_student = []

    if argc == 2:
        if (sys.argv[1][0] == '-' and sys.argv[1][1] == 'h' and len(sys.argv[1]) == 2):
            display_flag_h()
            sys.exit(0)
    while i <= argc[0]:
        main_start(sys.argv[i], data_time, nb_student, data_list, argc)
        i += 1
    data_list.append(None)
    if argc[0] >= 1:
        start(data_list, data_time, nb_student, argc[len(argc) - 1])
    sys.exit(0)

if __name__ == '__main__':
    main()
