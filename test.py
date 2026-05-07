import bcrypt

salt = bcrypt.gensalt()
pwd = bcrypt.hashpw("password".encode("utf-8"), salt)
print(bcrypt.checkpw())