import pytest
import tkinter as tk
from unittest.mock import MagicMock
from calculator import Calculator  # Replace with the correct import if needed

@pytest.fixture
def calc():
    # Create a TK root and a calculator instance
    root = tk.Tk()
    calculator = Calculator(root)
    # We don't necessarily run mainloop for logic tests
    return calculator

def test_press_single_digit(calc):
    # Press '1'
    calc.press('1')
    assert calc.entry_var.get() == '1'

def test_press_multiple_digits(calc):
    # Press '1', then '2', should show '12'
    calc.press('1')
    calc.press('2')
    assert calc.entry_var.get() == '12'

def test_press_clear(calc):
    calc.press('1')
    calc.press('+')
    calc.press('2')
    calc.press('C')  # Reset everything
    assert calc.entry_var.get() == '0'
    assert calc.current_operation is None

def test_simple_addition(calc):
    # 12 + 3 =
    calc.press('1')
    calc.press('2')
    calc.press('+')
    calc.press('3')
    calc.press('=')
    assert calc.entry_var.get() == '15.0'

def test_simple_subtraction(calc):
    # 10 - 5 =
    calc.press('1')
    calc.press('0')
    calc.press('-')
    calc.press('5')
    calc.press('=')
    assert calc.entry_var.get() == '5.0'

def test_simple_multiplication(calc):
    # 5 × 5 =
    calc.press('5')
    calc.press('\u00d7')  # Multiplication symbol
    calc.press('5')
    calc.press('=')
    assert calc.entry_var.get() == '25.0'

def test_simple_division(calc):
    # 10 ÷ 2 =
    calc.press('1')
    calc.press('0')
    calc.press('\u00f7')  # Division symbol
    calc.press('2')
    calc.press('=')
    assert calc.entry_var.get() == '5.0'

def test_division_by_zero(calc):
    # 5 ÷ 0 =
    calc.press('5')
    calc.press('\u00f7')
    calc.press('0')
    calc.press('=')
    assert calc.entry_var.get() == 'Деление на 0'

def test_clear_entry(calc):
    # Press digits, then CE
    calc.press('1')
    calc.press('2')
    calc.press('3')
    calc.press('CE')
    assert calc.entry_var.get() == '0'

def test_square_function(calc):
    # Press '4', then x² should be 16
    calc.press('4')
    calc.press('x²')
    assert calc.entry_var.get() == '16.0'

def test_square_root_function(calc):
    # Press '9', then √ should be 3
    calc.press('9')
    calc.press('\u221a')
    assert calc.entry_var.get() == '3.0'

def test_one_over_x(calc):
    # Press '2', then 1/x should be 0.5
    calc.press('2')
    calc.press('1/x')
    assert calc.entry_var.get() == '0.5'

def test_percentage(calc):
    # Press '50', then '%' should be 0.5
    calc.press('5')
    calc.press('0')
    calc.press('%')
    assert calc.entry_var.get() == '0.5'

def test_change_sign(calc):
    # Press '5', then ± should be -5
    calc.press('5')
    calc.press('\u00b1')
    assert calc.entry_var.get() == '-5.0'

def test_backspace(calc):
    # Press '1', '2', '3', then '<-' should remove the last digit to '12'
    calc.press('1')
    calc.press('2')
    calc.press('3')
    calc.press('<-')
    assert calc.entry_var.get() == '12'

def test_decimal_point(calc):
    # Press '5', ',', '5' should result in '5.5'
    calc.press('5')
    calc.press(',')
    calc.press('5')
    assert calc.entry_var.get() == '5.5'

def test_chained_operations(calc):
    # 2 + 3 + 4 =
    calc.press('2')
    calc.press('+')
    calc.press('3')
    calc.press('+')
    calc.press('4')
    calc.press('=')
    assert calc.entry_var.get() == '9.0'

def test_calculate_method_directly(calc):
    # Directly test calculate function
    calc.entry_var.set('10')
    calc.current_value = 5
    calc.current_operation = '+'
    calc.calculate()
    # After calculation: 5 + 10 = 15
    assert calc.entry_var.get() == '15.0'

def test_calculate_method_invalid_number(calc):
    # Set entry to something invalid
    calc.entry_var.set('abc')
    calc.current_operation = '+'
    calc.current_value = 5
    calc.calculate()
    assert calc.entry_var.get() == 'Ошибка'
