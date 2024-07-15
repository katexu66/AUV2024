import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertEqual(hello.sin(0.5), 0.479425538604203)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertEqual(hello.cos(0.5), 0.8775825618903728)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)
        self.assertEqual(hello.tan(0.5), 0.5463024898437905)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)
        self.assertEqual(hello.cot(0.5), 1.830487721712452)

    def test_add(self):
        self.assertEqual(hello.add(2, 3), 5)
        self.assertEqual(hello.add(3, 1), 4)
        self.assertEqual(hello.add(5, 4), 9)

    def test_sub(self):
        self.assertEqual(hello.sub(2, 3), -1)
        self.assertEqual(hello.sub(3, 1), 2)
        self.assertEqual(hello.sub(5, 4), 1)

    def test_mul(self):
        self.assertEqual(hello.mul(2, 3), 6)
        self.assertEqual(hello.mul(3, 1), 3)
        self.assertEqual(hello.mul(5, 4), 20)

    def test_div(self):
        self.assertEqual(hello.div(2, 1), 2)
        self.assertEqual(hello.div(8, 4), 2)
        self.assertEqual(
            hello.div(2, 0), "Can't divide by zero!"
        )  # code coverage -- test all cases

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(1), 1)
        self.assertEqual(hello.sqrt(4), 2)
        self.assertEqual(hello.sqrt(9), 3)

    def test_power(self):
        self.assertEqual(hello.power(2, 1), 2)
        self.assertEqual(hello.power(1, 2), 1)
        self.assertEqual(hello.power(2, 3), 8)

    def test_log(self):
        self.assertEqual(hello.log(10), 2.302585092994046)
        self.assertEqual(hello.log(100), 4.605170185988092)
        self.assertEqual(hello.log(1000), 6.907755278982137)

    def test_exp(self):
        self.assertEqual(hello.exp(1), 2.718281828459045)
        self.assertEqual(hello.exp(2), 7.38905609893065)
        self.assertEqual(hello.exp(3), 20.085536923187668)


if __name__ == "__main__":
    unittest.main()
