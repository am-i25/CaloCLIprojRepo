import argparse
import requests
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("topics", type=str)
parser.add_argument("orientation", type=str, choices=["landscape", "portrait"])
args = parser.parse_args()

access_key = "bENk092-ZYl-s-QU9bdG_xVJmqAfIIPpEg6Ssb3jM1A"
headers = {"Authorization": f"Client-ID {access_key}"}
params = {
    "query": args.topics,
    "orientation": args.orientation
}
response = requests.get("https://api.unsplash.com/search/photos", headers=headers, params=params)
data = response.json();

Path("pics").mkdir(exist_ok=True)
for result in data["results"]:
    pic_url = result["urls"]["full"]
    pic_id = result["id"]
    pic_response = requests.get(pic_url, headers=headers)
    pic_data = pic_response.content
    file_name = f"pics/{pic_id}.jpg"
    with open(file_name, "wb") as f:
        f.write(pic_data)