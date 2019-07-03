from fineract.objects.fineract_object import FineractObject


class Report(FineractObject):

    def _init_attributes(self):
        self.id = None
        self.report_name = None
        self.report_type = None
        self.report_category = None
        self.report_sql = None
        self.description = None
        self.core_report = None
        self.use_report = None
        self.report_parameters = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.report_name = attributes.get('reportName', None)
        self.report_type = attributes.get('reportType', None)
        self.report_category = attributes.get('reportCategory', None)
        self.report_sql = attributes.get('reportSql', None)
        self.description = attributes.get('description', None)
        self.core_report = attributes.get('coreReport', None)
        self.use_report = attributes.get('useReport', None)
        self.report_parameters = attributes.get('reportParameters', [])

    def update_sql(self, sql):
        data = self.request_handler.make_request(
            'PUT',
            '/reports/{}'.format(self.id),
            json={'reportSql': sql}
        )
        if data['resourceId'] == self.id:
            self.report_sql = sql

    @classmethod
    def create(cls, request_handler, report_name, report_type, report_category, report_sql, report_subtype='',
               description='', use_report=False, report_parameters=None):
        if report_parameters is None:
            report_parameters = []

        params = {
            'reportName': report_name,
            'reportType': report_type,
            'reportSubType': report_subtype,
            'reportCategory': report_category,
            'useReport': use_report,
            'description': description,
            'reportSql': report_sql,
            'reportParameters': report_parameters
        }

        data = request_handler.make_request(
            'POST',
            '/reports',
            json=params
        )

        return cls(request_handler,
                   request_handler.make_request(
                       'GET',
                       '/reports/{}'.format(data['resourceId']),
                   ), False)

    @classmethod
    def get_by_name(cls, request_handler, name):
        data = request_handler.make_request(
            'GET',
            '/reports'
        )
        for item in data:
            if item['reportName'] == name:
                return cls(request_handler, item, False)
        return None

    @staticmethod
    def exists(request_handler, name):
        """Check whether a report with the name (case sensitive) exists

        :param request_handler:
        :param name: Report name
        :return: bool
        """
        data = request_handler.make_request(
            'GET',
            '/reports'
        )
        for item in data:
            if item['reportName'] == name:
                return True
        return False