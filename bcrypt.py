# -*- coding: utf-8 -*-

import os
import bcrypt
from eve.auth import BasicAuth


class BCryptAuth(object):
    """docstring for BCryptAuth"""
    def check_auth(self, username, password, allowed_roles, resource, method):
        if resource == 'accounts':
            return username == 'superuser' and password == 'password'
