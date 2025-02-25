from conn import DynamoDBClient
from jmutils import show
db = DynamoDBClient()

response = db.client.list_tables()

show(response['TableNames'])