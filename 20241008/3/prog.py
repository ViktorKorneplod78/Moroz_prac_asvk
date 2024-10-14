roof = input()
w = len(roof) - 2
h = 0
water = 0

while True:
    layer = input()
    gas_cnt = layer.count('.')
    water_cnt = layer.count('~')
    if gas_cnt + water_cnt == 0:
        break
    h += 1
    water += water_cnt

gas = w * h - water
if h != 0:
    water_layers = water // h
    if water % h > 0:
        water_layers = water // h + 1
else:
    water_layers = 0

w, h = h, w
print("#" * (w + 2))
for i in range(h - water_layers):
    print("#", "." * w, "#", sep = "")
for i in range(water_layers):
    print("#", "~" * w, "#", sep = "")
print("#" * (w + 2))

if gas == 0:
    gas_len = 0
    if water == 0:
        water_len = 0
        len_ = 1
    else:
        water_len = 20
        len_ = len_ = len(str(water))
elif water == 0:
    water_len = 0
    gas_len = 20
    len_ = len(str(gas))
elif gas > water:
    len_ = len(str(gas))
    gas_len = 20
    water_len = round(water / gas * 20)
else:
    len_ = len(str(water))
    water_len = 20
    gas_len = round(gas / water * 20)

print("." * gas_len, " " * (20 - gas_len + 1), f"{gas:{len_}}/{w * h}", sep = "")
print("~" * water_len, " " * (20 - water_len + 1), f"{water:{len_}}/{w * h}", sep = "")
