"""
//organization : Sonata-software-Limited
//developed by : python team
//code         : route_deletion
//created on   : 11-10-2022
//code language: python
 """


from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = input('Enter_your_project_id:')

# Name of the Route resource to delete.
route = input("Enter your route name to delete.:")

request = service.routes().delete(project=project, route=route)
response = request.execute()

pprint(response)