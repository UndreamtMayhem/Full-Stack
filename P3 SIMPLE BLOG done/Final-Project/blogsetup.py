# Python dependencies
import os
import sys
import enum

# SQL ALCHEMY DEPENDENCIES
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DATETIME, Enum, Boolean, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


'''
todo? build a followers table

class Following(Base):
    # PK
    id = Column(Integer, primary_key=True)
    #user

'''


class Gender(enum.Enum):
    male = 1
    female = 2

class Users(Base):
    __tablename__ = 'user'
    # PK
    id = Column(Integer, primary_key=True)
    #Fields
    about = Column(String(150), nullable=False)

    # need to make a table
    #blogs_following = Column(ARRAY(String))

    email = Column(String(100), nullable=False, unique=True)
    # default let user edit later
    facebook_link = Column(String(80), nullable=False)

    first_name = Column(String(80), nullable=False)

    gender = Column(Enum(Gender))

    last_name = Column(String(80), nullable=False)

    linkedin_link = Column(String(80), nullable=False)

    password = Column(String(90), nullable=False)

    pininterest_link = Column(String(80), nullable=False)

    profile_pic = Column(String(80), nullable=False)

    salt = Column(String(10), nullable=False)

    snapchat_link = Column(String(80), nullable=False)

    twitter_link = Column(String(80), nullable=False)

    #  need to make a new table
    #tags = Column(ARRAY(String))

    username = Column(String(80), nullable=False, unique=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'about': self.about,
            #'blogs_following': self.blogs_following,
            'email': self.email,
            'facebook_link': self.facebook_link,
            'first_name': self.first_name,
            'gender': self.gender,
            'last_name': self.last_name,
            'linkedin_link': self.linkedin_link,
            'pininterest_link': self.pininterest_link,
            'profile_pic': self.profile_pic,
            'snapchat_link': self.snapchat_link,
            'twitter_link': self.twitter_link,
            'username': self.username,
            'id': self.id,
        }


class Tag(Base):
    __tablename__ = 'tag'

    # PK
    id = Column(Integer, primary_key=True)
    tagname = Column(String(100), nullable=False, unique=True)
    
    @property
    def serialize(self): 
        return {
            'tag': self.tagname,
            'id': self.id,
        }


class Blog(Base):
    __tablename__ = 'blog'
    # PK
    id = Column(Integer, primary_key=True)

    # FK
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)

    tag_id = Column(Integer, ForeignKey('tag.id'))
    tag = relationship(Tag)

    # FIELDS
    body = Column(Text(2500), nullable=False)
    caption = Column(String(100), nullable=False)
    date_uploaded = Column(DATETIME(), nullable=False)
    description = Column(String(150), nullable=False)
    likes = Column(Integer, nullable=False)
    name = Column(Text(100), nullable=False)
    image_url = Column(String(250), nullable=False)
    is_public = Column(Boolean, nullable=False)
    title = Column(String(100), nullable=False)

    @property
    def serialize(self): 
        return {
            'blog_body': self.body,
            'blog_caption': self.caption,
            'date_uploaded': self.date_uploaded,
            'blog_description': self.description,
            'blog_likes': self.likes,
            'blog_name': self.name,
            'blog_image_url': self.image_url,
            'blog_title': self.title,
            'id': self.id,
        }




engine = create_engine('sqlite:///userblogs.db')

Base.metadata.create_all(engine)