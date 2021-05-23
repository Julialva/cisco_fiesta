try:
    from flask import Flask
    from flask_restful import Api 
    from flask_sqlalchemy import SQLAlchemy
    from flask_marshmallow import Marshmallow
    import os
except Exception as e:
    print("These required modules are missing {}".format(e))
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
from cisco_fiesta import routes