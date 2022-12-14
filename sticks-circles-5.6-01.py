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
    

def victory(ML):
    if horizont(ML):
        win = horizont(ML)
    elif vertikal(ML):
        win = vertikal(ML)
    elif diaginal_1(ML):
        win = diaginal_1(ML)
    elif diaginal_2(ML):
        win = diaginal_2(ML)
    elif diaginal_3(ML):
        win = diaginal_3(ML)     
    elif diaginal_4(ML):
        win = diaginal_4(ML)
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
    for i in range(1, N-1):
        var = 0
        line = []
        j = i        
        while var <= N-1-i:
            line.append(d1[j])
            var += 1
            j += N+1
        if chek_kit(line):
            break
    return chek_kit(line)

def diaginal_3(d3):
    LL = len(d3)
    for i in range(LL-1, LL-N, -1):
        var = 0
        line = []
        j = i        
        while var <= N-LL+i:
            line.append(d3[j])
            var += 1
            j = j - N - 1
        if chek_kit(line):
            break
    return chek_kit(line)

def diaginal_2(d2):
    for i in range(1, N-1):
        var = 0
        line = []
        j = i        
        while var <= i:
            line.append(d2[j])
            var += 1
            j += N - 1
        if chek_kit(line):
            break
    return chek_kit(line)

def diaginal_4(d4):
    LL = len(d4)
    for i in range(LL-2, LL-N-1, -1):
        var = 0
        line = []
        j = i        
        while var <= LL-1-i:
            line.append(d4[j])
            var += 1
            j = j - N + 1
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
    if kit.find('O'*R) >= 0:
        win = 2
    if kit.find('X'*R) >= 0:
        win = 1 
    return win

def chek_winner():
    CW = victory(main_line)
    if CW == 2:
        winner = 2
    if CW == 1 and benefit == 0:
        winner = 3
    if CW == 1 and benefit == 1:
        winner = 1
    winner = CW
    return winner




print(f'Правила: 1. Размер поля - высота и ширина в клетках.\n'
      f'         2. Для хода нужно без пробела вводить две цифры:\n'
      f'            первая - номер строки, вторая - столбца.\n'
      f'         3. Если размер поля 3 или 4, игра идёт "до трёх",\n'
      f'            если 5 или 6, то "до 4", если более - "до 5".\n'
      f'         4. Первый ход выполняет "Х"\n'
      f'             УДАЧИ !!!')

N = input('Ведите размер поля (от 3 до 9): ')
while not (N.isdigit() and (3 <= int(N) <= 9)):
    N = input('Повторите ввод размера поля (от 3 до 9): ')
N = int(N)
size = N + 1
if N == 3 or N == 4:
    R = 3
elif N == 5 or N == 6:
    R = 4
else:
    R = 5
field = nums_field(keys)
button = None
count = 0
benefit = 0
while button != 0:
    show_field(field)
    main_line = main_field(field)
    winner = chek_winner()
   
    if winner > 0:
        if winner == 3:
            benefit = 1
            print('Внимание, у "O" последний ход...')
            mark = 'O'
            count += 1
        elif winner == 2 and benefit == 1:
            print('Игра окончена!! Ничья!!')
            button = 0
        elif winner == 1:
            favorite = 'Игра окончена!! Победил, "X". Поздравляю!!'
            print(favorite)
            button = 0
        elif winner == 2:
            favorite = 'Игра окончена!! Победил, "O". Поздравляю!!'
            print(favorite)
            button = 0

    button = int(step())
    if benefit == 0:
        if count % 2:
            mark = 'O'
        else:
            mark = 'X'
    count += 1
    field[button] = mark

    
