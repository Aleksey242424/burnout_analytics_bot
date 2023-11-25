def check_referrals(ref_id:str,user_id:str):
    if ref_id.isdigit():
        if ref_id != user_id:
            return True
        else:
            return
    else:
        return