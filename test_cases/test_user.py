# 登录
import pytest
import requests
from params.tools import TokenUtils, UserIdUtils, UserInfoUtils, UserAddDatasUtils

class TestUser:

    @pytest.mark.parametrize('args', UserAddDatasUtils().read_user_add_datas_yaml())
    def test_user_add(self, args):
        headers = {
            'token': TokenUtils().read_token_yaml('token')
        }
        data = args['data']
        response = requests.request('post', "http://218.0.51.16:1818/nanke/member/add", data=data, headers=headers)
        print(response.json())
        assert args['validate'] == response.json()['status']
        # assert None == response.json()['data']
    #

    def test_user_list(self):
        headers = {
            'token': TokenUtils().read_token_yaml('token')
        }
        response = requests.request('get', "http://218.0.51.16:1818/nanke/member/list", headers=headers)
        userid = response.json()['data']['list'][0]['id']
        UserIdUtils().write_userid_yaml({"id": userid})
        # print(response.json())
        assert 200 == response.json()['status']
    #
    # def test_user_update(self):
    #     headers = {
    #         'token': TokenUtils().read_token_yaml('token')
    #     }
    #     data = {
    #         "name": 'qwe006',
    #         "mobile": 13233333336,
    #         'sex': 1,
    #         'identities': 2006,
    #         'money': 0,
    #         'id': UserIdUtils().read_userid_yaml('id')
    #     }
    #     response = requests.request('post', "http://218.0.51.16:1818/nanke/member/update", json=data, headers=headers)
    #     print(response.json())
    #     assert 200 == response.json()['status']
    #
    #

    def test_user_info(self):
        headers = {
            'token': TokenUtils().read_token_yaml('token')
        }
        data = {
            'id': UserIdUtils().read_userid_yaml('id')
        }
        response = requests.request('get', "http://218.0.51.16:1818/nanke/member/single", params=data, headers=headers)
        print(response.json()['data'])
        UserInfoUtils().write_userInfo_yaml(response.json()['data'])
        # assert 200 == response.json()['status']
    #
    #

    def test_user_charge(self):
        headers = {
            'token': TokenUtils().read_token_yaml('token')
        }
        data = {
            "name": UserInfoUtils().read_userInfo_yaml('name'),
            "mobile": UserInfoUtils().read_userInfo_yaml('mobile'),
            'identities': UserInfoUtils().read_userInfo_yaml('identities'),
            'id': UserInfoUtils().read_userInfo_yaml('id'),
            'money': 100,

        }
        response = requests.request('post', "http://218.0.51.16:1818/nanke/recharge/member", json=data, headers=headers)
        print(response.json())
        assert 200 == response.json()['status']
    #
    def test_user_consume(self):
        headers = {
            'token': TokenUtils().read_token_yaml('token')
        }
        data = {
            "name": UserInfoUtils().read_userInfo_yaml('name'),
            "mobile": UserInfoUtils().read_userInfo_yaml('mobile'),
            'identities': UserInfoUtils().read_userInfo_yaml('identities'),
            'id': UserInfoUtils().read_userInfo_yaml('id'),
            'money': 10,

        }
        response = requests.request('post', "http://218.0.51.16:1818/nanke/consume/member", json=data, headers=headers)
        print(response.json())
        assert 200 == response.json()['status']
    #
    def test_user_delete(self):
        headers = {
            'token': TokenUtils().read_token_yaml('token')
        }
        data = {
            'id': UserIdUtils().read_userid_yaml('id')
        }
        response = requests.request('post', "http://218.0.51.16:1818/nanke/member/del", data=data, headers=headers)
        print(response.json())
        assert 200 == response.json()['status']
    #
