from fineract.objects import Loan


def test_loan_application(fineract):
    loan = Loan.apply(fineract.request_handler, 1, 1, 10000)
    assert isinstance(loan, Loan)