"""
//organization : Sonata-software-Limited
//developed by : python team
//code         : cloud_router_list
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
# Name of the region.
region = input("Enter your region:")

request = service.routers().list(project=project, region=region)
while request is not None:
    response = request.execute()

    for router in response['items']:
        pprint(router)

    request = service.routers().list_next(previous_request=request, previous_response=response)

