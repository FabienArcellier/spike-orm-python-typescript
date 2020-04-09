import io
import os

from ariadne import QueryType, gql

from sportsdb_backend import datastore, ROOT_DIR
from sportsdb_backend.entities import t_american_football_defensive_stats, t_display_names

query = QueryType()

# not very good to instanciate here, every query use the same connection
engine = datastore.get_engine()
session = datastore.get_session(engine)

def type_defs():
    schema_path = os.path.join(ROOT_DIR, 'schema', 'query.graphql')
    with io.open(schema_path) as file_content:
        schema = file_content.read()

    return gql(schema)

@query.field("players")
def resolve_players(obj, info):
    return session.query(t_display_names).filter(t_display_names.columns.entity_type=='persons').limit(20)

@query.field("american_football_defensive_stats")
def resolve_american_football_defensive_stats(obj, info):
    return session.query(t_american_football_defensive_stats).limit(20)

def type():
    return query
