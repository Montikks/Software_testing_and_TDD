"""Matice a transpozice
Implementujte třídu Matrix, která umožňuje vytvořit matici z dvourozměrného seznamu a poskytuje metodu transpose(),
která vrátí transponovanou matici.
"""
import pytest
from p12_Exercise_matrix import Matrix


def test_matrix_creation():
    m = Matrix([[1, 2], [3, 4]])
    assert m.data == [[1, 2], [3, 4]]


def test_matrix_transpose():
    m = Matrix([[1, 2], [3, 4]])
    mt = m.transpose()
    assert mt.data == [[2, 4], [1, 3]]

    m2 = Matrix([[1, 2, 3], [4, 5, 6]])
    mt2 = m2.transpose()
    assert mt2.data == [[4, 5, 6], [1, 2, 3]]


if __name__ == "__main__":
    pytest.main()
