from eve import Eve

app = Eve(auth=MyBasicAuth)
if __name__ == '__main__':
    app.run()
