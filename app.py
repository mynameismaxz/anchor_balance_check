from terra_sdk.client.lcd import LCDClient
import config

terra = LCDClient(chain_id=config.chainId, url=config.publicNodeUrl)

print('-' * 50)
print("Welcome: %s" % (config.terra_wallet_addr))

anchorDeposit = terra.wasm.contract_query(config.anchorTerraContract, {
    "balance": {
        "address": config.terra_wallet_addr,
    }
})

aUstBalance = int(anchorDeposit['balance'])/1000000

deposit = terra.wasm.contract_query(config.marketTerraContract, {
    "epoch_state": {},
})

deposit_money = float(aUstBalance) * float(deposit['exchange_rate'])
print("Total deposit: %.4f UST" %(deposit_money))
print("-" * 50)

if config.develop_mode:
    print("aUST exchange rate: %s\naTerra supply: %s" % (deposit['exchange_rate'], deposit['aterra_supply']))
    overseer = terra.wasm.contract_query(config.overseerTerraContract, {
        "epoch_state": {},
    })