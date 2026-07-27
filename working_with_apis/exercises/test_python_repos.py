from working_with_apis.python_repos import r

# print(r.status_code)

def test_successful_api_call():
    assert r.status_code == 200