from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DisplayNames(Base):
    __tablename__ = 'display_names'
    id = Column(Integer, primary_key=True)
    language = Column(String)
    entity_type = Column(String)
    entity_id = Column(Integer)
    full_name = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    alias = Column(String)
    abbreviation = Column(String)
    short_name = Column(String)
    prefix = Column(String)
    suffix = Column(String)

    def __repr__(self):
       return f"<User(fullname='{self.full_name}')>"
