import json

with open('todos.json', 'r') as f:
    todos_data_from_file = json.load(f)

for index, todo in enumerate(todos_data_from_file):
    with open(f'todo_{index + 1}.json', 'w') as f:
        json.dump(todo, f, indent=4)
    print(f"Данные задачи {index + 1} сохранены в файл todo_{index + 1}.json")
