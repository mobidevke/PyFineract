def test_get_datatable(fineract):
    client = fineract.get_client(1)
    assert client
    data = client.get_datatable_data('Client Profile')
    assert data
    assert len(data) == 1


def test_get_datatable__multirow(fineract):
    client = fineract.get_client(1)
    data = client.get_datatable_data('Client Laptops')
    assert data
    assert len(data) == 2
