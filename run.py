#!flask/bin/python
from app import app

#Config
app.config.from_object('config.DevelopmentConfig')

app.run()
