def add(x, y):
    z = x + y
    print("add() fonksiyonu ana alan icinde yürütülüyor", __name__)
    return z


x = input('Birinci sayiyi giriniz')
y = input('Ikinci sayiyi giriniz')

result = add(int(x), int(y))

print(x, '+', y, '=', result)

print("Bu kod ana alanda yürütülüyor", __name__)