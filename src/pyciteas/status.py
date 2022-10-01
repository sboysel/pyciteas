from src.pyciteas.request import request

class Status:
    """https://citeas.org/api#api-status-object"""
    def __init__(self):
        data = status()
        self.documentation_url = data['documentation_url']
        self.msg = data['msg']
        self.version = data['version']
    def __repr__(self):
        return 'Status()'
    def __str__(self):
        s = f'documentation_url: {self.documentation_url}\n'
        s += f'msg: {self.msg}\n'
        s += f'version: {self.version}'
        return s

def status():
    """Make a request against CiteAs API"""
    data = request()
    if not data:
        raise ValueError('No data returned')
    return data

if __name__ == '__main__':
    s = Status()
    print(s)
