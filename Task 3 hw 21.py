fruits_tuple = ('яблоко', 'банан', 'апельсин', 'яблоко', 'груша', 'банан', 'вишня', 'яблоко', 'bananamango', 'strawberry-banana')
fruit_name = input("Введите название фрукта: ")

count = sum(fruit_name in fruit for fruit in fruits_tuple)

print(f"Фрукт '{fruit_name}' встречается в кортеже как часть элемента {count} раз(а).")