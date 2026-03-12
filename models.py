from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime

db = SQLAlchemy()

class StudentGroup(db.Model):
    __tablename__ = 'student_groups'
    
    id = db.Column(db.Integer, primary_key=True)
    students = db.Column(JSONB, nullable=False, default=list) 
    
    def __repr__(self):
        count = len(self.students) if self.students else 0
        return f'<Группа №{self.id} (студентов: {count})>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'students': self.students or [],
        }