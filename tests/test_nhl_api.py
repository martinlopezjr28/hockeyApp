# tests/test_nhl_api.py

from nhl_api import get_player_stats, parse_player_stats

def test_get_player_stats():
    player_id = 8478445
    data = get_player_stats(player_id)
    assert data is not None

def test_parse_player_stats():
    api_response = {"featuredStats":{
        "regularSeason":{
            "subSeason":{
                'goals': 10, 'assists': 20
                }
            }
            }
        }
    stats_types = ['goals', 'assists']
    
    stats = parse_player_stats(api_response,stats_types)
    assert stats == {'goals': 10, 'assists': 20}