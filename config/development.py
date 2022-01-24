from config.default import *

SQLALCHEMY_DATABASE_URI =  'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACH_MODIFICATIONS = False
SECRET_KEY = "dev"