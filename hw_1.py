import tkinter as tk
from tkinter import ttk
import requests


def fetch_data():
    user_id = id_entry.get()

    if not user_id.isdigit():
        result_label.config(text="Ошибка: ID должен быть числом.", fg="red")
        return

    url = f"https://jsonplaceholder.typicode.com/posts/{user_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        save_to_file(data)

        result_label.config(text=f"Title: {data['title']}\n\nBody: {data['body']}", fg="black")
    except requests.exceptions.HTTPError as http_err:
        result_label.config(text=f"HTTP ошибка: {http_err}", fg="red")
    except Exception as err:
        result_label.config(text=f"Ошибка: {err}", fg="red")


def save_to_file(data):
    try:
        with open("result.txt", "w", encoding="utf-8") as file:
            file.write(f"ID: {data['id']}\n")
            file.write(f"Title: {data['title']}\n")
            file.write(f"Body: {data['body']}\n")
        result_label.config(text=result_label.cget("text") + "\nДанные сохранены в result.txt", fg="black")
    except Exception as e:
        result_label.config(text=f"Ошибка при сохранении файла: {e}", fg="red")


def main():
    root = tk.Tk()
    root.title("JSONPlaceholder Fetcher")
    root.geometry("500x400")

    title_label = tk.Label(root, text="JSONPlaceholder Fetcher", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    id_frame = tk.Frame(root)
    id_frame.pack(pady=10)

    id_label = tk.Label(id_frame, text="Введите ID:", font=("Arial", 12))
    id_label.pack(side=tk.LEFT, padx=5)

    global id_entry
    id_entry = ttk.Entry(id_frame, font=("Arial", 12), width=15)
    id_entry.pack(side=tk.LEFT, padx=5)

    fetch_button = ttk.Button(id_frame, text="Получить данные", command=fetch_data)
    fetch_button.pack(side=tk.LEFT, padx=5)

    global result_label
    result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=450, justify="left", anchor="w")
    result_label.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
