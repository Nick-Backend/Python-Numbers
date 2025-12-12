from num2words import num2words

masofa = float(input("Masofani kiriting: "))
boshlangich = 5.00
km = 0.80
result = round(masofa * km + boshlangich, 2)

words_en = num2words(result, lang = 'en', currency = 'USD',to= 'currency')
words_ru = num2words(result, lang = 'ru', currency = 'USD', to= 'currency')

print("Yetkazib berish narxi: ${} ({}, {})".format(result, words_en, words_ru))

