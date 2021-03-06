from token_class import Token
from session_class import Session
from token_types_class import tokenTypes

class URL(Token):
    def __init__(self, session: Session, name: str, description: str = None, message: str = None):
        super().__init__(session, name, tokenTypes.URL, description, message)
        self.path = None

    def create_token(self, ip, port = None) -> str:
        if port == None:
            self.path = 'http://' + ip + '/token?type=url&id=' + self.token_id
            return 'http://' + ip + '/token?type=url&id=' + self.token_id
        else:
            self.path = 'http://' + ip + ':' + port + '/token?type=url&id=' + self.token_id
            return 'http://' + ip + ':' + port + '/token?type=url&id=' + self.token_id


if __name__ == "__main__":
    print(URL.create_token('145.123.45.123', '38j1s89j21js18', "3000"))
    print(URL.create_token('145.123.45.123', '38j1s89j21js18'))