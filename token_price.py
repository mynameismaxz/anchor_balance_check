from terra_sdk.client.lcd import LCDClient
import config
import constants.token_mainnet as token

terra = LCDClient(chain_id=config.chainId,
                  url=config.publicNodeUrl)

# getting token contact from pair
swap_query_contract = terra.wasm.contract_query(token.TERRASWAP_PAIR["MINE-UST"], {
    "pool": {},
})

token_addr = swap_query_contract['assets'][0]['info']['token']['contract_addr']

token_query = terra.wasm.contract_query(token.TERRASWAP_PAIR["MINE-UST"], {
    "simulation": {
        "offer_asset": {
            "amount": "1000000",
            "info": {
                "token": {
                    "contract_addr": token_addr
                }
            }
        }
    }
})

token_price = int(token_query["return_amount"])/1000000

print("MINE Price: %f UST" % (token_price))