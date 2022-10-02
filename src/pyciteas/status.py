from src.pyciteas.request import request

class Status:
    """
    Class to structure response from CiteAs status endpoint request.

    Reference: https://citeas.org/api#api-status-object

    Attributes
    ----------
    documentation_url : str
        CiteAs API documentation URL.
    msg : str
        A wise message from the status endpoint.
    version : str
        CiteAs API version.

    """

    def __init__(self, data):
        """
        Parameters
        ----------

        data : dict
            Request data parsed as dict from request()
        """
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
    """
    Make a request against the status endpoint of the CiteAs API.

    Raises
    ------
    ValueError
        If the request returns a non-200 status code, there is no data returned
        and therefore nothing to be parsed.

    Returns
    -------
    Status
        A Status object containing the response of the status request.
    """

    data = request()

    if not data:
        raise ValueError('No data returned')

    return Status(data)
