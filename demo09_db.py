"""
  Created by Even on 2019-6-15
"""
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)
# 创建数据库管理对象
db = SQLAlchemy(app)
# 创建flask脚本管理工具对象
manager = Manager(app)
# 创建数据库迁移工具对象
migrate = Migrate(app, db)
# 想manager对象注册db命令，这样命令行才能支持
manager.add_command('db', MigrateCommand)


# 配置数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/gz1901_python_web'
# 配置跟踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 配置数据库操作相关的回显
app.config['SQLALCHEMY_ECHO'] = True


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    passwd = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.username


if __name__ == "__main__":
    manager.run()