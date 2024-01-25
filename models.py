# models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    image = Column(String)
    details = Column(String)
    download_link = Column(String)

class Series(Base):
    __tablename__ = 'series'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    image = Column(String)
    details = Column(String)
    download_link = Column(String)
    episodes = relationship('Episode', back_populates='series')

class Episode(Base):
    __tablename__ = 'episodes'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    season = Column(Integer)
    episode_number = Column(Integer)
    series_id = Column(Integer, ForeignKey('series.id'))
    details = Column(String)
    download_link = Column(String)
    series = relationship('Series', back_populates='episodes')

class TopOne(Base):
    __tablename__ = 'topones'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    image = Column(String)
    details = Column(String)
    download_link = Column(String)

engine = create_engine('sqlite:///media_database.db')

Base.metadata.create_all(engine)
