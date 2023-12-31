# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

# Вариант 1

# song_list = "пара-ра-рам рам-пам-папам па-ра-па-да".split()
# test_list = "уеэоаыиюя"
# for string in song_list:      

    # count = 0
    # for letter in string:
    #     if letter in test_list:
    #         count += 1
    # result.add(count)

# print('Парам пам-пам' if len(result) == 1 else 'Пам парам')            


# Вариант 2

# song = "пара-ра-рам рам-пам-папам па-ра-па-па па-па-ра-па" 
# test_list = "уеэоаыиюя"

# result = set()
# count = lambda x: sum(1 for letter in x if letter in test_list)

# for string in song.split():
#     result.add(count(string))

# print('Парам пам-пам' if len(result) == 1 else 'Пам парам')




#Ваиант 3

# song_list = "пара-ра-рам рам-пам-папам па-ра-па-па".split()
# test_list = "уеэоаыиюя"
# result = set()

# for i in song_list:
#     result.add(sum(list(map(lambda x: sum(1 for letter in x if letter in test_list), i))))
    
# print('Парам пам-пам' if len(result) == 1 else 'Пам парам')  



#Вариант 4 HARDCORE

print('Парам пам-пам' if len({(sum(list(map(lambda x: sum(1 for letter in x if letter in "уеэоаыиюя"), i)))) for i in "пара-ра-рам рам-пам-папам па-ра-па-па".split()}) == 1 else 'Пам парам')