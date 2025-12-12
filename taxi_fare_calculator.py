from num2words import num2words
km = float(input("Masofani kiriting: "))
boshlangich = 3.00
km = km * 1.20
result = round(km + boshlangich, 2)

words_en = num2words(result, lang = 'en')
words_ru = num2words(result, lang = 'ru')

print("Taxi narxi: ${} ({}, {})".format(result,words_en,words_ru))