s = input()
match s.split():
    case ["mov", r1, r2, *tail] if len(tail) == 0:
        print(f"movint {r2} to {r1}")
    case ["push" as comand, *reglist] | ["pop" as comand, *reglist] if len(reglist) > 0:
        print(f"{comand}ing {' '.join(reglist)}")
    case [cmd, r1, *tail] if len(tail) == 0:
        print(f"making {cmd} with {r1}")
    case _:
        print("Parse error")
