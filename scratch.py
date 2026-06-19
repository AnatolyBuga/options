# Текстовый файл состоит из символов A, B, C, D и E.
# Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых комбинация символов AB
#  встречается ровно 50 раз.

# with open('24_13715.txt') as f:
#     content = f.readline()
# N = 50

# "AB123AB" # 7
# content = "AB123ABC" # 8
# "WAB123ABC" # 9

# 3
content ="ABAB123ABC" # 8 9 

# content = "FAB45.ABA39678AB.CAB" # 17
N = 2 
xxxxxxx = "FA B45.A-BA396-78AB.-CA B" # 17

# First Solution
abs_indexes = [] # 1, 6, 14 # len(abs_indexes) == count of ABs
abs_max = 0

for i in range(1, len(content)):

    c = content[i]

    if content[i-1:i+1] == 'AB':
        abs_indexes.append(i-1)
    
    chars = 0 # Placeholder, in case chars doesn't get defined below
    if len(abs_indexes) == N:
        chars = i+1
    elif len(abs_indexes) > N: # eg 3
        chars = i+1 - ( abs_indexes[-N-1] + 1 )
        
    abs_max = max(abs_max, chars)

print(abs_max)






# (И. Женецкий) Системный администратор Дамир обслуживает крупную корпорацию. 
# У него в текстовом файле находятся IP-адреса этих сотрудников.
#  Ему необходимо посчитать количество таких различных IP-адресов, которые удовлетворяют маске 195.2?.1?5.14,
# где символ ? обозначает цифру от 0 до 9. 
# Например, подходящие IP-адреса могут быть такими: 195.20.145.14, 195.24.185.14, 195.21.135.14 и т.д.
#  Определите количество различных подходящих IP-адресов в файле.

with open('24_3726.txt') as f:
    contents = f.readlines()

mask = "195.2?.1?5.14"
# Optional
# to_check = [] 
# for i, c in enumerate(mask):
#     if c == "?":
#         if not to_check and i != 0 :
#             to_check.append((0, i-1))
#         else:
#             to_check[-1][1] # last one of the previous

to_check = [(0,4), (5,None), (6, 7), (8,None), (9,12)]
accepted_chars = [str(i) for i in range(10)]
matches = set()

# Mini Example
# contents = ["195.21.135.14", "196.23.135.14", "195.20.105.14", "195.21.115.15"]
for ip in contents:
    
    for _from, _to in to_check:
        if _to is not None:
            a = ip[_from:_to+1]
            b = mask[_from:_to+1]
            if a == b:
                match=True
            else:
                match = False
                break
        else:
            match = ip[_from] in accepted_chars
            match2 = match
            if not match2:
                stop = True
            if not match: break

    if match:
        matches.add(ip)
        # print(ip)
        # match_count += 1
        
print(len(matches))


def is_odd(x):
    return bool(x%2)

count = 0
for i in range(1_000, 10_000):
    s = str(i)

    if len(set(s)) != 4:
        continue

    # if s == "9875":
    #     stop = True

    matches_criteria = True
    for j in range(1,4):
        previous = int(s[j-1])
        current = int(s[j])
        previous_is_odd  = is_odd(previous)
        current_is_odd   = is_odd(current)
        # Check
        if (previous_is_odd and current_is_odd) or (not current_is_odd and not previous_is_odd):
            matches_criteria = False
            break

    # print(s)
    if not matches_criteria:
        continue

    count += 1

print(count)

from itertools import *
alf = '0123456789'
k = 0
for i in permutations(alf, 4):
    s = ''.join(i)
    if s[0] != '0' and '13' not in s and '31' not in s and '15' not in s  and '51' not in s and '17' not in s and '71' not in s and '19' not in s and '91' not in s and '35' not in s and '53' not in s and '37' not in s and '73' not in s and '39' not in s and '93' not in s and '57' not in s  and '75' not in s and '59' not in s and '95' not in s and '79' not in s and '97' not in s and '02' not in s and '20' not in s and '04' not in s and '40' not in s and '06' not in s and '60' not in s and '08' not in s and '80' not in s and '24' not in s and '42' not in s and '26' not in s and '62' not in s and '28' not in s and '82' not in s and '46' not in s and '64' not in s and '48' not in s and '84' not in s and '68' not in s and '86' not in s:
        # print(s)
        k += 1
print("\n")
print(k)

