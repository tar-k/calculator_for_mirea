import tkinter as tk

def calculate(expression):
    """Обрабатывает математическое выражение вручную."""
    try:
        tokens = expression.split()
        if len(tokens) < 3:
            return "Ошибка"

        left = float(tokens[0])
        op = tokens[1]
        right = float(tokens[2])

        if op == "+":
            return left + right
        elif op == "-":
            return left - right
        elif op == "×":
            return left * right
        elif op == "÷":
            if right != 0:
                return left / right
            else:
                return "Деление на 0"
        else:
            return "Ошибка"
    except Exception:
        return "Ошибка"

def press(key):
    """Обработка нажатия кнопок."""
    if key == "C":
        entry_var.set("")
    elif key == "=":
        result = calculate(entry_var.get())
        entry_var.set(result)
    else:
        entry_var.set(entry_var.get() + (" " if key in "+-×÷" else "") + key + (" " if key in "+-×÷" else ""))

# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Кнопки калькулятора
buttons = [
    ("7", "lightgray"), ("8", "lightgray"), ("9", "lightgray"), ("÷", "orange"),
    ("4", "lightgray"), ("5", "lightgray"), ("6", "lightgray"), ("×", "orange"),
    ("1", "lightgray"), ("2", "lightgray"), ("3", "lightgray"), ("-", "orange"),
    ("C", "red"),       ("0", "lightgray"), ("=", "green"),    ("+", "orange")
]

for i, (btn, color) in enumerate(buttons):
    action = lambda key=btn: press(key)
    tk.Button(
        root, text=btn, command=action, font=("Arial", 18), bg=color, fg="white"
    ).grid(row=1 + i // 4, column=i % 4, sticky="nsew")

# Настраиваем сетку
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()