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
        """Add a document to an entity of type ``entity_type`` with id ``entity_id``

        :param request_handler:
        :param entity_type:
        :param entity_id:
        :param name:
        :param description:
        :param file:
        :param filename:
        :param content_type:
        :rtype: :class:`fineract.objects.document.Document`
        """
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
        """Get all documents for an entity of type ``entity_type`` with id ``entity_id``

        :param request_handler:
        :param entity_type:
        :param entity_id:
        :rtype: :class:`fineract.pagination.PaginatedList` of :class:`fineract.objects.document.Document`
        """
        return PaginatedList(
            Document,
            request_handler,
            '/{}/{}/documents'.format(entity_type, entity_id),
            dict()
        )

    @classmethod
    def get(cls, request_handler, entity_type, entity_id, document_id):
        """Get a document for an entity of type ``entity_type`` with id ``entity_id`` if it matches ``document_id``

        :param request_handler:
        :param entity_type:
        :param entity_id:
        :param document_id:
        :rtype: :class:`fineract.objects.document.Document`
        """
        return Document(request_handler,
                    request_handler.make_request(
                        'GET',
                        '/{}/{}/documents/{}'.format(entity_type, entity_id, document_id),
                    ), False)

    def delete(self):
        """Delete a document

        :return: bool
        """
        data = self._request_handler.make_request(
            'DELETE',
            '/{}/{}/documents/{}'.format(self.parent_entity_type, self.parent_entity_id, self.id)
        )
        return data['resourceIdentifier'] == self.id

    def download(self):
        """Download a document

        :return: file content
        """
        return self._request_handler.make_request(
            'GET',
            '/{}/{}/documents/{}/attachment'.format(self.parent_entity_type, self.parent_entity_id, self.id),
            is_file=True
        )