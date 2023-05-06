#Import Statements
import random
import requests
import os
from requests_oauthlib import OAuth1Session
from datetime import datetime

##API Access Information -- This should be kept secret
API_KEY = "32fsZ54tkFXW6jbRZB3PpgLKLsMM4szT"
API_SECRET = "9Qj82Cfrfw9LQgNhZnXVTGTJVXPrkQ9X5hJppH2cdNJrXzTX7xhQpKmtVVmdcFx3"
USER_NICKNAME = "nearlovingsbend"
ACCESS_TOKEN = "tGh4TpzF3BpvmkZd3sVZhg8XX57RQ92X"
ACCESS_TOKEN_SECRET = "PDpT9f78N7WnDrhrGC2TcBf28zBDhSTkdpxzh445jPMx5MBG6ZPgxpjtVLS5sdtq"
#specify file save path
save_path = "C:\\Users\\jared\\Desktop\\SmugMug\\image_returns"
#authenticate to smugmug
smugmug = OAuth1Session(API_KEY, client_secret=API_SECRET, resource_owner_key=ACCESS_TOKEN, resource_owner_secret=ACCESS_TOKEN_SECRET)


# Make an API call to fetch your albums
headers = {'Accept': 'application/json'}
ALBUMS_URL = f'https://api.smugmug.com/api/v2/user/{USER_NICKNAME}/!albums'
response = smugmug.get(ALBUMS_URL, headers=headers)
##debug statements
if response.status_code != 200:
    print(f"Error fetching albums. Status code: {response.status_code}")
    print("Response content:", response.content)
    exit()
##error handling
try:
    albums = response.json()['Response']['Album']
except ValueError as e:
    print(f"Error parsing JSON response: {e}")
    print("Response content:", response.content)
    exit()

# Choose a random album
random_album = random.choice(albums)
album_uri = 'https://api.smugmug.com' + random_album['Uris']['AlbumImages']['Uri']

# Make an API call to fetch the images within the selected album
response = smugmug.get(album_uri, headers=headers)

if response.status_code != 200:
    print(f"Error fetching images. Status code: {response.status_code}")
    print("Response content:", response.content)
    exit()

try:
    images = response.json()['Response']['AlbumImage']
except ValueError as e:
    print(f"Error parsing JSON response: {e}")
    print("Response content:", response.content)
    exit()

# Choose a random image and retrieve its details
random_image = random.choice(images)
image_url = random_image['ArchivedUri']
image_description = random_image['Caption']

print("Random image URL:", image_url)
print("Image Description", image_description)

# Create a folder with the current date in the specified path
date_str = datetime.now().strftime('%Y-%m-%d')
folder_path = os.path.join(save_path,date_str)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Download the image and save it as a JPEG file
response = requests.get(image_url)
image_filename = os.path.join(folder_path, f"{random_image['ImageKey']}.jpeg")
with open(image_filename, 'wb') as f:
    f.write(response.content)

# Save the caption as a TXT file
caption_filename = os.path.join(folder_path, f"{random_image['ImageKey']}.txt")
with open(caption_filename, 'w') as f:
    f.write(image_description)