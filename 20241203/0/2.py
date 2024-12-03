t = "qweas"
match t.split():
    case []:
        print("empty")
    case ["qwe"]:
        print("no doubt qwe")
    case [str(x)]:
        print("list of 1 str")
    case [x]:
        print("a list of 1")
    case [_, *tail]:
        print("list with tail", tail)
