"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(1, 2) == 3
    assert my_calculator.addition(1, -2) == -1
    assert my_calculator.last_result == -1

def test_subtraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(3, 1) == 2
    assert my_calculator.subtraction(2, 5) == -3
    assert my_calculator.last_result == -3

def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(1, 2) == 2
    assert my_calculator.multiplication(7, 8) == 56
    assert my_calculator.last_result == 56

def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(1, 2) == 0.5
    assert my_calculator.division(4, 2) == 2
    assert my_calculator.division(4, -2) == -2
    assert my_calculator.last_result == -2
    assert my_calculator.division(4, 0) == "Erreur : division par zéro"
    assert my_calculator.last_result == "Error"