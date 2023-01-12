from src.enums.global_enums import GlobalErrorMessages
from datetime import date, timedelta

class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert  self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def assert_response_time(self, response_time):
        assert self.response.elapsed.total_seconds() <= response_time, GlobalErrorMessages.LONG_RESPONSE_TIME.value

    def assert_graphql_error(self):
        assert self.response_json['data']['biIndicators'][0]['indicatorData']['debugData']['error'] == None, GlobalErrorMessages.GRAPHQL_ERROR.value

    def assert_date(self):
        result_yesterday = str(date.today() - timedelta(days=1)) + 'T00:00:00.000Z'
        result_today = str(date.today()) + 'T00:00:00.000Z'
        period_from = self.response_json['data']['biIndicators'][0]['indicatorData']['period']['from']
        period_to = self.response_json['data']['biIndicators'][0]['indicatorData']['period']['to']
        assert period_from == result_yesterday, GlobalErrorMessages.WRONG_PERIOD.value
        assert period_to == result_today, GlobalErrorMessages.WRONG_PERIOD.value