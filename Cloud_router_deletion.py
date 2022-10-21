"""
//organization : Sonata-software-Limited
//developed by : python team
//code         : cloud_router_deletion
//created on   : 20-10-2022
//code language: python
 """


from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = input('Enter_your_project_id:')

# Name of the Router resource to delete.
router = input("Enter your cloud router name to delete:")
# Name of the region.
region = input("Enter your region:")
print(router)
print("deleting router...\n")

request = service.routers().delete(project=project, region=region, router=router)
response = request.execute()

pprint(response)
