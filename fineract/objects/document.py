from fineract.objects.fineract_object import FineractObject


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
        self.file_name = attributes.get('file_name', None)
        self.size = attributes.get('size', None)
        self.type = attributes.get('description', None)