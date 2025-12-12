from num2words import num2words
oy_boshi = float(input("Oy boshidagi ko'rsatgich: "))
oy_oxiri = float(input("Oy oxiridagi ko'rsatgich: "))
narx_kWh = 0.45
result = round((oy_oxiri - oy_boshi) * 0.45 ,2)

words_en = num2words(result, lang = 'en')
words_ru = num2words(result, lang = 'ru')

print(f"To'lov: ${result} ({words_en}, {words_ru})")
