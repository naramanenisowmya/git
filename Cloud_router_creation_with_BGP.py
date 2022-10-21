"""
//organization : Sonata-software-Limited
//developed by : python team
//code         : cloud_router_creation with BGP
//created on   : 18-10-2022
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

router_body = {
    "name": input("Enter your router name:"),
    "network": input("Enter your Network Name like below formate \nglobal/networks/NETWORK-NAME:\n-->"),
    "bgp": {
        "asn": input("Enter your asn number:"),  # 65500
        "advertiseMode": "CUSTOM",
        "advertisedGroups": [
            "ALL_SUBNETS"
        ]
    },
    "bgpPeers": [
        {
            "name": input("Enter your bgpPeer name:"),  # bgp
            "enableIpv6": False,
            "bfd": {
                "sessionInitializationMode": "DISABLED",
                "multiplier": 5,
                "minTransmitInterval": 1000,
                "minReceiveInterval": 1000
            },
            "interfaceName": input("Enter your interface name:"),  # if-bgp
            "peerIpAddress": input("Enter your peerIpAddress:"),  # 169.254.0.2
            "peerAsn": 65501,
            "advertiseMode": "DEFAULT",
            "enable": "TRUE",
            "ipAddress": "169.254.0.1"
        }
    ],
    "interfaces": [
        {
            "name": "if-bgp",
            # "ipRange": "169.254.0.1/30",
            "linkedVpnTunnel": input("Enter your linkedVpnTunnel like below format "
                                     "\nprojects/bubbly-bastion-358405/regions/us-central1/vpnTunnels/TUNNEL NAME"
                                     "\n-->")
        }
    ]

    # "selfLink": "projects/bubbly-bastion-358405/regions/us-central1/routers/royal"
}
request = service.routers().insert(project=project, region=region, body=router_body)
response = request.execute()

pprint(response)
