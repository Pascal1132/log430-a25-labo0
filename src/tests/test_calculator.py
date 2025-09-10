"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator
my_calculator = Calculator()

def test_app():
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
    assert my_calculator.addition(2, 3) == 5
