from fyers_apiv3 import fyersModel
import webbrowser
import config


def authenticate():
    session = fyersModel.SessionModel(
        client_id=config.FYERS_CLIENT_ID,
        secret_key=config.FYERS_SECRET_KEY,
        redirect_uri=config.FYERS_REDIRECT_URI,
        response_type="code"
    )

    # Step 1: Generate and open auth URL
    auth_url = session.generate_authcode()
    webbrowser.open(auth_url)

    # Step 2: Manual auth code input
    auth_code = input("Enter auth code: ").strip()

    # Step 3: Generate access token
    session.set_token(auth_code)
    token_response = session.generate_token()

    access_token = token_response["access_token"]

    # Step 4: Create FYERS client
    fyers = fyersModel.FyersModel(
        client_id=config.FYERS_CLIENT_ID,
        token=access_token,
        log_path="logs/"
    )

    return fyers
