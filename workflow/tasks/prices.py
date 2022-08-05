from director import task
from ..coinrequest import BTCPrice

@task(name="GET_BTC_PRICE")
def get_btc_price(*args, **kwargs):
    return {'prices': BTCPrice.get_btc_prices()}

@task(name="PROCESS_PRICES")
def process_prices(*args, **kwargs):
    return {'price_json': BTCPrice.process_prices(args[0].get('prices'))}

@task(name="SEND_MAIL")
def send_mail(*args, **kwargs):
    return BTCPrice.compose_price_email(args[0].get('price_json'))

