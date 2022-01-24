from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xf8n\x7f\xb4\xea\x02\x93\x03\x87\x1d\x19}\x9d.\xee\xbf'