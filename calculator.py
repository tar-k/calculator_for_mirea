import tkinter as tk
# Некий комментарий
class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Калькулятор")
        self.master.geometry("300x450")

        # Calculator state
        self.current_value = 0
        self.current_operation = None
        self.new_number = True

        # Variables for display
        self.entry_var = tk.StringVar(value="0")
        self.operator_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry field
        entry = tk.Entry(self.master, textvariable=self.entry_var, font=("Arial", 20), justify="right")
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Operation label
        operator_label = tk.Label(self.master, textvariable=self.operator_var, font=("Arial", 12), anchor="e")
        operator_label.grid(row=1, column=0, columnspan=4, sticky="nsew")

        # Buttons configuration
        buttons = [
            ("%", "lightblue"), ("CE", "lightblue"), ("C", "lightblue"), ("<-", "lightblue"),
            ("1/x", "lightblue"), ("x²", "lightblue"), ("\u221a", "lightblue"), ("\u00f7", "lightblue"),
            ("1", "lightgray"), ("2", "lightgray"), ("3", "lightgray"), ("\u00d7", "lightblue"),
            ("4", "lightgray"), ("5", "lightgray"), ("6", "lightgray"), ("+", "lightblue"),
            ("7", "lightgray"), ("8", "lightgray"), ("9", "lightgray"), ("-", "lightblue"),
            ("\u00b1", "lightblue"), ("0", "lightgray"), (",", "lightblue"), ("=", "blue")
        ]

        # Create and place buttons
        for i, (btn, color) in enumerate(buttons):
            action = lambda key=btn: self.press(key)
            tk.Button(
                self.master, text=btn, command=action, font=("Arial", 18), bg=color, fg="black"
            ).grid(row=2 + i // 4, column=i % 4, sticky="nsew")

        # Configure grid resizing
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1)

    def calculate(self):
        """Perform the stored operation with the current input."""
        try:
            value = float(self.entry_var.get())
            if self.current_operation == "+":
                self.current_value += value
            elif self.current_operation == "-":
                self.current_value -= value
            elif self.current_operation == "\u00d7":
                self.current_value *= value
            elif self.current_operation == "\u00f7":
                if value != 0:
                    self.current_value /= value
                else:
                    self.entry_var.set("Деление на 0")
                    return

            self.entry_var.set(str(self.current_value))
        except ValueError:
            self.entry_var.set("Ошибка")

    def press(self, key):
        """Handle a button press."""
        if key == "C":
            # Reset everything
            self.current_value = 0
            self.current_operation = None
            self.new_number = True
            self.entry_var.set("0")
            self.operator_var.set("")
        elif key == "CE":
            # Clear only the entry
            self.entry_var.set("0")
        elif key in "+-\u00d7\u00f7":
            # If operation in progress and a new number not started, calculate first
            if self.current_operation and not self.new_number:
                self.calculate()
            else:
                self.current_value = float(self.entry_var.get())

            self.current_operation = key
            self.operator_var.set(f"Текущая операция: {key}")
            self.new_number = True
        elif key == "1/x":
            try:
                result = 1 / float(self.entry_var.get())
                self.entry_var.set(str(result))
            except ZeroDivisionError:
                self.entry_var.set("Деление на 0")
            except ValueError:
                self.entry_var.set("Ошибка")
        elif key == "<-":
            if len(self.entry_var.get()) == 1:
                self.entry_var.set("0")
            else:
                self.entry_var.set(self.entry_var.get()[:-1])
        elif key == "=":
            if self.current_operation:
                self.calculate()
                self.current_operation = None
                self.operator_var.set("")
            self.new_number = True
        elif key == "\u221a":  # Square root
            try:
                result = float(self.entry_var.get()) ** 0.5
                self.entry_var.set(str(result))
            except ValueError:
                self.entry_var.set("Ошибка")
        elif key == "x²":  # Square
            try:
                result = float(self.entry_var.get()) ** 2
                self.entry_var.set(str(result))
            except ValueError:
                self.entry_var.set("Ошибка")
        elif key == "%":  # Percentage
            try:
                result = float(self.entry_var.get()) / 100
                self.entry_var.set(str(result))
            except ValueError:
                self.entry_var.set("Ошибка")
        elif key == "\u00b1":  # Change sign
            try:
                result = -float(self.entry_var.get())
                self.entry_var.set(str(result))
            except ValueError:
                self.entry_var.set("Ошибка")
        else:
            # Digits or comma
            if self.new_number:
                self.entry_var.set("0")
                self.new_number = False
            if key == ",":
                if "." not in self.entry_var.get():
                    self.entry_var.set(self.entry_var.get() + ".")
            else:
                if self.entry_var.get() == '0':
                    self.entry_var.set(key)
                else:
                    self.entry_var.set(self.entry_var.get() + key)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
