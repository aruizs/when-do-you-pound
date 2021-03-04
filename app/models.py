from . import db


class Credential(db.Model):
    __tablename__ = 'credentials'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='credential', lazy='dynamic')

    def __repr__(self):
        return '<Credential %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    credential_id = db.Column(db.Integer, db.ForeignKey('credentials.id'))

    def __repr__(self):
        return '<User %r>' % self.username
