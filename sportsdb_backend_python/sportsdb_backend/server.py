from ariadne import QueryType, ObjectType, gql, make_executable_schema
from ariadne.asgi import GraphQL

from sportsdb_backend.api import query


schema = make_executable_schema(query.type_defs(), query.type())
app = GraphQL(schema)
