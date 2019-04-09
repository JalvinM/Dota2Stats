import api

MY_ID = '28256361'

def get_match_hist():
    return api.do_get('IDOTA2Match_570/GetMatchHistory/v001/',{})

def get_match_hist_id(accid):
    return api.do_get('IDOTA2Match_570/GetMatchHistory/v001/',{'account_id': accid})

print(get_match_hist_id(MY_ID))