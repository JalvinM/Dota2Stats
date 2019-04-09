from Api import api

MY_ID = '28256361'

def get_match_hist():
    return api.do_get('IDOTA2Match_570/GetMatchHistory/v001/',{})

def get_match_hist_acc(accid):
    return api.do_get('IDOTA2Match_570/GetMatchHistory/v001/',{'account_id': accid})

def get_match_list_acc(accid):
    match_hist = get_match_hist_acc(MY_ID)
    d = match_hist['result']['matches']
    match_list = {i["match_id"] for i in d}
    return match_list

print(get_match_list_acc(MY_ID))

