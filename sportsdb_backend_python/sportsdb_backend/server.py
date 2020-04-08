from ariadne import QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

from sportsdb_backend import datastore

engine = datastore.get_engine()
session = datastore.get_session(engine)

type_defs = gql("""type Query { hello: String! }""")

query = QueryType()

schema = make_executable_schema(type_defs, query)
app = GraphQL(schema)
