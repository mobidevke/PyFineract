from fineract.objects.fineract_object import FineractObject


class DataTable(FineractObject):
    """
    This class represents a datatable
    """
    CLIENT = 'm_client'
    GROUP = 'm_group'
    LOAN = 'm_loan'
    OFFICE = 'm_office'
    SAVING_ACCOUNT = 'm_saving_account'
    PRODUCT_LOAN = 'm_product_loan'
    SAVINGS_PRODUCT = 'm_savings_product'

    def _init_attributes(self):
        self.application_table_name = None
        self.registered_table_name = None
        self.column_header_data = None

    def _use_attributes(self, attributes):
        self.application_table_name = attributes.get('applicationTableName', None)
        self.registered_table_name = attributes.get('registeredTableName', None)
        self.column_header_data = self._make_fineract_objects_list(DataTableColumn,
                                                                   attributes.get('columnHeaderData', None))

    @classmethod
    def create(cls, request_handler, name, apptable_name, columns, is_multirow=False):
        params = {
            'datatableName': name,
            'apptableName': apptable_name,
            'multiRow': is_multirow,
            'columns': columns,
        }

        data = request_handler.make_request(
            'POST',
            '/datatables',
            json=params
        )

        return cls(request_handler,
                   request_handler.make_request(
                       'GET',
                       '/datatables/{}'.format(data['resourceIdentifier']),
                   ), False)

    @classmethod
    def get(cls, request_handler, name):
        data = request_handler.make_request(
            'GET',
            '/datatables/{}'.format(name),
        )
        if not data:
            return None
        return cls(request_handler, data, False)

    def update(self, apptable_name=None, drop_columns=None, add_columns=None, change_columns=None):
        params = {}
        if apptable_name:
            params['apptableName'] = apptable_name

        if drop_columns:
            params['dropColumns'] = drop_columns

        if add_columns:
            params['addColumns'] = add_columns

        if change_columns:
            params['changeColumns'] = change_columns

        data = self._request_handler.make_request(
            'PUT',
            '/datatables/{}'.format(self.registered_table_name),
            json=params
        )

        if 'resourceIdentifier' in data:
            data = self._request_handler.make_request(
                'GET',
                '/datatables/{}'.format(self.registered_table_name))
            self._use_attributes(data)

    def delete(self):
        data = self._request_handler.make_request(
            'DELETE',
            '/datatables/{}'.format(self.registered_table_name)
        )
        return data['resourceIdentifier'] == self.registered_table_name

    @classmethod
    def register(cls, request_handler, name, apptable_name):
        data = request_handler.make_request(
            'POST',
            '/datatables/register/{}/{}'.format(name, apptable_name)
        )
        return data['resourceIdentifier'] == name

    @classmethod
    def deregister(cls, request_handler, name):
        data = request_handler.make_request(
            'POST',
            '/datatables/deregister/{}'.format(name)
        )
        return data['resourceIdentifier'] == name

    def insert(self, app_table_id, data):
        data = self._request_handler.make_request(
            'POST',
            '/datatables/{}/{}'.format(self.registered_table_name, app_table_id),
            json=data
        )
        return data['resourceId'] == app_table_id

    def get_data(self, app_table_id, order=None, desc=False):
        params = {
            'genericResultSet': False
        }
        if order:
            params['order'] = '`{}`'.format(order) if not desc else '`{}` desc'.format(order)
        return self._request_handler.make_request(
            'GET',
            '/datatables/{}/{}'.format(self.registered_table_name, app_table_id),
            params=params
        )

    def update_data(self, app_table_id, data, datatable_id=None):
        endpoint = '/datatables/{}/{}'.format(self.registered_table_name, app_table_id)
        if datatable_id:
            endpoint = '/datatables/{}/{}/{}'.format(self.registered_table_name, app_table_id, datatable_id)
        data = self._request_handler.make_request(
            'PUT',
            endpoint,
            json=data
        )
        return data['resourceId'] == app_table_id

    def delete_data(self, app_table_id, datatable_id=None):
        endpoint = '/datatables/{}/{}'.format(self.registered_table_name, app_table_id)
        if datatable_id:
            endpoint = '/datatables/{}/{}/{}'.format(self.registered_table_name, app_table_id, datatable_id)

        data = self._request_handler.make_request(
            'delete',
            endpoint,
        )
        return data['resourceId'] == app_table_id


class DataTableColumn(FineractObject):
    """
   This class represent a datatable column
   """

    def _init_attributes(self):
        self.column_name = None
        self.column_type = None
        self.column_length = None
        self.column_display_type = None
        self.is_column_nullable = None
        self.is_column_primary_key = None

    def _use_attributes(self, attributes):
        self.column_name = attributes.get('columnName', None)
        self.column_type = attributes.get('columnType', None)
        self.column_length = attributes.get('columnLength', 0)
        self.column_display_type = attributes.get('columnDisplayType', None)
        self.is_column_nullable = attributes.get('isColumnNullable', True)
        self.is_column_primary_key = attributes.get('isColumnPrimaryKey', False)
