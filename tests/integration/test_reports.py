import random

from fineract.objects.report import Report

number = random.randint(0, 10000)


def test_get_all_reports(fineract):
    reports = [report for report in fineract.get_reports()]
    assert len(reports) > 1


def test_create_report(fineract):
    report = Report.create(fineract.request_handler, 'Test Report ' + str(number), 'Table', 'Client',
                           'SELECT * FROM m_client')
    assert isinstance(report, Report)


def test_report_exists(fineract):
    assert Report.exists(fineract.request_handler, 'Test Report ' + str(number))


def test_get_by_name(fineract):
    assert Report.get_by_name(fineract.request_handler, 'Test Report ' + str(number))


def test_update_sql(fineract):
    report = Report.get_by_name(fineract.request_handler, 'Test Report ' + str(number))
    report.update_sql('SELECT id FROM m_client')
    assert report.report_sql == 'SELECT id FROM m_client'


def test_run_report(fineract):
    data = Report.run(fineract.request_handler, 'Test Report ' + str(number), False)
    assert data
