# import libraries
#pip install pystac-client sat-search 
import requests
import rasterio

# Set the URL of the Landsat API
api_url = 'https://api.landsat-pds.eosdis.nasa.gov/landsat/api/v1/assets/'

# Set the parameters for the API request
params = {
    'lat': 44.05,  # latitude of the location you want to download data for
    'lon': -121.3,  # longitude of the location you want to download data for
    'date': '2022-01-01',  # start date of the period you want to download data for
    'end_date': '2022-11-30',  # end date of the period you want to download data for
    'cloud_max': 20,  # maximum percentage of clouds allowed in the images
    'bands': 'B4,B6',  # bands to download (Band 4 and Band 6 in this case)
}

# Send the request to the Landsat API
response = requests.get(api_url, params=params)

# Check the status code of the response
if response.status_code == 200:
    # Get the download URL for the first scene in the list
    download_url = response.json()['results'][0]['download_url']

    # Download the data using the download URL
    data = requests.get(download_url)

    # Save the data to a file
    with open('landsat8_image.tar.gz', 'wb') as f:
        f.write(data.content)
else:
    print('Request failed')

# Extract the contents of the tar.gz file
import tarfile

with tarfile.open('landsat8_image.tar.gz', 'r:gz') as tar:
    tar.extractall()

# Open the Band 4 and Band 6 images using rasterio
with rasterio.open('LC08_L1TP_019036_20221231_20221231_01_T1_B4.TIF') as src_b4:
    band4 = src_b4.read()

with rasterio.open('LC08_L1TP_019036_20221231_20221231_01_T1_B6.TIF') as src_b6:
    band6 = src_b6.read()

# Calculate the modified normalized water index
mndwi = (band4 - band6) / (band4 + band6)

import requests
from requests.adapters import HTTPAdapter

# Set the number of retries to 5
adapter = HTTPAdapter(max_retries=5)

# Create a session with the adapter
session = requests.Session()
session.mount('https://', adapter)

# Send the request using the session
response = session.get(api_url, params=params)


# new
#new
#try