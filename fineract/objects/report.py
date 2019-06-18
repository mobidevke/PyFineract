from fineract.objects.fineract_object import FineractObject


class Report(FineractObject):

    def _init_attributes(self):
        self.id = None
        self.report_name = None
        self.report_type = None
        self.report_category = None
        self.description = None
        self.core_report = None
        self.use_report = None
        self.report_parameters = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.report_name = attributes.get('reportName', None)
        self.report_type = attributes.get('reportType', None)
        self.report_category = attributes.get('reportCategory', None)
        self.description = attributes.get('description', None)
        self.core_report = attributes.get('coreReport', None)
        self.use_report = attributes.get('useReport', None)
        self.report_parameters = attributes.get('reportParameters', [])
