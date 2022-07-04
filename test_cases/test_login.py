# 登录
import pytest
import requests
from params.tools import TokenUtils, LoginRequestsUtils

class TestLogin:
    @pytest.mark.parametrize('loginData', LoginRequestsUtils().read_login_requests_yaml())
    def test_login(self, loginData):
        # data =
        method = loginData['api_request']['method']
        url = loginData['api_request']['url']
        params = loginData['api_request']['params']
        response = requests.request(method, url, data=params)
        TokenUtils().write_token_yaml({"token": response.json()['data']})
        assert 200 == response.json()['status']

