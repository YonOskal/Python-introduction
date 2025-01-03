# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, 
# если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

# Пример
# На входе:

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# На выходе:

# Парам пам-пам

def check_rhythm(str):
    # Определяем гласные
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    
    # Разделяем строки на фразы
    phrases = str.replace('-','').split()

    # Проверяем количество фраз
    if len(phrases) < 2:
        return "Количество фраз должно быть больше одной!"
    
    # Подсчитываем количество гласных в каждой фразе
    vowel_counts = []
    count = 0
    for phrase in phrases:
        for char in phrase:
            if char in vowels:
                count += 1
        vowel_counts.append(count)
        count = 0


    # Проверяем, все ли значения одинаковы
    if all(x == vowel_counts[0] for x in vowel_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"

# Пример использования
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
print(check_rhythm(stroka))
