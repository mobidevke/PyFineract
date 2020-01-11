from fineract import FineractException
from fineract.objects.fineract_object import FineractObject
from fineract.objects.types import Type
from fineract.pagination import PaginatedList


class Note(FineractObject):
    """
    This class represents a note
    """
    CLIENTS = 'clients'
    GROUPS = 'groups'
    LOANS = 'loans'
    SAVINGS = 'savingsaccounts'

    def _init_attributes(self):
        self.id = None
        self.entity_id = None
        self.entity_type = None
        self.note_type = None
        self.note = None
        self.created_by_id = None
        self.created_by_username = None
        self.created_on = None
        self.updated_by_id = None
        self.updated_by_username = None
        self.updated_on = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.entity_id = self.__get_entity_id(attributes)
        self.entity_type = self.__get_entity_type(attributes)
        self.note_type = self._make_fineract_object(NoteType, attributes.get('noteType', None))
        self.note = attributes.get('note', None)
        self.created_by_id = attributes.get('createdById', None)
        self.created_by_username = attributes.get('createdByUsername', None)
        self.created_on = self._make_date_object_from_timestamp(attributes.get('createdOn', None))
        self.updated_by_id = attributes.get('updatedById', None)
        self.updated_by_username = attributes.get('updatedByUsername', None)
        self.updated_on = self._make_date_object_from_timestamp(attributes.get('updatedOn', None))

    @classmethod
    def create(cls, request_handler, entity_type, entity_id, note) -> 'Note':
        """Add a note to an entity of type ``entity_type`` with id ``entity_id``

        :param request_handler:
        :param entity_type:
        :param entity_id:
        :param note:
        :rtype: :class:`fineract.objects.note.Note`
        """
        data = request_handler.make_request(
            'POST',
            '/{}/{}/notes'.format(entity_type, entity_id),
            json={'note': note}
        )

        return cls(request_handler,
                   request_handler.make_request(
                       'GET',
                       '/{}/{}/notes/{}'.format(entity_type, entity_id, data['resourceId'], ),
                   ), False)

    @staticmethod
    def __get_entity_id(attributes):
        if 'groupId' in attributes:
            return attributes['groupId']

        if 'loanId' in attributes:
            return attributes['loanId']

        if 'clientId' in attributes:
            return attributes['clientId']

        return None

    @staticmethod
    def __get_entity_type(attributes):
        if 'groupId' in attributes:
            return 'groups'

        if 'loanId' in attributes:
            return 'loans'

        if 'clientId' in attributes:
            return 'clients'

        return None

    @classmethod
    def get_all(cls, request_handler, entity_type, entity_id):
        """Get all notes for an entity of type ``entity_type`` with id ``entity_id``

        :param request_handler:
        :param entity_type:
        :param entity_id:
        :rtype: :class:`fineract.pagination.PaginatedList` of :class:`fineract.objects.note.Note`
        """
        return PaginatedList(
            Note,
            request_handler,
            '/{}/{}/notes'.format(entity_type, entity_id),
            dict()
        )

    @classmethod
    def get(cls, request_handler, entity_type, entity_id, note_id) -> 'Note':
        """Get a note for an entity of type ``entity_type`` with id ``entity_id`` if it matches ``note_id``

        :param request_handler:
        :param entity_type:
        :param entity_id:
        :param note_id:
        :rtype: :class:`fineract.objects.note.Note`
        """
        return Note(request_handler,
                    request_handler.make_request(
                        'GET',
                        '/{}/{}/notes/{}'.format(entity_type, entity_id, note_id),
                    ), False)

    def delete(self) -> bool:
        """Delete a note

        :return: bool
        """
        if self.entity_type is None:
            raise FineractException(500, 'Missing entity type')

        data = self._request_handler.make_request(
            'DELETE',
            '/{}/{}/notes/{}'.format(self.entity_type, self.entity_id, self.id)
        )
        return data['resourceIdentifier'] == self.id


class NoteType(Type):
    pass
