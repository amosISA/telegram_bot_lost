class TokenManager:
    
    @staticmethod
    def getToken(filepath):
        file = open(filepath,'r')
        token = file.read()
        file.close()
        return token

