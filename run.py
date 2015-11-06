from eve import Eve
from bcrypt import BCryptAuth

app = Eve(auth=BCryptAuth)
if __name__ == '__main__':
    app.run()
