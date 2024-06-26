from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.server import db

class User(db.Model):
    # membuat stuktur database
    id = db.Column(db.BigInteger, primary_key = True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(70), index=True, unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    role = db.Column(db.Enum('admin', 'user', name='role_enum'), nullable=False, default='user')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    # merepresentasikan Class User
    def __repr__(self):
        return '<User {}>'.format(self.name)
    
    def setPassword(self, password):
        self.password = generate_password_hash(password)
        
    def verifyPassword(self, password):
        return check_password_hash(self.password, password)