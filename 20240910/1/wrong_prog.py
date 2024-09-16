import ast

in_str = input()
s = ast.literal_eval(in_str)

#new_s = sorted(s)
out_str = ', '.join(map(str, s))

print(out_str)
