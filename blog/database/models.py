from blog.database.db import data
from datetime import datetime

class User(data.Model):
    __tablename__ = 'user'
    id = data.Column(data.Integer, primary_key=True)
    full_name = data.Column(data.String(50), nullable=False)
    email = data.Column(data.String(), unique=True, nullable=False)
    username = data.Column(data.String(20), index=True, unique=True, nullable=False)
    password = data.Column(data.String(), nullable=False)

    admin = data.Column(data.Boolean, default=False)


    def __repr__(self) -> str:
        return f'<User> -> {self.username}'

class Category(data.Model):
    __tablename__ = 'category'

    id = data.Column(data.Integer, primary_key=True)
    name = data.Column(data.String(25), index=True, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<Category> -> {self.name}'

class Post(data.Model):
    __tablename__ = 'post'

    id = data.Column(data.Integer, primary_key=True)

    title = data.Column(data.String, nullable=False)
    slug = data.Column(data.String, nullable=False)

    user_id = data.Column('author', data.Integer, data.ForeignKey('user.id'))
    user = data.relationship('User', foreign_keys=user_id)

    abstract = data.Column(data.Text, nullable=False)
    content = data.Column(data.Text, nullable=False)

    created = data.Column(data.DateTime, nullable=False, default=datetime.utcnow)
    last_edit = data.Column(data.DateTime, default=datetime.utcnow)

    category_id = data.Column('category' ,data.Integer, data.ForeignKey('category.id'))
    category = data.relationship('Category', foreign_keys=category_id)
