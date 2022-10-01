from src.pyciteas.status import Status

def test_status():
    s = Status()
    assert s.documentation_url == 'https://citeas.org/api'
    assert s.msg == "Don't panic"
