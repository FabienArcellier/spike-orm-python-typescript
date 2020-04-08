import os

from sqlalchemy import create_engine
from sqlalchemy.engine.strategies import EngineStrategy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


def get_engine() -> EngineStrategy:
    datastore_host = os.getenv('DATASTORE_HOST', 'localhost')
    engine = create_engine(f'postgresql://postgres:1234@{datastore_host}/sportsdb', echo=True)
    return engine

def get_session(engine: EngineStrategy) -> Session:
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
