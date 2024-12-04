fruits_tuple = ('яблоко', 'банан', 'апельсин', 'яблоко', 'груша', 'банан', 'вишня', 'яблоко')
fruit_name = input("Введите название фрукта: ")

count = fruits_tuple.count(fruit_name)

print(f"Фрукт '{fruit_name}' встречается в кортеже {count} раз(а).")

