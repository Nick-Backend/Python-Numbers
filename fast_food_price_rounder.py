from num2words import num2words

taom1 = float(input("Mahsulot narxlarini kiriting: "))
taom2 = float(input("Mahsulot narxlarini kiriting: "))
taom3 = float(input("Mahsulot narxlarini kiriting: "))

total_price = round(taom1 + taom2 + taom3, 3)


words_en = num2words(
    total_price, 
    to='currency', 
    currency='USD'
)
words_ru = num2words(
    total_price, 
    lang='ru', 
    to='currency', 
    currency='USD'
)


print(f"Umumiy narx: ${total_price, words_en, words_ru}\n"
      f"Yaxlitlangan narx: ${total_price, words_en, words_ru}"
      )
