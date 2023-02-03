from random import choice

words = {}
alphabet = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ж': 0, 'з': 0,
            'и': 0, 'й': 0, 'к': 0, 'л': 0, 'м':0, 'н':0, 'о': 0, 'п': 0, 'р': 0,
            'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0,
            'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0, 'я': 0}
fuck = [
    'Чего бля? Тогда', 'Сука! Тогда', 'Блять! Ну тогда',
    'Да блять! Пиши:', 'Ой. Ну тогда это точно', 'Я в ахуе. Пробуй'
       ]

with open('Words.txt', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        for i in line:
            alphabet[i] += 1
        words[line] = 0


def find_best_word(words, alphabet):
    for word in words:
        for i in word:
            words[word] += alphabet[i]/word.count(i)
        if words[word] == max(words.values()):
            best_word = word
    return best_word


def del_reds(words, take, best_word):
    for letter, result in zip(best_word, take):
        if result == 'r':
            words = {word: words[word] for word in words if not letter in word}
    return words


def del_yels(words, take, best_word):
    for letter, result, num in zip(best_word, take, range(len(best_word))):
        if result == 'y':
            words = {word: words[word] for word in words if letter in word and word[num] != letter}
    return words


def del_nogreens(words, take, best_word):
    for letter, result, num in zip(best_word, take, range(len(best_word))):
        if result == 'g':
            words = {word: words[word] for word in words if word[num] == letter}
    return words


best_word = find_best_word(words, alphabet)
print(f'Привет! Попробуй слово "{best_word}"')
take = input('Ввведи "g", если буква угадана верно; "y", если буква присутствует в слове; "r", если такой буквы нет \n')

while take != 'ggggg':
    try:
        words = del_reds(words, take, best_word)
        words = del_yels(words, take, best_word)
        words = del_nogreens(words, take, best_word)
        best_word = find_best_word(words, alphabet)
        print(f'{choice(fuck)} "{best_word}"')
        take = input()
    except ValueError:
        print('Дьявол! Это слово мне незнакомо... Что это было?\n')
        new_word = input()
        while len(new_word) != len(best_word):
            print('Я не верю, что такое слово вообще существует')
            new_word = input()
        with open ('Words.txt', 'a') as file:
            file.write('\n'+new_word.lower())
        take = 'ggggg'
        print('Вау! Буду иметь ввиду!\n')

print('Ещё увидимся!')
