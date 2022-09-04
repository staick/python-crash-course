import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for class Employee."""
    def setUp(self):
        self.employee = Employee('Tao', 'Song', 10000)
        
    def test_give_default_raise(self):
        """Test the default raise."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 15000)

    def test_give_custom_raise(self):
        """Test the custom raise."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 20000)


if __name__ == '__main__':
    unittest.main()
