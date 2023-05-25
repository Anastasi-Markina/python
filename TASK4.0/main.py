# vowels = 'уеыаоэяиюё'
# phrases = input().split()
# counters = [sum([phrase.count(letter) for letter in vowels]) for phrase in phrases]
# rhythm = True
# max_counter = max(counters)
# for counter in counters:
#     if counter != max_counter:
#         rhythm = False
# print('Парам пам-пам' if rhythm else 'Пам парам')

vowels = 'уеыаоэяиюё'
phrases = input().split()
counters = list(map(lambda phrase: sum(map(lambda letter: phrase.count(letter), vowels)), phrases))
rhythm = True
max_counter = max(counters)
for counter in counters:
    if counter != max_counter:
        rhythm = False
print('Парам пам-пам' if rhythm else 'Пам парам')