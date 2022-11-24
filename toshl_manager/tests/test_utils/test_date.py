from datetime import date
from unittest.mock import patch
from unittest import TestCase
from toshl_manager.utils.date import begin_month, end_month, _today


class TestToday(TestCase):

    @patch('toshl_manager.utils.date.date')
    def test_first_november(self, date_mock):
        today = date(year=2022, month=11, day=1)
        date_mock.today.return_value = today
        self.assertEqual(_today(), today)

    @patch('toshl_manager.utils.date.date')
    def test_second_february(self, date_mock):
        today =  date(year=2022, month=2, day=2)
        date_mock.today.return_value = today
        self.assertEqual(_today(), today)


class TestBeginMonth(TestCase):

    @patch('toshl_manager.utils.date._today', return_value=date(year=2022, month=11, day=12))
    def test_current_month(self, today_mock):
        self.assertEqual(begin_month(), "01/11/22")

    @patch('toshl_manager.utils.date._today', return_value=date(year=2022, month=10, day=5))
    def test_last_month(self, today_mock):
        self.assertEqual(begin_month(), "01/10/22")


class TestEndMonth(TestCase):

    @patch('toshl_manager.utils.date._today', return_value=date(year=2022, month=11, day=12))
    def test_current_month(self, today_mock):
        self.assertEqual(end_month(), "30/11/22")

    @patch('toshl_manager.utils.date._today', return_value=date(year=2022, month=10, day=5))
    def test_last_month(self, today_mock):
        self.assertEqual(end_month(), "31/10/22")
