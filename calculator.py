import tkinter as tk

current_value = 0  # Текущее число
current_operation = None
new_number = True  # Флаг для определения, когда начинать ввод нового числа


def calculate():
    global current_value, current_operation
    try:
        if current_operation == "+":
            current_value += float(entry_var.get())
        elif current_operation == "-":
            current_value -= float(entry_var.get())
        elif current_operation == "\u00d7":
            current_value *= float(entry_var.get())
        elif current_operation == "\u00f7":
            if float(entry_var.get()) != 0:
                current_value /= float(entry_var.get())
            else:
                entry_var.set("Деление на 0")
                return
        entry_var.set(str(current_value))
    except ValueError:
        entry_var.set("Ошибка")


def press(key):
    global current_value, current_operation, new_number

    if key == "C":
        current_value = 0
        current_operation = None
        new_number = True
        entry_var.set("0")
        operator_var.set("")
    elif key == "CE":
        entry_var.set("0")
    elif key in "+-\u00d7\u00f7":
        if current_operation and not new_number:
            calculate()
        else:
            current_value = float(entry_var.get())

        current_operation = key
        operator_var.set(f"Текущая операция: {key}")
        new_number = True
    elif key == "1/x":
        try:
            result = 1 / float(entry_var.get())
            entry_var.set(str(result))
        except ValueError:
            entry_var.set("Ошибка")
        except ZeroDivisionError:
            entry_var.set("Деление на 0")
    elif key == "<-":
        if len(entry_var.get()) == 1:
            entry_var.set("0")
        else:
            entry_var.set(entry_var.get()[:-1])
    elif key == "=":
        if current_operation:
            calculate()
            current_operation = None
            operator_var.set("")
        new_number = True
    elif key == "\u221a":  # Корень
        try:
            result = float(entry_var.get()) ** 0.5
            entry_var.set(str(result))
        except ValueError:
            entry_var.set("Ошибка")
    elif key == "x²":  # Квадрат
        try:
            result = float(entry_var.get()) ** 2
            entry_var.set(str(result))
        except ValueError:
            entry_var.set("Ошибка")
    elif key == "%":  # Процент
        try:
            result = float(entry_var.get()) / 100
            entry_var.set(str(result))
        except ValueError:
            entry_var.set("Ошибка")
    elif key == "\u00b1":  # Смена знака
        try:
            result = -float(entry_var.get())
            entry_var.set(str(result))
        except ValueError:
            entry_var.set("Ошибка")
    else:
        if new_number:
            entry_var.set("0")
            new_number = False
        if key == ",":
            if "." not in entry_var.get():
                entry_var.set(entry_var.get() + ".")
        else:
            if entry_var.get() == '0':
                entry_var.set(key)
            else:
                entry_var.set(entry_var.get() + key)


root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x450")

entry_var = tk.StringVar(value="0")
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

operator_var = tk.StringVar()
operator_label = tk.Label(root, textvariable=operator_var, font=("Arial", 12), anchor="e")
operator_label.grid(row=1, column=0, columnspan=4, sticky="nsew")

buttons = [
    ("%", "lightblue"), ("CE", "lightblue"), ("C", "lightblue"), ("<-", "lightblue"),
    ("1/x", "lightblue"), ("x²", "lightblue"), ("\u221a", "lightblue"), ("\u00f7", "lightblue"),
    ("1", "lightgray"), ("2", "lightgray"), ("3", "lightgray"), ("\u00d7", "lightblue"),
    ("4", "lightgray"), ("5", "lightgray"), ("6", "lightgray"), ("+", "lightblue"),
    ("7", "lightgray"), ("8", "lightgray"), ("9", "lightgray"), ("-", "lightblue"),
    ("\u00b1", "lightblue"), ("0", "lightgray"), (",", "lightblue"), ("=", "blue")
]

for i, (btn, color) in enumerate(buttons):
    action = lambda key=btn: press(key)
    tk.Button(
        root, text=btn, command=action, font=("Arial", 18), bg=color, fg="black"
    ).grid(row=2 + i // 4, column=i % 4, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
