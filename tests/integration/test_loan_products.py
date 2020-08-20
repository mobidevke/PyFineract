def test_get_all_loan_products(fineract):
    products = [product for product in fineract.get_loan_products()]
    assert len(products) == 1


def test_get_single_loan_product(fineract):
    product = fineract.get_loan_product(1)
    assert product
