from num2words import num2words
day_1 = 12.0
day_2 = 15.0
day_3 = 10.0
day_4 = 13.0
day_5 = 12.5
day_6 = 11.0
day_7 = 14.0
avg = round((day_1 + day_2 + day_3 +day_4 + day_5 + day_6 + day_7) / 7, 2)

words_en = num2words(avg, lang ='en', to = 'currency', currency = 'USD' )
words_ru = num2words(avg, lang ='ru', to = 'currency', currency = 'USD' )

print(f"O'rtacha harajatlar: ${avg} ({words_en}, {words_ru})")