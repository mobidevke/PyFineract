import filecmp

from fineract.objects.document import Document


def test_document_creation(fineract):
    with open('tests/files/image.png', 'rb') as in_file:
        doc = Document.create(fineract.request_handler, Document.CLIENTS, 1, 'Test image', 'Some test description',
                              in_file)
        assert isinstance(doc, Document)


def test_retrieve_all_documents(fineract):
    documents = Document.get_all(fineract.request_handler, Document.CLIENTS, 1)
    assert documents.total_count > 0


def test_retrieve_single_document(fineract):
    with open('tests/files/image.png', 'rb') as in_file:
        doc = Document.create(fineract.request_handler, Document.CLIENTS, 1, 'Test image', 'Some test description',
                              in_file)
        doc = Document.get(fineract.request_handler, Document.CLIENTS, 1, doc.id)
        assert isinstance(doc, Document)


def test_download_document_file(fineract, tmpdir):
    in_path = 'tests/files/image.png'
    with open(in_path, 'rb') as in_file:
        doc = Document.create(fineract.request_handler, Document.CLIENTS, 1, 'Test image', 'Some test description',
                              in_file)
        out_file = tmpdir.join('out.png')
        out_path = str(out_file)
        out_file.write_binary(doc.download())
        assert filecmp.cmp(in_path, out_path)