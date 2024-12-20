import tkinter as tk

# Глобальные переменные для состояния
current_value = 0  # Текущее число
current_operation = None  # Текущая операция (например, "+", "-", и т.д.)
new_number = True  # Флаг для определения, когда начинать ввод нового числа


def calculate():
    """Выполняет текущую операцию."""
    global current_value, current_operation
    try:
        if current_operation == "+":
            current_value += float(entry_var.get())
        elif current_operation == "-":
            current_value -= float(entry_var.get())
        elif current_operation == "×":
            current_value *= float(entry_var.get())
        elif current_operation == "÷":
            if float(entry_var.get()) != 0:
                current_value /= float(entry_var.get())
            else:
                entry_var.set("Деление на 0")
                return
        entry_var.set(str(current_value))
    except ValueError:
        entry_var.set("Ошибка")


def press(key):
    """Обработка нажатия кнопок."""
    global current_value, current_operation, new_number

    if key == "C":
        # Сброс всех значений
        current_value = 0
        current_operation = None
        new_number = True
        entry_var.set("")
        operator_var.set("")
    elif key in "+-×÷":
        # Если уже есть операция, вычисляем текущий результат
        if current_operation and not new_number:
            calculate()
        else:
            current_value = float(entry_var.get())

        # Устанавливаем новую операцию
        current_operation = key
        operator_var.set(f"Текущая операция: {key}")
        new_number = True
    elif key == "=":
        # Выполняем вычисление и сбрасываем операцию
        if current_operation:
            calculate()
            current_operation = None
            operator_var.set("")
        new_number = True
    else:
        # Набираем числа (очищаем поле ввода, если это начало нового числа)
        if new_number:
            entry_var.set("")
            new_number = False
        entry_var.set(entry_var.get() + key)


# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x450")

# Поле ввода
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Отображение текущей операции
operator_var = tk.StringVar()
operator_label = tk.Label(root, textvariable=operator_var, font=("Arial", 12), anchor="e")
operator_label.grid(row=1, column=0, columnspan=4, sticky="nsew")

# Кнопки калькулятора
buttons = [
    ("7", "lightgray"), ("8", "lightgray"), ("9", "lightgray"), ("÷", "orange"),
    ("4", "lightgray"), ("5", "lightgray"), ("6", "lightgray"), ("×", "orange"),
    ("1", "lightgray"), ("2", "lightgray"), ("3", "lightgray"), ("-", "orange"),
    ("C", "red"), ("0", "lightgray"), ("=", "green"), ("+", "orange")
]

for i, (btn, color) in enumerate(buttons):
    action = lambda key=btn: press(key)
    tk.Button(
        root, text=btn, command=action, font=("Arial", 18), bg=color, fg="white"
    ).grid(row=2 + i // 4, column=i % 4, sticky="nsew")

# Настраиваем сетку
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()