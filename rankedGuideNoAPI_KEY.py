import requests


debug = False
api_key = 'YOUR-API-KEY'

def request_summoner_data(region, summoner_name, api_key):
    url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key
    response = requests.get(url)
    return response.json()

def request_ranked_data(region, summoner_id, api_key):
    url = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + summoner_id + "?api_key=" + api_key
    response = requests.get(url)
    return response.json()

def request_solo_queue_summoners_rift_rank(ranked_data_response_json):
    for queueType in ranked_data_response_json:
        if (str(queueType['queueType']) == "RANKED_SOLO_5x5"):
            print("Queue Type: " + str(queueType['queueType']))
            print("Tier: " + str(queueType['tier']) + " Rank: " + str(queueType['rank']) + " Points: " + str(queueType['leaguePoints']))

def request_flex_queue_summoners_rift_rank(ranked_data_response_json):
    for queueType in ranked_data_response_json:
        if (str(queueType['queueType']) == "RANKED_FLEX_SR"):
            print("Queue Type: " + str(queueType['queueType']))
            print("Tier: " + str(queueType['tier']) + " Rank: " + str(queueType['rank']) + " Points: " + str(queueType['leaguePoints']))

def request_flex_queue_twisted_treeline_rank(ranked_data_response_json):
    for queueType in ranked_data_response_json:
        if (str(queueType['queueType']) == "RANKED_FLEX_TT"):
            print("Queue Type: " + str(queueType['queueType']))
            print("Tier: " + str(queueType['tier']) + " Rank: " + str(queueType['rank']) + " Points: " + str(queueType['leaguePoints']))


if (debug):
    region = "na1"
    summoner_name = "naruza"
else:
    region = input("Enter a region: ")
    summoner_name = input("Enter your summoner name: ")





summoner_response_json = request_summoner_data(region, summoner_name, api_key)
ranked_data_response_json = request_ranked_data(region, str(summoner_response_json['id']), api_key)


print(summoner_response_json)
print(ranked_data_response_json)
request_solo_queue_summoners_rift_rank(ranked_data_response_json)
#request_flex_queue_summoners_rift_rank(ranked_data_response_json)
#request_flex_queue_twisted_treeline_rank(ranked_data_response_json)




input()