import tkinter as tk
import operator

# Словарь операций
operations = {
 "+": operator.add,
 "-": operator.sub,
 "×": operator.mul,
 "÷": operator.truediv
}

def calculate(expression):
 """Обрабатывает математическое выражение без eval."""
 try:
 tokens = expression.split()
 if len(tokens) < 3:
 return "Ошибка"
 
 left = float(tokens[0])
 op = tokens[1]
 right = float(tokens[2])
 
 if op in operations:
 return operations[op](left, right)
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
 entry_var.set(entry_var.get() + (" " if key in operations else "") + key + (" " if key in operations else ""))

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