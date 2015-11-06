from auth.bcrypt import BCryptAuth
from eve import Eve

app = Eve(auth=BCryptAuth)
if __name__ == '__main__':
    app.run()
