import requests
import data.queries as q
import data.creds as c
from src.classes.response import Response


def test_auth_request():
    r = requests.post(c.identityURL, auth=requests.auth.HTTPBasicAuth(c.user, c.password), headers=c.authHeaders, verify=False, data=c.authData)
    response = Response(r)

    response.assert_status_code(200)

    access_token = response.response_json['access_token']
    return {"Authorization": "Bearer " + access_token}

def test_query_n_1_events():
    r = requests.post(c.apiURL, headers=test_auth_request(), json={"query": q.query_1}, verify=False)
    response = Response(r)

    response.assert_status_code(200)
    response.assert_response_time(1)
    response.assert_graphql_error()

def test_query_n_2_date():
    r = requests.post(c.apiURL, headers=test_auth_request(), json={"query": q.query_2}, verify=False)
    response = Response(r)

    response.assert_status_code(200)
    response.assert_response_time(10)
    response.assert_graphql_error()
    response.assert_date()

def test_query_n_3_sum():
    r = requests.post(c.apiURL, headers=test_auth_request(), json={"query": q.query_3}, verify=False)
    response = Response(r)

    response.assert_status_code(200)
    response.assert_response_time(10)
    response.assert_graphql_error()

def test_query_n_4_moving_deviation():
    r = requests.post(c.apiURL, headers=test_auth_request(), json={"query": q.query_4}, verify=False)
    response = Response(r)

    response.assert_status_code(200)
    response.assert_response_time(10)
    response.assert_graphql_error()

def test_query_n_5_moving_delta():
    r = requests.post(c.apiURL, headers=test_auth_request(), json={"query": q.query_5}, verify=False)
    response = Response(r)

    response.assert_status_code(200)
    response.assert_response_time(10)
    response.assert_graphql_error()

def test_query_n_6_avg():
    r = requests.post(c.apiURL, headers=test_auth_request(), json={"query": q.query_6}, verify=False)
    response = Response(r)

    response.assert_status_code(200)
    response.assert_response_time(10)
    response.assert_graphql_error()

def test_query_n_7_normalization():
    r = requests.post(c.apiURL, headers=test_auth_request(), json={"query": q.query_7}, verify=False)
    response = Response(r)

    response.assert_status_code(200)
    response.assert_response_time(10)
    response.assert_graphql_error()

def test_query_n_8_no_postprocessing():
    r = requests.post(c.apiURL, headers=test_auth_request(), json={"query": q.query_8}, verify=False)
    response = Response(r)

    response.assert_status_code(200)
    response.assert_response_time(10)
    response.assert_graphql_error()