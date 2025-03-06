# # Test file for the sum function
import unittest
import pytest

from srcs.my_sum import sum
from srcs.auto import Args
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, Fraction(9, 10))

    def test_bad_type(self):
        data = "Hello"
        with self.assertRaises(TypeError):
            result = sum(data)
            return result


@pytest.mark.parametrize("num", [4, 2, 6, 44, 68, 96])
def test_is_div_two(num):
    assert Args.is_div_two(num) is True


@pytest.mark.parametrize("num", [3, 1, 5, 43, 67, 95])
@pytest.mark.xfail
def test_is_div_odd(num):
    assert Args.is_div_two(num) is False


@pytest.mark.parametrize("num", ["stirng", 'a', "56"])
@pytest.mark.xfail
def test_invalid_type(num):
    with pytest.raises(TypeError):
        Args.is_div_two(num)


def test_args():
    a = Args(10)
    b = Args(20)
    c = a
    assert a == c
    assert a != b
    assert b.num == 20
    assert c.num == 10


if __name__ == "__main__":
    unittest.main()
