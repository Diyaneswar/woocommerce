import os

class Credential():
    def __init__(self):
        pass

    @staticmethod
    def generate_cred():
        wc_key=os.getenv("wc_key")
        wc_sec=os.getenv("wc_sec")

        return {"wc_key":wc_key,"wc_sec":wc_sec}

    @staticmethod
    def generate_db():
        db_user=os.getenv("db_user")
        db_pass=os.getenv("db_pass")

        return {"db_user":db_user,"db_pass":db_pass}
