import tkinter as tk


def press(key):
    if key == "C":
        entry_var.set("")
    elif key == "=":
        try:
            expression = entry_var.get().replace("÷", "/").replace("×", "*")
            result = eval(expression)  # Выполняем расчет
            entry_var.set(result)
        except Exception:
            entry_var.set("Ошибка")
    else:
        entry_var.set(entry_var.get() + key)


# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    "7", "8", "9", "÷",
    "4", "5", "6", "×",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

for i, btn in enumerate(buttons):
    action = lambda key=btn: press(key)
    tk.Button(root, text=btn, command=action, font=("Arial", 18)).grid(row=1 + i // 4, column=i % 4, sticky="nsew")

# Настраиваем сетку
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
