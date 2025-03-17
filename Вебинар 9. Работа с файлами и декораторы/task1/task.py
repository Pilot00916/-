
# Открываю файл чтобы прочитать его
with open("test_file/task1_data.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Удаляю цифры согласно вводным
cleaned_text = ''.join([char for char in text if not char.isdigit()])

# Создаю новый файл и записываю туда итог
with open("test_file/task1_answer.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)

