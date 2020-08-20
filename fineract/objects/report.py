from typing import Union, List, Dict, Optional

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
               description='', use_report=False, report_parameters=None) -> 'Report':
        """Create a report

        :param request_handler:
        :param report_name:
        :param report_type:
        :param report_category:
        :param report_sql:
        :param report_subtype:
        :param description:
        :param use_report:
        :param report_parameters:
        :rtype: :class:`fineract.objects.report.Report`
        """
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
    def get_by_name(cls, request_handler, name) -> Optional['Report']:
        """Return a report that matches ``name``

        :param request_handler:
        :param name:
        :rtype: :class:`fineract.objects.report.Report`
        """
        data = request_handler.make_request(
            'GET',
            '/reports'
        )
        for item in data:
            if item['reportName'] == name:
                return cls(request_handler, item, False)
        return None

    @staticmethod
    def exists(request_handler, name) -> bool:
        """Check whether a report with the name (case sensitive) exists

        :param request_handler: :class:`fineract.handlers.RequestHandler`
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

    @staticmethod
    def run(request_handler, name, generic_result_set=True, **kwargs) -> Union[List, Dict]:
        """Run the report ``name`` if it exists

        :param request_handler: :class:`fineract.handlers.RequestHandler`
        :param name: Report name
        :param generic_result_set: if 'True' an optimised JSON forma is returned. If 'False' a simple JSON format is
               returned
        :param kwargs: Report parameters
        :return: list of dict
        """
        params = {
            'genericResultSet': generic_result_set,
            'pretty': False
        }
        for param in kwargs.keys():
            params['R_{}'.format(param)] = kwargs[param]

        return request_handler.make_request('GET', '/runreports/{}'.format(name), params=params)
