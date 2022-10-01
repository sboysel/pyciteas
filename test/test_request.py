from src.pyciteas.request import request

def test_request_status():
    r = request()
    assert r['documentation_url'] == 'https://citeas.org/api'
    assert r['msg'] == "Don't panic"


def test_request_product():
    product = 'https://github.com/datacite/maremma'
    r = request(product)
    assert r['name'] == 'Maremma: a Ruby library for simplified network calls'
    assert r['url'] == 'https://github.com/datacite/maremma'
