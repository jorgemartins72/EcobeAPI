import boto3
import json
from config import settings

class DynamoDBClient:
	def __init__(self):
		self.client = None
		self.get_client()

	def get_client(self):
		self.client = boto3.client(
			'dynamodb',
			region_name=settings.AWS_REGION,
			aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
			aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
		)

