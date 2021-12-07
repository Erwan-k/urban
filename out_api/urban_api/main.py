from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from routes.account import account
from routes.login import login
from routes.mail_code import mail_code
from routes.match import match,match2
from routes.password import password,password2
from routes.password_code import password_code
from routes.team import team
from routes.user import user

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(account,"/account")
api.add_resource(login,"/login")
api.add_resource(mail_code,"/mail_code")
api.add_resource(match,"/match")
api.add_resource(match2,"/match2")
api.add_resource(password,"/password")
api.add_resource(password2,"/password2")
api.add_resource(password_code,"/password_code")
api.add_resource(team,"/team")
api.add_resource(user,"/user")

if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')