# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.


istr = "a a a b c a a d c d d"
strlist = istr.split()
sdict = {}
for s in strlist:
    if s in sdict: 
        print(f"{s}_{sdict[s]}", end=' ')
    else:
        sdict[s] = 0
print(s, end=' ')
