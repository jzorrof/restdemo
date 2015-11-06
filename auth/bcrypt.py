# -*- coding: utf-8 -*-

import bcrypt
from eve.auth import BasicAuth


class BCryptAuth(BasicAuth):
    """docstring for BCryptAuth"""
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        if resource == 'accounts':
            return username == 'superuser' and password == 'password'
        else:
            accounts = app.data.drive.db['accounts']
            account = accounts.find_one({'username': username})
            return account and \
                   bcrypt.hashpwd(password, account['password']) == account['password']
