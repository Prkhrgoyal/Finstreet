from fyers_apiv3 import fyersModel, accessToken
import webbrowser
import config

def authenticate():
    session = accessToken.SessionModel(
        client_id=config.FYERS_CLIENT_ID,
        secret_key=config.FYERS_SECRET_KEY,
        redirect_uri=config.FYERS_REDIRECT_URI,
        response_type="code",
        grant_type="authorization_code"
    )

    auth_url = session.generate_authcode()
    webbrowser.open(auth_url)

    auth_code = input("Enter auth code: ")
    session.set_token(auth_code)

    token = session.generate_token()["access_token"]

    fyers = fyersModel.FyersModel(
        client_id=config.FYERS_CLIENT_ID,
        token=token,
        log_path="logs/"
    )
    return fyers
