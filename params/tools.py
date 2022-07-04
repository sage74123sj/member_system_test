# 封装读取Yaml的方法
import os
import yaml


class TokenUtils:
    def write_token_yaml(self, data):
        with open(os.getcwd()+"\\params\\yaml\\token.yaml", mode="w", encoding="utf-8") as f:
            yaml.dump(data=data, stream=f)

    def read_token_yaml(self, token):
        with open(os.getcwd()+"\\params\\yaml\\token.yaml", mode='r', encoding='utf-8') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[token]


class UserIdUtils:
    def write_userid_yaml(self, data):
        with open(os.getcwd()+"\\params\\yaml\\user_id.yaml", mode="w", encoding="utf-8") as f:
            yaml.dump(data=data, stream=f)

    def read_userid_yaml(self, userid):
        with open(os.getcwd()+"\\params\\yaml\\user_id.yaml", mode='r', encoding='utf-8') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[userid]


class UserInfoUtils:
    def write_userInfo_yaml(self, data):
        with open(os.getcwd()+"\\params\\yaml\\user_info.yaml", mode='w', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f)

    def read_userInfo_yaml(self, props):
        with open(os.getcwd()+"\\params\\yaml\\user_info.yaml", mode='r', encoding='utf-8') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[props]


class LoginRequestsUtils:
    def read_login_requests_yaml(self):
        with open(os.getcwd()+"\\params\\yaml\\login_request.yaml", encoding='utf-8') as f:
            data = yaml.load(f, yaml.FullLoader)
            return data

class UserAddDatasUtils:
    def read_user_add_datas_yaml(self):
        with open(os.getcwd()+"\\params\\yaml\\user_add.yaml", encoding='utf-8') as f:
            data = yaml.load(f, yaml.FullLoader)
            return data