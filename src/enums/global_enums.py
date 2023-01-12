from enum import Enum

class GlobalErrorMessages(Enum):
    LONG_RESPONSE_TIME = "Response time exceeds expected"
    WRONG_STATUS_CODE = "Recieved status code is not equal to expected"
    GRAPHQL_ERROR = "Got GraphQL Execution Error"
    WRONG_PERIOD = "Period is wrong"
