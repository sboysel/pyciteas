import json
import urllib3
from src.pyciteas.config import Config

def request(product=None):
    """
    Make a request against CiteAs API.

    Parameters
    ----------
    product : str or None
        Product or item to query (e.g. URL or DOI).  If product is None, then
        the status endpoint is queried.

    Returns
    -------
    data : dict or None
        Response of the request parsed as a dict.  If the request returns a
        non-200 status code, None is returned.
    """

    cfg = Config()
    http = urllib3.PoolManager()
    url = 'https://api.citeas.org/'

    if product:
        url = f'https://api.citeas.org/product/{product}'

    try:

        r = http.request('GET', url, fields={'email': cfg.email})

        return json.loads(r.data.decode('utf-8'))

    except urllib3.exceptions.HTTPError as e:

        print('Request failed:', e.reason)

        return None
