"""
Этот код решает задачу о минимальной сумме, которую нужно заплатить при акции
"""
def min_cost_with_discount(prices):
    """
    Эта функция принимает список цен товаров и вычисляет минимальную сумму денег.
    """
    prices.sort(reverse=True)
    total_cost = sum(prices[i] for i in range(len(prices)) if (i + 1) % 3 != 0)
    return total_cost

if __name__ == "__main__":
    n = int(input("Введите количество товаров: "))
    price_list = list(map(int, input("Введите стоимости товаров через пробел: ").split()))
    print(min_cost_with_discount(price_list))
