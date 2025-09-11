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
    assert my_calculator.addition(2, 4) == 6

def test_subtraction():
    assert my_calculator.subtraction(10, 3) == 7
    assert my_calculator.last_result == 7

def test_multiplication():
    assert my_calculator.multiplication(3, 5) == 15
    assert my_calculator.last_result == 15

def test_division():
    assert my_calculator.division(10, 2) == 5
    assert my_calculator.last_result == 5

def test_division_by_zero():
    assert my_calculator.division(5, 0) == "Erreur : division par zéro"
    assert my_calculator.last_result == "Error"
