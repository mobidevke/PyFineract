import mimetypes

from fineract.objects.fineract_object import FineractObject
from fineract.pagination import PaginatedList


class Document(FineractObject):
    """
    This class represents a document
    """
    CLIENTS = 'clients'
    STAFF = 'staff'
    LOANS = 'loans'
    SAVINGS = 'savings'
    CLIENT_IDENTIFIERS = 'client_identifiers'
    GROUPS = 'groups'

    def _init_attributes(self):
        self.id = None
        self.parent_entity_type = None
        self.parent_entity_id = None
        self.name = None
        self.file_name = None
        self.size = None
        self.type = None
        self.description = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.parent_entity_type = attributes.get('parentEntityType', None)
        self.parent_entity_id = attributes.get('parentEntityId', None)
        self.name = attributes.get('name', None)
        self.file_name = attributes.get('fileName', None)
        self.size = attributes.get('size', None)
        self.type = self._get_type(self.file_name)
        self.description = attributes.get('description', None)

    @staticmethod
    def _get_type(filename):
        if filename is not None:
            guessed = mimetypes.guess_type(filename, False)
            if guessed:
                return guessed[0]

        return None

    @classmethod
    def create(cls, request_handler, entity_type, entity_id, name, description, file, filename, content_type=None):
        if content_type is None:
            content_type = cls._get_type(filename)
        file_descr = (filename, file, content_type)
        params = {
            'name': name,
            'description': description,
            'file': file_descr,
        }

        data = request_handler.make_request(
            'POST',
            '/{}/{}/documents'.format(entity_type, entity_id),
            files=params,
            content_type='multipart/form-data'
        )

        return cls(request_handler,
                   request_handler.make_request(
                       'GET',
                       '/{}/{}/documents/{}'.format(entity_type, entity_id, data['resourceIdentifier'],),
                   ), False)

    @classmethod
    def get_all(cls, request_handler, entity_type, entity_id):
        return PaginatedList(
            Document,
            request_handler,
            '/{}/{}/documents'.format(entity_type, entity_id),
            dict()
        )

    @classmethod
    def get(cls, request_handler, entity_type, entity_id, document_id):
        return Document(request_handler,
                    request_handler.make_request(
                        'GET',
                        '/{}/{}/documents/{}'.format(entity_type, entity_id, document_id),
                    ), False)

    def delete(self):
        data = self._request_handler.make_request(
            'DELETE',
            '/{}/{}/documents/{}'.format(self.parent_entity_type, self.parent_entity_id, self.id)
        )
        return data['resourceIdentifier'] == self.id

    def download(self):
        return self._request_handler.make_request(
            'GET',
            '/{}/{}/documents/{}/attachment'.format(self.parent_entity_type, self.parent_entity_id, self.id),
            is_file=True
        )