from Api import api


def get_league_listing():
    return api.do_get('IDOTA2Match_570/GetLiveLeagueGames/V1/', {})


print(get_league_listing())
