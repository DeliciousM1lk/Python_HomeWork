# Task 1
Login = input("Введите логин >>>")
Password = input("Введите пароль >>>")
if Login == "user" and Password == "qwerty":
    print("Authentication completed")
else:
    print("Invalid login or password")

# Task 2
USD = 420
EUR = 510
RUB = 5.8
try:
    inputed_ammount =float(input("Insert ammount in KZT >>> "))
    currency_choice = int(input(
"""Choose currency:
[1] USD
[2] EUR
[3] RUB
>>>>>>>>> """))
    if currency_choice == 1:
        converted_amount = inputed_ammount / USD
        print(f"{converted_amount:.2f} USD")
    if currency_choice == 2:
        converted_amount = inputed_ammount / EUR
        print(f"{converted_amount:.2f} EUR")
    if currency_choice == 3:
        converted_amount = inputed_ammount / RUB
        print(f"{converted_amount:.2f} RUB")
except ValueError:
    print("Use numbers only!")
