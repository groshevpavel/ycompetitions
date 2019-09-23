# https://ru.wikipedia.org/wiki/Палиндром
#
# алгоритм учитывает набор символов, которые НЕ принимают участия в решении что строка палиндром

pol = ["Я иду с мечем судия", 'Sum summus mus ']
pol += """Кони топот инок
Но не речь, а черен он.
Идем, молод, долом меди.
Чин зван мечем навзничь.
Голод, чем меч долог? """.splitlines()

print(pol)

# символы которые будут пропущены и НЕ примут участия в решении что строка палиндром
skippers=[' ', "'", ",", ".", "\n", "?", "ь"]

def is_pol(s:str, skippers=skippers)->float:
    i, len_s = 0, len(s)
    inc_left, inc_right = 0, 0

    while True: # решил что while True в данном случае корректнее, потому что условие while i<len_s и так никогда не выполнится :/
        left, right = i + inc_left, (len_s - 1) - i - inc_right

        left_s, right_s = s[left].lower(), s[right].lower()

        while left_s in skippers:
            inc_left += 1
            left = i + inc_left
            left_s = s[left].lower()

        while right_s in skippers:
            inc_right += 1
            right = (len_s - 1) - i - inc_right
            right_s = s[right].lower()


        if left_s != right_s:
            print(s[left].lower() , s[right].lower(), i, left, right, len_s)
            return False
        else:
            i += 1

        if left >= right:
            return True


print([is_pol(p) for p in pol])

# Результат работы
# ['Я иду с мечем судия', 'Sum summus mus ', 'Кони топот инок', 'Но не речь, а черен он.', 'Идем, молод, долом меди.', 'Чин зван мечем навзничь.', 'Голод, чем меч долог? ']
# [True, True, True, True, True, True, True]

