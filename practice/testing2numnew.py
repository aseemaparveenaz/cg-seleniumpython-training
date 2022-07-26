def close_check(a, b, c):
    if a == b+1 or a == c+1 or b == a+1 or b == c+1 or c == a+1 or c == b+1:
        l1 = [a, b, c]
        l1.sort()
        if (l1[1] - l1[0] >= 2 and l1[2] - l1[0] >= 2) or (l1[2] - l1[0] >= 2 and l1[2] - l1[1] >= 2):
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    print(close_check(4, 1, 3))
    print(close_check(5, 6, 7))
    print(close_check(1, 2, 3))
    print(close_check(99, 100, 3))

-------
import unittest
import Day19.activity1 as A

class TestActivity1(unittest.TestCase):
    def test_close_check(self):
        self.assertTrue(A.close_check(4, 1, 3))
        self.assertFalse(A.close_check(5, 6, 7)
----
import unittest

def check(test):
    lis = list(test)
    lis.sort()
    if (lis[1] == lis[0]+1 or lis[1] == lis[2] - 1 or lis[1] == lis[0] or lis[1] == lis[2]):
        if lis[1] +2 <= lis[2] or lis[0]+2 <= lis[1]:
            return True
        else:
            return False
    else:
        return False

test = 4,1,3
print(check(test))


class testthenumber(unittest.TestCase):
    test = 4,1,3
    def test_check(self):
        self.test = test
        self.assertEqual(check((test)), True)

if __name__ == '__main__':
    unittest.main()

----------
import assignment
import pytest

def test_valid_conditons():
    assert(assignment.conditions(5, 6, 8),True)
    assert(assignment.conditions(4, 1, 3),True)


def test_invalid_conditions():
    assert(assignment.conditions(1, 2, 3),False)


def test_negative_numbers():
    assert(assignment.conditions(-1, -2, -3),False)


def test_invalid_float_numbers():
    assert(assignment.conditions(1.1, 2.2, 3.3),False)


def test_valid_float_numbers():
    assert(assignment.conditions(4.1, 1.1, 3.1),True)