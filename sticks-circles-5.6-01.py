def show_field(f):
    print(' '+'___ '*(size))
    for k in range(size):
        print('|'+'   |'*(size))
        line  = []
        for m in range(size):
            line.append('|')
            line.append(f.get(10*k+m))
        print(*line, '|')
        print('|'+'___|'*(size))


def keys(n=3):
    keys = set()
    key = 0
    for i in range(n+1):
        for j in range(n+1):
            key = j + 10*i
            keys.add(key)
    return keys
    

def nums_field(*args):
    field = {}
    for i in keys(size-1):
        if 0 <= i < 10:
            field[i] = i
        elif 10 <= i < 100 and not i % 10:
            field[i] = i // 10
        else:
            field[i] = ' '  
    return field
            

def input_key(key):
    key == ' '
    return input_key


def step():
    button = input('Введите № клетки (0 - выход из программы): ')
    if button != '0':
        if not button.isdigit():
            print('Только цифры. Повторите ввод № клетки ')
            step()
        elif int(button)==0 or int(button)<10 or int(button)%10==0 or int(button)%10>N or int(button)//10>N:
            print('Запрещенный символ. Повторите ввод № клетки ')
            step()
        elif check_busy(int(button)):
            print('Клетка занята. Повторите ввод № клетки ')
            step()
    return button
    

def check_busy(button):
    if field[button] != ' ':
        return True
    else:
        return False
    

def victory():
    if horizont(main_line):
        win = horizont(main_line)
    elif vertikal(main_line):
        win = vertikal(main_line)
    elif diaginal_1(main_line):
        win = diaginal_1(main_line)
    elif diaginal_2(main_line):
        win = diaginal_2(main_line)
    else:
        win = 0
    return win

def horizont(hL):
    for j  in range (size-1):
        line = []
        for i in range (size-1):
            line.append(hL[i+j*(size-1)])
        if chek_kit(line):
            break
        j += 1
    return chek_kit(line)

def vertikal(vL):
    for j  in range (size-1):
        line = []
        for i in range (size-1):
            line.append(vL[i*(size-1)+j])
        if chek_kit(line):
            break
        j += 1
    return chek_kit(line)

def diaginal_1(d1):
    for i in range(len(d1)):
        line = []
        while i < len(d1):
            line.append(d1[i])
            i += size
        if chek_kit(line):
            break
    return chek_kit(line)

def diaginal_2(d2):
    for i in range(len(main_line)-2, 0, -1):
        line = []
        while i >= 0:
            line.append(main_line[i])
            i = i - size +2
        if chek_kit(line):
            break
    return chek_kit(line)


def main_field(f):
    field = f.copy()
    for i in range(size):
        field.pop(i)
        i += size
    for i in range(1, size):
        i = i*10
        field.pop(i)
    line = list(field.values())
    return line


def chek_kit(k):
    kit = (''.join(k)).strip(' ')
    win = None
    if kit.find('OOO') >= 0:
        win = 2
    if kit.find('XXX') >= 0:
        win = 1
    return win


print(f'Правила: 1. Размер поля - высота и ширина в клетках.\n'
      f'         2. Для хода нужно без пробела вводить две цифры:\n'
      f'            первая - номер строки, вторая - столбца\n'
      f'         3. Первый ход выполняет "Х"\n'
      f'             УДАЧИ !!!')
N = input('Ведите размер поля (от 3 до 9): ')
while not (N.isdigit() and (3 <= int(N) <= 9)):
    N = input('Повторите ввод размера поля (от 3 до 9): ')
N = int(N)
size = N + 1
field = nums_field(keys)

button = None
count = 0

while button != 0:
    show_field(field)
    main_line = main_field(field)
    winner = victory()
    
    if winner > 0:
        if winner == 1:
            favorite = 'Игра окончена!! Победил, "X". Поздравляю!!'
        elif winner == 2:
            favorite = 'Игра окончена!! Победил, "0". Поздравляю!!'
        print(favorite)
        button = 0
   
    button = int(step())
    if count % 2:
        mark = 'O'
    else:
        mark = 'X'
    count += 1
        
    field[button] = mark

    
 


