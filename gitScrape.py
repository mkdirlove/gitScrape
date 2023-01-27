import argparse
import requests
import json

parser = argparse.ArgumentParser(description='Search for top 30 repositories on GitHub')
parser.add_argument('-q', '--query', help='Search query', required=True)
args = parser.parse_args()

if args.query:
    url = f"https://github-scraper.p.rapidapi.com/search_top30/{args.query}"
    headers = {
    "X-RapidAPI-Key": "18140c0733msh4177590f10ca716p1ba0c8jsnd344b761be19",
    "X-RapidAPI-Host": "github-scraper.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)

    #parse json data
    data = json.loads(response.text)

    print("""
   ▄▄ • ▪  ▄▄▄▄▄.▄▄ ·  ▄▄· ▄▄▄   ▄▄▄·  ▄▄▄·▄▄▄ .
 ▐█ ▀ ▪██ •██  ▐█ ▀. ▐█ ▌▪▀▄ █·▐█ ▀█ ▐█ ▄█▀▄.▀·
 ▄█ ▀█▄▐█· ▐█.▪▄▀▀▀█▄██ ▄▄▐▀▀▄ ▄█▀▀█  ██▀·▐▀▀▪▄
 ▐█▄▪▐█▐█▌ ▐█▌·▐█▄▪▐█▐███▌▐█•█▌▐█ ▪▐▌▐█▪·•▐█▄▄▌
 ·▀▀▀▀ ▀▀▀ ▀▀▀  ▀▀▀▀ ·▀▀▀ .▀  ▀ ▀  ▀ .▀    ▀▀▀ 
    """)
    for item in data:
        print(f" Name: https://github.com/{item['name']}")
        print(f" Description: {item['description']}")
        print()
else:
    parser.print_help(argparse._sys.stderr)
