# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Last character in {word} is {word[-1]}')

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f"Count of \"а\" character in {word} is {word.lower().count('а')}")


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'е']
vowels_count = len([letter for letter in word if letter.lower() in 'ае'])
print(f'Vowels count in {word} is {vowels_count}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'Words count in sentence "{sentence}" is {len(sentence.split())}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
first_letters = [word[0] for word in sentence.split()]
for letter in first_letters:
    print(letter)

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = [word for word in sentence.split()]
total_letters = 0
for word in words:
    total_letters += len(word)
average_letters = total_letters / len(words)
print(round(average_letters))