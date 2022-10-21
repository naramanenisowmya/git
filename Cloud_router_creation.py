"""
//organization : Sonata-software-Limited
//developed by : python team
//code         : cloud_router_creation
//created on   : 17-10-2022
//code language: python
 """


from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = input('Enter_your_project_id:')
# Name of the region for this request.
region = input("Enter your region:")

router_body = dict(name=input("Enter your router name:"),
                   network=input("Enter your Network Name like below formate \nglobal/networks/NETWORK-NAME:\n-->"),
                   bgp={
                       "asn": input("Enter your asn number:"),  # 65500
                       "advertiseMode": "CUSTOM",
                       "advertisedGroups": [
                           "ALL_SUBNETS"
                       ]
                   })
request = service.routers().insert(project=project, region=region, body=router_body)
response = request.execute()

pprint(response)

