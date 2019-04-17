import json

import requests
from requests import Response

from fineract.handlers import RequestHandler
from fineract.objects.loan import Loan, LoanSummary, LoanRepaymentSchedule, LoanRepaymentPeriod
from fineract.pagination import PaginatedList


def fake_handler1(method, url, **kwargs):
    class FakeResponse(Response):

        @property
        def ok(self):
            return True

        def json(self, **kwargs):
            with open('tests/files/loan.json', 'r') as in_file:
                data = json.load(in_file)

            return [data]

    return FakeResponse()


def test_loan_object_creation__interest_recalculation_data():
    with open('tests/files/loan.json', 'r') as in_file:
        data = json.load(in_file)
        loan = Loan(None, data, False)
        assert isinstance(loan.summary, LoanSummary)


def test_get_loans(mocker):
    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)

    mocker.patch.object(requests.Session, 'send', new=fake_handler1)
    paginated_list = PaginatedList(Loan, request_handler, '/', {})
    count = 0
    for item in paginated_list:
        count += 1

    assert count == 1
    assert isinstance(paginated_list[0], Loan)


def test_loan_repayment_schedule_object_creation__interest_recalculation_data():
    with open('tests/files/loanrepaymentschedule.json', 'r') as in_file:
        data = json.load(in_file)
        loan = LoanRepaymentSchedule(None, data, False)
        assert isinstance(loan.periods, list)
        assert isinstance(loan.periods[0], LoanRepaymentPeriod)
