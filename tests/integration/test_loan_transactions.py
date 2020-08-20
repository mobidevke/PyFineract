import datetime

from fineract.objects import Loan


def test_loan_approval(fineract):
    Loan.apply(fineract.request_handler, 1, 1, 10000)
    client = fineract.get_client(1)
    loans = client.get_loans()
    loans[-1].approve()
    loans[-1].disburse()
    assert loans[-1].make_repayment(5000, datetime.datetime.now(), receiptNumber='abc')
