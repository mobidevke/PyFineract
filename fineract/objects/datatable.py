from fineract.objects.fineract_object import FineractObject


class DataTable(FineractObject):
    """
    This class represents a datatable
    """

    def _init_attributes(self):
        self.application_table_name = None
        self.registered_table_name = None
        self.column_header_data = None

    def _use_attributes(self, attributes):
        self.application_table_name = attributes.get('applicationTableName', None)
        self.registered_table_name = attributes.get('registeredTableName', None)
        self.column_header_data = self._make_fineract_objects_list(DataTableColumn,
                                                                   attributes.get('columnHeaderData', None))


class DataTableColumn(FineractObject):
    """
   This class represent a datatable column
   """

    def _init_attributes(self):
        self.name = None
        self.type = None
        self.length = None
        self.display_type = None
        self.is_nullable = None
        self.is_primary_key = None

    def _use_attributes(self, attributes):
        self.name = attributes.get('columnName', None)
        self.type = attributes.get('columnType', None)
        self.length = attributes.get('columnLength', 0)
        self.display_type = attributes.get('columnDisplayType', None)
        self.is_nullable = attributes.get('isColumnNullable', True)
        self.is_primary_key = attributes.get('isColumnPrimaryKey', False)
