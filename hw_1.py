import matplotlib.pyplot as plt
import numpy as np


def main():
    np.random.seed(42)
    data = {
        "Product": [f"Product {i}" for i in range(1, 11)],
        "Units Sold": np.random.randint(50, 500, size=10),
        "Price per Unit": np.random.uniform(5, 50, size=10),
    }

    total_revenue = [q * p for q, p in zip(data["Units Sold"], data["Price per Unit"])]

    mean_sales = np.mean(data["Units Sold"])
    median_sales = np.median(data["Units Sold"])
    max_sales = np.max(data["Units Sold"])
    min_sales = np.min(data["Units Sold"])

    mean_revenue = np.mean(total_revenue)
    total_revenue_sum = np.sum(total_revenue)

    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    axes[0].bar(data["Product"], data["Units Sold"], color="skyblue", label="Units Sold")
    axes[0].set_title("Units Sold by Product")
    axes[0].set_ylabel("Units")
    axes[0].legend()

    axes[1].bar(data["Product"], total_revenue, color="salmon", label="Total Revenue")
    axes[1].set_title("Total Revenue by Product")
    axes[1].set_ylabel("Revenue")
    axes[1].legend()

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    print(f"Mean Units Sold: {mean_sales}")
    print(f"Median Units Sold: {median_sales}")
    print(f"Max Units Sold: {max_sales}")
    print(f"Min Units Sold: {min_sales}")
    print(f"Mean Revenue: {mean_revenue}")
    print(f"Total Revenue: {total_revenue_sum}")


if __name__ == "__main__":
    main()
