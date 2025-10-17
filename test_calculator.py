import unittest
from calculator import add, subtract

# 测试类，继承unittest.TestCase
class TestCalculator(unittest.TestCase):
    # 测试加法：正确情况
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # 2+3应该等于5
        self.assertEqual(add(-1, 1), 0)  # 负数测试

    # 测试减法：故意留一个错误（方便看CI报错效果）
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)  # 正确
        self.assertEqual(subtract(3, 5), -2)  # 错误！3-5应该是-2，这里写成-1

