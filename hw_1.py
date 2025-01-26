import tkinter as tk
from tkinter import ttk
import requests


class JSONPlaceholderFetcher:
    def __init__(self, root):
        self.root = root
        self.root.title("JSONPlaceholder Fetcher")
        self.root.geometry("500x400")
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="JSONPlaceholder Fetcher", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        id_frame = tk.Frame(self.root)
        id_frame.pack(pady=10)

        id_label = tk.Label(id_frame, text="Введите ID:", font=("Arial", 12))
        id_label.pack(side=tk.LEFT, padx=5)

        self.id_entry = ttk.Entry(id_frame, font=("Arial", 12), width=15)
        self.id_entry.pack(side=tk.LEFT, padx=5)

        fetch_button = ttk.Button(id_frame, text="Получить данные", command=self.fetch_data)
        fetch_button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(
            self.root, text="", font=("Arial", 12), wraplength=450, justify="left", anchor="w"
        )
        self.result_label.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

    def fetch_data(self):
        user_id = self.id_entry.get()

        if not user_id.isdigit():
            self.update_result_label("Ошибка: ID должен быть числом.", "red")
            return

        url = f"https://jsonplaceholder.typicode.com/posts/{user_id}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            self.save_to_file(data)

            self.update_result_label(
                f"Title: {data['title']}\n\nBody: {data['body']}", "black"
            )
        except requests.exceptions.HTTPError as http_err:
            self.update_result_label(f"HTTP ошибка: {http_err}", "red")
        except Exception as err:
            self.update_result_label(f"Ошибка: {err}", "red")

    def save_to_file(self, data):
        try:
            with open("result.txt", "w", encoding="utf-8") as file:
                file.write(f"ID: {data['id']}\n")
                file.write(f"Title: {data['title']}\n")
                file.write(f"Body: {data['body']}\n")

            current_text = self.result_label.cget("text")
            self.update_result_label(current_text + "\nДанные сохранены в result.txt", "black")
        except Exception as e:
            self.update_result_label(f"Ошибка при сохранении файла: {e}", "red")

    def update_result_label(self, text, color):
        self.result_label.config(text=text, fg=color)


def main():
    root = tk.Tk()
    app = JSONPlaceholderFetcher(root)
    root.mainloop()


if __name__ == "__main__":
    main()
