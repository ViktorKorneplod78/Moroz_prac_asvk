start = list(eval(input()))
n = len(start)
op1 = []
op2 = []
mul = []

op1.append(start)
for i in range(1, n):
  op1.append(list(eval(input())))
for i in range(0, n):
  op2.append(list(eval(input())))

for i in range(0, n):
  mul.append([])
  for j in range(0, n):
    elem_sum = 0
    for k in range(0, n):
      elem_sum += op1[i][k] * op2[k][j]
    mul[i].append(elem_sum)

for i in range(0, n):
  print(*mul[i], sep = ",")
