from fineract.objects import Savings


def test_submit_savings_application(fineract):
    savings = Savings.apply(fineract.request_handler, 1, 1)
    assert isinstance(savings, Savings)


def test_get_all_savings_accounts(fineract):
    savings_accounts = fineract.get_savings_accounts()
    assert savings_accounts.total_count >= 1


def test_get_single_savings_account(fineract):
    savings = Savings.apply(fineract.request_handler, 1, 1)
    savings = fineract.get_savings_account(savings.id)
    assert isinstance(savings, Savings)


def test_savings_account_approval(fineract):
    savings = Savings.apply(fineract.request_handler, 1, 1)
    assert savings.approve()


def test_savings_account_activation(fineract):
    savings = Savings.apply(fineract.request_handler, 1, 1)
    savings.approve()
    assert savings.activate()

