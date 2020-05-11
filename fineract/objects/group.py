from fineract.objects.fineract_object import DataFineractObject
from fineract.objects.types import Type


class Group(DataFineractObject):
    """
    This class represents a Group.
    """
    def __repr__(self):
        return self.get__repr__({'group_id': self.id})

    def _init_attributes(self):
        self.id = None
        self.account_no = None
        self.external_id = None
        self.name = None
        self.status = None
        self.active = None
        self.activation_date = None
        self.office_id = None
        self.office_name = None
        self.hierarchy = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.account_no = attributes.get('accountNo', None)
        self.external_id = attributes.get('externalId', None)
        self.name = attributes.get('name', None)
        self.status = self._make_fineract_object(GroupStatus, attributes.get('status', None))
        self.active = attributes.get('active', None)
        self.activation_date = self._make_date_object(attributes.get('activationDate', None))
        self.office_id = attributes.get('officeId', None)
        self.office_name = attributes.get('officeName', None)
        self.hierarchy = attributes.get('hierarchy', None)

    def add_members(self, members_list):
        params = {
            'clientMembers': members_list
        }

        data = self.request_handler.make_request(
            'POST',
            '/groups/{}?command=associateClients'.format(self.id),
            json=params
        )
        return data['groupId'] == self.id

    def remove_members(self, members_list):
        params = {
            'clientMembers': members_list
        }

        data = self.request_handler.make_request(
            'POST',
            '/groups/{}?command=disassociateClients'.format(self.id),
            json=params
        )
        return data['groupId'] == self.id

    @classmethod
    def create(cls, request_handler, name, office_id, active=True, activation_date=None):
        """Create a group

        :param request_handler:
        :param name:
        :param office_id:
        :param active:
        :param activation_date:
        :rtype: :class:`fineract.objects.group.Group`
        """
        data = {
            'name': name,
            'officeId': office_id,
            'active': active,
            'activationDate': activation_date or cls._get_current_date()
        }

        res = request_handler.make_request(
            'POST',
            '/groups',
            json=data
        )

        group_id = res['groupId']
        return cls(request_handler,
                   request_handler.make_request(
                       'GET',
                       '/groups/{}'.format(group_id)
                   ), False)

    @classmethod
    def get_group_by_name(cls, request_handler, name):
        """Get a group by name

        :param request_handler:
        :param name:
        :rtype: :class:`fineract.objects.group.Group`
        """
        data = request_handler.make_request(
            'GET',
            '/groups'
        )
        if data:
            for item in data:
                if item['name'] == name:
                    print(item)
                    return cls(request_handler, item, False)

        return None


class GroupStatus(Type):
    """
    This class represents a Group status.
    """
    pass
