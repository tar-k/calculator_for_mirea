import pytest
import tkinter as tk
from calculator import Calculator

@pytest.fixture
def calc():
    # Create a TK root and a calculator instance
    root = tk.Tk()
    calculator = Calculator(root)
    # We don't necessarily run mainloop for logic tests
    return calculator

@pytest.mark.parametrize("numbers", [(["1"]),(["1","2"]),(["5","9","0"])])
def test_press_digit(calc, numbers):
    expected_str = ''
    for i in numbers:
        expected_str+=i
        calc.press(i)
    
    assert calc.entry_var.get() == expected_str


def test_clear_entry(calc):
    calc.press('1')
    calc.press('2')
    calc.press('3')
    calc.press('CE')
    assert calc.entry_var.get() == '0'


def test_press_clear(calc):
    calc.press('1')
    calc.press('+')
    calc.press('2')
    calc.press('C')  # Reset everything
    assert calc.entry_var.get() == '0'
    assert calc.current_operation is None

@pytest.mark.parametrize("a,b, expected_result", [("1","1","2.0")])
def test_addition(calc, a, b, expected_result):
    calc.press(a)
    calc.press("+")
    calc.press(b)
    calc.press("=")
    assert calc.entry_var.get() == expected_result

@pytest.mark.parametrize("a,b, expected_result", [("1","1","0.0")])
def test_subtraction(calc, a, b, expected_result):
    calc.press(a)
    calc.press("-")
    calc.press(b)
    calc.press("=")
    assert calc.entry_var.get() == expected_result

@pytest.mark.parametrize("a,b, expected_result", [("2","3","6.0")])
def test_multiplication(calc, a, b, expected_result):
    # 5 × 5 =
    calc.press(a)
    calc.press("\u00d7")
    calc.press(b)
    calc.press("=")
    assert calc.entry_var.get() == expected_result

@pytest.mark.parametrize("a,b, expected_result", [("6","2","3.0"), ("9","0","Деление на 0")])
def test_division(calc, a, b, expected_result):
    
    calc.press(a)
    calc.press('\u00f7')  # Division symbol
    calc.press(b)
    calc.press("=")
    assert calc.entry_var.get() == expected_result

@pytest.mark.parametrize("a, expected_result", [("3","9.0"),("-3","9.0")])
def test_square_function(calc, a, expected_result):
    calc.entry_var.set(a)
    calc.press('x²')
    assert calc.entry_var.get() == expected_result

@pytest.mark.parametrize("a, expected_result", [("9","3.0")])
def test_square_root_function(calc, a, expected_result):
    calc.press(a)
    calc.press('\u221a')
    assert calc.entry_var.get() == expected_result

@pytest.mark.parametrize("a, expected_result", [("2","0.5"),("0","Деление на 0")])
def test_one_over_x(calc, a, expected_result):
    calc.press(a)
    calc.press('1/x')
    assert calc.entry_var.get() == expected_result

def test_percentage(calc):
    calc.press('5')
    calc.press('0')
    calc.press('%')
    assert calc.entry_var.get() == '0.5'

def test_change_sign(calc):
    calc.press('5')
    calc.press('\u00b1')
    assert calc.entry_var.get() == '-5.0'

def test_backspace(calc):
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

def test_calculate_method_invalid_number(calc):
    # Set entry to something invalid
    calc.entry_var.set('abc')
    calc.current_operation = '+'
    calc.current_value = 5
    calc.calculate()
    assert calc.entry_var.get() == 'Ошибка'
