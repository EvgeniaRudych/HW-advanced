import unittest
from unittest.mock import patch
from employee import Employee


class MockTestTrue:
    text = 'response.ok = True'
    status_code = 200
    ok = True
    
    def __init__(self, *args, **kwargs):
        pass


class MockTestFalse:
    text = 'response.ok = False'
    ok = False

    def __init__(self, *args, **kwargs):
        pass


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee('Evgenia', 'Rudych', 20000)

    def test_email(self):
        self.assertEqual(self.employee1.email, 'Evgenia.Rudych@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee1.fullname, f'{self.employee1.first} {self.employee1.last}')

    def test_apply_raise(self):
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.pay, 21000)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock_get_response):
        mock_get_response.side_effect = MockTestTrue
        print(self.employee1.monthly_schedule('May'))
        self.assertEqual(self.employee1.monthly_schedule('May'), 'response.ok = True')
        mock_get_response.side_effect = MockTestFalse
        print(self.employee1.monthly_schedule('May'))
        self.assertEqual(self.employee1.monthly_schedule('May'), 'Bad Response!')
