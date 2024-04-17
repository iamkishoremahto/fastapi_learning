from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated= "auto")

class Hash():
    def bcrypt(password:str):
        return pwd_cxt.hash(password)
    
    def verify(raw_password,hash_password):
        return pwd_cxt.verify(raw_password,hash_password)

