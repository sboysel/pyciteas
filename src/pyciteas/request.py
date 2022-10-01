import json
import urllib3
from src.pyciteas.config import Config

def request(product=None):
    """Make a request against CiteAs API"""

    cfg = Config()
    http = urllib3.PoolManager()

    if product:
        url = f'https://api.citeas.org/product/{product}'
    else:
        url = f'https://api.citeas.org/'

    try:
        r = http.request(
            'GET',
            url,
            fields={'email': cfg.email}
        )
        return json.loads(r.data.decode('utf-8'))
    except urllib3.exceptions.HTTPError as e:
        print('Request failed:', e.reason)
        return None
