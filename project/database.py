import pymongo
import sqlalchemy
import time, sys, os

e = create_engine(
    "mongodb:///?Server=MyServer&Port=27017&Database=test&User=test&Password=Password"
)

db = c.flaskauth
col = db.ssoauth

NAME = "rocky"
PIN = "12345"
PASSWORD = "passw0rd"
PGP_PUBLIC_KEY = "loooxcdcxsqwlkjkjjjnjinihijhdjfksdjnfkalsjdfnksjdfnkasjdnfkjsdnfaksjdnksjaldnfkasjnfdkasjdfnkasljdfnksajdnfksaldjnfksaldjnfklsdnkksljfndkdsajfnklsdjfnlkasjdnfkladsnjfklsjdnfskdjnfaksdjfaksdnfklasjndflkasdfnaklsfn"
BIP_32_KEY = "bpi32keyeyey"
BIP_32_KEY_INDEX = "cool shit"
IS_VENDOR = "1"

datadict = {
    "name": NAME,
    "PIN": PIN,
    "password": PASSWORD,
    "pgp_public_key": PGP_PUBLIC_KEY,
    "bip32_key": BIP_32_KEY,
    "bip32_key_index": BIP_32_KEY_INDEX,
    "is_vendor": IS_VENDOR,
}


try:
    col.insert_one(datadict)
except Exception as e:
    print("An exception occurred ::", e)
