from src.main import db


class User(db.Model):
    """用户信息表"""
    __tablename__ = "tb_user"

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(8), comment="用户id")
    birth_date = db.Column(db.Integer, comment="出生日期")
    sex = db.Column(db.Integer, comment="性别")
    height = db.Column(db.Integer, comment="身高")
    weight = db.Column(db.Float, comment="体重")
    create_time = db.Column(db.Integer, comment="创建时间")


class Weight(db.Model):
    """体重表"""
    __tablename__ = "tb_weight"

    uid = db.Column(db.String(8), comment="用户id")
    weight = db.Column(db.Float, comment="体重")
    create_time = db.Column(db.Integer, comment="创建时间")