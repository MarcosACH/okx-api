import os
import json
import okx.Account as Account
from dotenv import load_dotenv

load_dotenv()


# API initialization
apikey = os.getenv('OKX_API_KEY')
secretkey = os.getenv('OKX_SECRET_KEY')
passphrase = os.getenv("OKX_PASSPHRASE")

flag = "0"  # Production trading:0 , demo trading:1

accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

# Get account balance
result = accountAPI.get_account_balance()

with open('balance.json', 'w') as file:
    file.write(json.dumps(result))
