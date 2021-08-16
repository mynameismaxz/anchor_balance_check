# configuration file
import os

# terra configuration
terra_wallet_addr = os.environ.get("WALLET", "")
chainId = "columbus-4"                              # MainNet -> if testnet, using tequila-0004
publicNodeUrl = "https://lcd.terra.dev"             # MainNet -> if testnet, using https://tequila-fcd.terra.dev
anchorTerraContract = "terra1hzh9vpxhsk8253se0vv5jj6etdvxu3nv8z07zu"
marketTerraContract = "terra1sepfj7s0aeg5967uxnfk4thzlerrsktkpelm5s"
overseerTerraContract = "terra1tmnqgvg567ypvsvk6rwsga3srp7e3lg6u0elp8"

# sender notfication
# TODO: Send to line notification

# development flag
develop_mode = False
