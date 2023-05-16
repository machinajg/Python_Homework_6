# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, 
# главное наличие последовательности букв), то холодильник заражен и нужно вывести номер
# холодильника, нумерация начинается с единицы
# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3

# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8

n = int(input('Введите количество холодильников: '))

virus = 'anton'
for i in range(1, n+1):
    s = input ('Введите название холодильника: ') 
    res = ''
    for j in virus:
        if j in s:
            res += j
            s = s[s.find(j):]
        
    if res == 'anton':
        print(i, end=' ')
        continue             


