import random

print('Добро пожаловать в числовую угадайку')

def is_valid(inp):
    if inp.isdigit():
        return True
    return False

def retry():
    print('Хотите сыграть ещё?')
    inp = input()
    if inp == 'yes':
        game()
    elif inp == 'no':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    else:
        print('Введите yes или no')
        retry()

def game():
    print('Укажите правую границу для случайного выбора')
    last = input()
    while not is_valid(last):
        print('Введите целое число')
        last = input()
    last = int(last) # Преобразуем правую границу в целое число
    rand = random.randint(1, last)
    count = 1
    num = input()
    while True:
        if not is_valid(num) or int(num) > last:
            print(f'А может быть все-таки введем целое число от 1 до {last}?')
        else:
            if int(num) < rand:
                print('bigger')
                count += 1
            elif int(num) > rand:
                print('smaller')
                count += 1
            else:
                print('victory')
                print(f'Вы угадали число за {count} попыток')
                retry()
                break
        num = input()

game()