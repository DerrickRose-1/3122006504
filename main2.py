import unittest  # 导入单元测试框架

def add_numb(a, b):
    # 加法函数
    return a + b

def division_numb(a, b):
    # 除法函数，处理除以零的情况
    if b == 0:
        raise ValueError("不能除以零。")
    return a / b

class TestMathOperations(unittest.TestCase):
    # 单元测试类
    def test_add(self):
        # 测试加法
        test_cases = [(1, 1, 2), (2, 0, 2)]
        for a, b, expected in test_cases:
            self.assertEqual(add_numb(a, b), expected)

    def test_division(self):
        # 测试除法
        self.assertEqual(division_numb(2, 1), 2)
        with self.assertRaises(ValueError):
            division_numb(2, 0)  # 验证除以零的异常

if __name__ == "__main__":
    # 运行单元测试
    unittest.main()
