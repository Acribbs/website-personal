#Default Config

class BaseConfig(object):
	MAP_API_KEY = "AIzaSyBKZ8HTbkOmKT2oaJ_8p8djs02C4OlF44I"
	DEBUG = False
	WTF_CSRF_ENABLED = True
	SECRET_KEY = 'z\xa4\xff\x95\x97\x80\x97Z,7\xcc\x92F\x04\xb6\xe9T~\xfb\x92jT\xe8\x05'
	DATABASE = '/Users/adamc/Documents/website/app/csvdb.sqlite'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
	SQALCHEMY_BINDS = {
		'csvdb':		'sqlite:///csvdb',
		'users2':		'sqlite:///login.sqlite'
		}
	OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '158184191213013',
        'secret': '5544cc829ba6b63719b6215415ff4d15'
    },
    'twitter': {
        'id': 'S5lbcjs6ktyxWNnbN9IDF2nyP',
        'secret': '4rsoZytczoRjnr8esiOvZyYAGXVsM77YaD7rg46FuNaOlERSgb'
    }
}

class DevelopmentConfig(BaseConfig):
	DEBUG = True
	
class ProductionConfig(BaseConfig):
	DEBUG = False

#current_app.config['OAUTH_CREDENTIALS']