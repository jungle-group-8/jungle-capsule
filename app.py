from flask import Flask
from routes.capsule import capsule_bp
from routes.auth import auth_bp
<<<<<<< HEAD
from dotenv import load_dotenv

=======
>>>>>>> 9fd3f3d (resolve conflicts)
from services.auth import login #blueprint사용 login.py import
from routes import capsule
from database import client   #database에서 client  변수 가져옴
from dotenv import load_dotenv
import os
from routes import capmaking,capsulelist,checkcap,deletecap,detailcpa,member,question
from services import imageupload



app = Flask(__name__)

load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")


app.register_blueprint(capmaking.capmaking)
app.register_blueprint(capsulelist.caplist)
app.register_blueprint(checkcap.checkcap)
app.register_blueprint(deletecap.deletecap)
app.register_blueprint(detailcpa.detailcap)
app.register_blueprint(member.members)
app.register_blueprint(question.question)
app.register_blueprint(imageupload.image_bp)

app.register_blueprint(capsule_bp)
app.register_blueprint(login.auth_bp)

app.config["S3_ACCESS_KEY"] = os.getenv("S3_ACCESS_KEY")
app.config["S3_SECRET_KEY"] = os.getenv("S3_SECRET_KEY")
app.config["S3_BUCKET"] = os.getenv("S3_BUCKET")

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5001, debug=True)
   