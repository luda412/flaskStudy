from pathlib import Path
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 전역으로 인스턴스만 만든 뒤, 실제 초기화는 create_app 안에서
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # 설정
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # 확장 초기화
    db.init_app(app)
    migrate.init_app(app, db)

    # 라우트는 여기 안에서 정의
    @app.route("/")
    def index():
        return "Hello world!"

    @app.route("/hello/<name>")
    def say_hello(name):
        print(f"type is {type(name)}")
        return render_template("index.html", name=name)

    # 반드시 app 반환
    return app
