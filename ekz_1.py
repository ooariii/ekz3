def card(a):
    res = (a % 10000)
    print('*' * 12, res)
    return res

if __name__ == '__main__':
    a = int(input('введите номер карты: '))
    card(a)
