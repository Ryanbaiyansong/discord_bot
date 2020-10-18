import os
import json
import requests
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# THIS HANDLES NO ERRORS AND IS JUST A RAW CONNECTION TO THE LOL API;
# USE THE API MODULE TO GET ERROR FALLBACK METHODS

with open(os.path.join(__location__, 'config'), 'r') as f:
    try:
        config = json.load(f)
    except ValueError:
        config = {'champggKey': ""}

KEY = config["champggKey"]
ENDPOINT = "http://api.champion.gg/"


def get_matchups(champName):
	"""
	Retrieves matchup data for a champion
	"""

	return requests.get(ENDPOINT + "champion/" + champName + \
		"/matchup?api_key=" + KEY)