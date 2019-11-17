from fineract.objects import Loan


def test_loan_application(fineract):
    loan = Loan.apply(fineract.request_handler, 1, 1, 10000)
    assert isinstance(loan, Loan)


def test_loan_deletion(fineract):
    client = fineract.get_client(1)
    loans = client.get_loans()
    assert loans[-1].delete()


def test_loan_approval(fineract):
    Loan.apply(fineract.request_handler, 1, 1, 10000)
    client = fineract.get_client(1)
    loans = client.get_loans()
    assert loans[-1].approve()


def test_loan_disbursal(fineract):
    client = fineract.get_client(1)
    loans = client.get_loans()
    assert loans[-1].disburse()


def test_undo_loan_disbursal(fineract):
    client = fineract.get_client(1)
    loans = client.get_loans()
    assert loans[-1].undo_disbursal('No reason')


# def test_loan_disbursal_to_savings(fineract):
#     client = fineract.get_client(1)
#     loans = client.get_loans()
#     assert loans[-1].disburse_to_savings()


def test_undo_loan_approval(fineract):
    client = fineract.get_client(1)
    loans = client.get_loans()
    assert loans[-1].undo_approval('No reason')

