import requests

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=mUO2S2kEycLh24qiFNZW8XMeXCgHghVeGnF1FgyO"

response = requests.get(url)

print(response.json())