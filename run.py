# -*- coding: utf-8 -*-

import bcrypt
from eve import Eve
from eve.auth import BasicAuth

app = Eve()

class BCryptAuth(object):
	"""docstring for BCryptAuth"""
	def check_auth(self, username, password, allowed_roles):
		if resource == 'accounts':
            return username == 'superuser' and password == 'password'
        else
			accounts = app.data.drive.db['accounts']
			account = accounts.find_one({'username':username})
			return account and \
				bcrypt.hashpwd(password, account['password']) == account['password']
if __name__ == '__main__':
	app = Eve(auth=BCryptAuth)
	app.run()