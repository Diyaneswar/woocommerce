import random
import string
import logging as logger

def email_and_passgen():
    logger.info("Generating random email and password")
    first=["ganesh","suresh","Mahesh","diyanesh"]
    last=["m","h","j","k"]
    domain=["gmail","hotmail","yahoo"]
    firstname=random.choice(first)
    lastname=random.choice(last)
    domain_add=random.choice(domain)

    email=firstname+"_"+lastname+"@"+domain_add+".com"
    password="".join(random.choices(string.ascii_lowercase,k=6))

    return {"email":email,"password":password}

def create_randomsring(random_strlen):
    return "".join(random.choices(string.ascii_lowercase,k=random_strlen))







