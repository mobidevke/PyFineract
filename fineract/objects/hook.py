from typing import Optional

from fineract.objects.fineract_object import FineractObject


class Hook(FineractObject):

    def _init_attributes(self):
        self.id = None
        self.name = None
        self.is_active = None
        self.created_at = None
        self.updated_at = None
        self.display_name = None
        self.template_id = None
        self.events = None
        self.config = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)
        self.display_name = attributes.get('displayName', None)
        self.is_active = attributes.get('isActive', None)
        self.created_at = self._make_date_object(attributes.get('createdAt', None))
        self.updated_at = self._make_date_object(attributes.get('updatedAt', None))
        self.template_id = attributes.get('templateId', None)
        self.events = attributes.get('events', [])
        self.config = attributes.get('config', [])

    def update(self, payload_url, events) -> 'Hook':
        """Update a web hook

        :param payload_url:
        :param events:
        :return:
        """
        params = {
            'name': 'Web',
            'displayName': self.display_name,
            'events': events,
            'isActive': self.is_active,
            'config': {
                'Payload URL': payload_url,
                'Content Type': 'json'
            }
        }

        self.request_handler.make_request(
            'PUT',
            '/hooks/{}'.format(self.id),
            json=params
        )
        return self.get(self.request_handler, self.id)

    @classmethod
    def create_web_hook(cls, request_handler, display_name, payload_url, events, content_type='json', is_active=False,
                        template_id=None) -> 'Hook':
        """Create a web hook

        :param request_handler:
        :param display_name:
        :param payload_url:
        :param events:
        :param content_type:
        :param is_active:
        :param template_id:
        :rtype: :class:`fineract.objects.hook.Hook`
        """
        params = {
            'name': 'Web',
            'displayName': display_name,
            'events': events,
            'config': {
                'Payload URL': payload_url,
                'Content Type': content_type
            }
        }

        if is_active:
            params['isActive'] = is_active

        if template_id:
            params['templateId'] = template_id

        data = request_handler.make_request(
            'POST',
            '/hooks',
            json=params
        )

        return cls(request_handler,
                   request_handler.make_request(
                       'GET',
                       '/hooks/{}'.format(data['resourceId']),
                   ), False)

    @classmethod
    def get(cls, request_handler, id) -> 'Hook':
        """Get a hook with id ``id``

        :param request_handler:
        :param id:
        :rtype: :class:`fineract.objects.hook.Hook`
        """
        return Hook(request_handler,
                    request_handler.make_request(
                        'GET',
                        '/hooks/{}'.format(id),
                    ), False)

    @classmethod
    def get_by_name(cls, request_handler, name) -> Optional['Hook']:
        """Get a hook that matches ``name``

        :param request_handler:
        :param name:
        :rtype: :class:`fineract.objects.hook.Hook`
        """
        data = request_handler.make_request(
            'GET',
            '/hooks'
        )
        for item in data:
            if item['displayName'] == name:
                return cls(request_handler, item, False)
        return None

    @staticmethod
    def exists(request_handler, name) -> bool:
        """Check whether a hook with the name (case sensitive) exists

        :param request_handler:
        :param name: Hook name
        :return: bool
        """
        data = request_handler.make_request(
            'GET',
            '/hooks'
        )
        for item in data:
            if item['displayName'] == name:
                return True
        return False

    @staticmethod
    def template(request_handler) -> dict:
        """Get a hook template

        :param request_handler:
        :return: dict
        """
        return request_handler.make_request(
            'GET',
            '/hooks/template'
        )
