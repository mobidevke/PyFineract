from fineract.objects.note import Note


def test_document_creation(fineract):
    note = Note.create(fineract.request_handler, Note.CLIENTS, 1, 'Test Note')
    assert isinstance(note, Note)


def test_retrieve_all_documents(fineract):
    notes = Note.get_all(fineract.request_handler, Note.CLIENTS, 1)
    assert notes.total_count > 0


def test_retrieve_single_note(fineract):
    note = Note.create(fineract.request_handler, Note.CLIENTS, 1, 'Test Note')
    note = Note.get(fineract.request_handler, Note.CLIENTS, 1, note.id)
    assert isinstance(note, Note)
