a = 80000
b = 200000
anos = 0
while  b > a:
    a = (a * 0.03) + a
    b = (b * 0.015) + b
    anos += 1

print(f'Demorou {anos} anos para o Pais A passar o B')
