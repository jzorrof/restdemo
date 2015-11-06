# -*- coding: utf-8 -*-

import os
import bcrypt
from eve.auth import BasicAuth


class BCryptAuth(object):
    """docstring for BCryptAuth"""

    def check_auth(self, username, password, allowed_roles, methods):
        if resource == 'accounts':
            return username == 'superuser' and password == 'password'
        else:
            accounts = app.data.drive.db['accounts']
            account = accounts.find_one({'username': username})
            return account and \
                   bcrypt.hashpwd(password, account['password']) == account['password']
