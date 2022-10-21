"""
//organization : Sonata-software-Limited
//developed by : python team
//code         : route_creation
//created on   : 10-10-2022
//code language: python
 """


from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = input('Enter_your_project_id:')
route_body = {
    "name": input("Enter your route name:"),
    "description": input("Enter your description:"),
    "network": input("Enter your Network Name like below formate \nglobal/networks/NETWORK-NAME:\n-->"),
    "destRange": input("Enter your destination IP range:"),
    "priority": "1000",  # priority level
    "nextHopGateway": input("Enter your next hoop:")

}
request = service.routes().insert(project=project, body=route_body)
response = request.execute()
print("creating route...\n")
pprint(response)


