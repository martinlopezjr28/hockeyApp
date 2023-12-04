import requests as req
import logging as log

logger = log.getLogger(__name__)

def get_player_stats(player_id):
    base_url = "https://api-web.nhle.com/v1/player"
    endpoint = f"/{player_id}/landing"

    # params = {
    #     None
    # }

    try:
        response = req.get(base_url + endpoint)
        response.raise_for_status()

        if response.status_code == 200:
            return response.json()
        else: 
            print(f'Error: {response.status_code}')
            logger.warning(f"Unexpected status code: {response.status_code}")
            return None
        
    except req.RequestException as e:
        logger.error(f"Error making API requests: {e}")

def parse_player_stats(api_response, stats_types):

    player_stats = {}

    for stat_type in stats_types:
        if stat_type in api_response["featuredStats"]["regularSeason"]["subSeason"]:
            player_stats[stat_type] = api_response["featuredStats"]["regularSeason"]["subSeason"][stat_type]

    return player_stats