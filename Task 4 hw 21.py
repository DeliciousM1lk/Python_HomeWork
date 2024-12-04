car_brands = ('Toyota', 'Ford', 'Porsche', 'Ford', 'Honda', 'Ford', 'Chevrolet')
print(car_brands)
brand_to_replace = input("Введите название производителя: ").capitalize()
replacement_word = input("Введите слово для замены: ").capitalize()

modified_brands = tuple(replacement_word if brand == brand_to_replace else brand for brand in car_brands)

print("Обновленный кортеж:", modified_brands)
