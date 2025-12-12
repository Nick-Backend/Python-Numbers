from num2words import num2words

price = int(input("Pul miqdorini kiriting ($): "))

dollar = 186
dollar_50 = 186 // 50 
dollar_10 = (186 % 50) //10
dollar_5 = (186 % 50) % 10 % 5
dollar_1 = (186 % 50) % 10 % 5

words_en = num2words(dollar, lang='en')
words_ru = num2words(dollar, lang='ru')

resault = (f"$50 kupyuradan: {dollar_50} ta\n"
           f"$10 kupyuradan: {dollar_10} ta\n"
           f"$5 kupyuradan: {dollar_5} ta\n"
           f"$1 kupyuradan: {dollar_1} ta\n"
           f"Umumiy summa: ${dollar} {words_en, words_ru}")

print(resault)
