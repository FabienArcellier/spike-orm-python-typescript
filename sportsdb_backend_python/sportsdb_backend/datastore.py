import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.strategies import EngineStrategy


def get_engine() -> EngineStrategy:
    datastore_host = os.getenv('DATASTORE_HOST', 'localhost')
    engine = create_engine(f'postgresql://postgresql:1234@{datastore_host}/sportsdb', echo=True)
    return engine

def get_session(engine: EngineStrategy) -> sessionmaker:
    session = sessionmaker(bind=engine)
