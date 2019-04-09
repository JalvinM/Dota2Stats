from Api import api

MY_ID = '4559363087'

def get_match_details():
    return api.do_get('IDOTA2Match_570/GetMatchDetails/v001/',{})

def get_match_details_id(match_id):
    return api.do_get('IDOTA2Match_570/GetMatchDetails/v001/',{'match_id': match_id})

print(get_match_details_id(MY_ID))