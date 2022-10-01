from src.pyciteas.status import status

def test_status():
    s = status()
    assert s.documentation_url == 'https://citeas.org/api'
    assert s.msg == "Don't panic"
