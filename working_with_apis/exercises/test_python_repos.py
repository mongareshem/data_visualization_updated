from working_with_apis.python_repos import r, response_dict

def test_successful_api_call():
    assert r.status_code == 200
    assert response_dict['total_count'] == 971
    assert len(response_dict['items']) == 30