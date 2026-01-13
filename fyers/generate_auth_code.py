from fyers_apiv3 import fyersModel

client_id = "DBFHNZB15F-100"  # e.g. ABCD12-100
redirect_uri = "http://127.0.0.1:5000/callback"

session = fyersModel.SessionModel(
    client_id=client_id,
    redirect_uri=redirect_uri,
    response_type="code"
)

auth_url = session.generate_authcode()
print("Open this URL in your browser:\n")
print(auth_url)
