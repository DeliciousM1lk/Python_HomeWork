set_a = {1, 2, 3}
set_b = {1, 2}

if set_a == set_b:
    print("Множества равны")
elif set_a.issuperset(set_b):
    print(f"Объект {set_a} является чистым супермножеством")
else:
    print("Супермножество не обнаружено")
