def palindrome(s):
    return s[::-1] == s

while True:
    s = input("Введите слов: ")
    if palindrome(s):
        print('да')
    else:
        print('нет')