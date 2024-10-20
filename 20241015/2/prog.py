from math import *

func_args_n = {}
func_cnt = 1
str_cnt = 0

def construct_arg_str(str_orig, s):
    i = len(s[0])
    while str_orig[i] != s[1][0]:
        i += 1
    return(str_orig[i:])

def construct_func(str_orig, s):
    func_name = s[0][1:]
    func = "def _" + func_name + "("
    for i in range(1, len(s) - 1):
        func += s[i]
        if i != len(s) - 2:
            func += ", "
    func += "):\n    return " + s[len(s) - 1]
    return func

def construct_call(str_orig, s):
    args = ""
    if func_args_n[s[0]] > 1:
        for i in range(1, len(s)):
            args += s[i]
            if i != len(s) - 1:
                args += ", "
    elif func_args_n[s[0]] == 1:
        args = construct_arg_str(str_orig, s)
    return "_" + s[0] + "(" + args + ")"

while True:
    str_orig = input()
    s = str_orig.split()
    str_cnt += 1

    if s[0][0] == ":":
        func_cnt += 1
        exec(construct_func(str_orig, s))
        func_args_n[s[0][1:]] = len(s) - 2

    elif s[0] == "quit":
        i = len(s[0])
        arg = construct_arg_str(str_orig, s)
        print(eval(arg + ".format(" + str(func_cnt) + ", " + str(str_cnt) + ")"))
        break

    else:
        print(eval(construct_call(str_orig, s)))
