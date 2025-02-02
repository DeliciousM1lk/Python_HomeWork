import sys
import os
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt6.QtCore import QUrl, QIODevice


class JSONFetcherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.handle_response)

    def init_ui(self):
        self.setWindowTitle("JSONPlaceholder Fetcher")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Нажмите кнопку для запроса данных")
        layout.addWidget(self.label)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)

        self.button = QPushButton("Запросить данные")
        self.button.clicked.connect(self.fetch_data)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def fetch_data(self):
        url = QUrl("https://jsonplaceholder.typicode.com/posts")
        request = QNetworkRequest(url)
        self.manager.get(request)
        self.label.setText("Ожидание ответа...")

    def handle_response(self, reply):
        if reply.error():
            self.text_edit.setText(f"Ошибка запроса: {reply.errorString()}")
            return

        data = reply.readAll().data().decode("utf-8")
        json_data = json.loads(data)

        self.text_edit.setText(json.dumps(json_data, indent=4, ensure_ascii=False))
        self.label.setText("Данные получены и сохранены!")

        self.save_json(json_data)

    def save_json(self, json_data):
        save_dir = "json_data"
        os.makedirs(save_dir, exist_ok=True)

        file_path = os.path.join(save_dir, "posts.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

        print(f"Файл сохранён: {file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JSONFetcherApp()
    window.show()
    sys.exit(app.exec())
