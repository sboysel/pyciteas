import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('pyciteas.ini')
        try:
            self.email = self.config['pyciteas']['email']
        except:
            self.email = 'test@example.com'

# if __name__ == '__main__':
#     c = Config()
#     print(f'email: {c.email}')
