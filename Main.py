# import libraries
#pip install pystac-client sat-search 
from pystac_client import Client

LandsatSTAC = Client.open("https://landsatlook.usgs.gov/stac-server", headers=[])

for collection in LandsatSTAC.get_collections():
    print(collection)
# functions
# new
#new
#try