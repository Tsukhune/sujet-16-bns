from exercices.exercice1 import *

def test_moyenne_un():
    assert moyenne([1.0]) == 1.0

def test_moyenne_trois():
    assert moyenne([1.0, 2.0, 4.0]) == 2.3333333333333335 