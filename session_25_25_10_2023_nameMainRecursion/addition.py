def add(x, y):
    z = x + y
    print('add() fonksiyonu ana alan içinde yürütülüyor', __name__)
    return z

x = input('Birinci sayıyı giriniz')
y = input('İkinci sayıyı giriniz')

result = add(int(x), int(y))

print(x, '+', y, '=', result)

print("Bu kod ana alanda yürütülüyor", __name__)