# Anchor protocol balance check.
This repository aims to checking balance from [Anchor farming](https://anchorprotocol.com/)

## Prerequisite.
- Python v3.8+ (We're testing on python 3.8 because requirement of terra-sdk is 3.7+.)

## How to use?
- Install package that need to use.
``` 
$ pip install -r requirements.txt 
```

- Set the environment *WALLET=terra...* variable with your terra wallet or edit file `config.py` in line 5 section `<Put your wallet address here!>`
``` 
$ export WALLET=terra... 
```

- Start `app.py` to run balance check.
``` 
$ python app.py 
```

## TODO:
- [ ] Integrated with 3rd party notify (eg. line-notify, discord, telegram).
- [ ] Looking for arbitrage coins on terra.

## License
Copyright © 2021 mynameismaxz. This project is Unlicense licensed.