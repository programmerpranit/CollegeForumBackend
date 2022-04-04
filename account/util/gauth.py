from google.oauth2 import id_token
from google.auth.transport import requests

CLIENT_ID = "855467182800-lb0n7pki7mb37j884nquqlrhgi08s4uu.apps.googleusercontent.com"

def getSub(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        userid = idinfo['sub']
        useremail = idinfo['email']

        data = {
            'sub' : userid,
            'email' : useremail
        }
        
        return data

    except ValueError:
        return None