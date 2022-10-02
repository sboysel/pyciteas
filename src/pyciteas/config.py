import configparser

class Config:
    """
    Class for parsing the pyciteas config (e.g. email address)
    """
    def __init__(self):
        """
        Attributes
        ----------
        config : configparser.ConfigParser
            Parsed config.
        email : str
            Email address requests against CiteAs API will be associated with.
            Default is <test@example.com>.
        """
        self.config = configparser.ConfigParser()
        self.config.read('pyciteas.ini')
        try:
            self.email = self.config['pyciteas']['email']
        except:
            self.email = 'test@example.com'
