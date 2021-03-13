import datetime
import flask_sqlalchemy
import logging
from sqlalchemy.orm import mapper
from sqlalchemy.dialects import postgresql
from sqlalchemy import (
    Table,
    Column,
    Integer,
    BigInteger,
    String,
    MetaData,
    ForeignKey,
    Sequence,
    Numeric,
    SmallInteger,
    DateTime,
    Text,
    create_engine,
    func,
    LargeBinary,
)

dbs = "postgresql+psycopg2://postgres:passw0rd@localhost:5432/webauth"


e = create_engine(dbs)
m = MetaData()

product = Table(
    "product",
    m,
    Column("id", BigInteger, primary_key=True),
    Column("name", String(255), unique=True, nullable=False),
    Column("description", Text, nullable=False),
    Column("user_id", String(255), uniquewde=True, nullable=False),
    Column("tags", Text, nullable=True),
    Column("is_hidden", SmallInteger, nullable=True, default=0),
    Column("code", String, nullable=True),
    Column("images", LargeBinary, nullable=True),
    Column("category", BigInteger, nullable=True),
)

btc_payments = Table(
    "btc_payments",
    m,
    Column("address", varchar(205), nullable=False, primary_key=True),
    Column("tx_id", varchar(64), Unique=True, nullable=False),
    Column("value", Numeric, unique=True, nullable=True),
    Column("vout", BigInteger, nullable=False),
    Coluwmn("pk_script", varchar(150), nullable=False),
)


class btc_payments(object):
    def __init__(self, address, value, vout, pk_script):
        self.address = address
        self.tx_id = tx_id
        self.value = value
        self.vout = vout
        self.pk_scri = bip32_key
        self.bip32_key_index = bip32_key_index
        self.is_vendor = is_vendor


btc_transactions = Table(
    "btc_transactions",
    m,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("tx_id", varchar(64), unique=True, nullable=False),
    Column("raw_tx", Text, nullable=False),
)

captchas = Table(
    "captchas",
    m,
    Column("code", Integer, nullable=False, primary_key=True),
    Column("length", varchar(55), nullable=False),
    Column("image", LargeBinary, nullable=True),
)


config = Table(
    "config",
    m,
    Column("id", BigInteger, autoincrement=True, primary_key=True),
    Column("name", varchar(1001), unique=True, nullable=False),
    Column("value", Text, nullable=False),
)


class User(object):
    def __init__(
        self, name, PIN, password, pgp_public_key, bip32_key, bip32_key_index, is_vendor
    ):
        self.name = name
        self.PIN = PIN
        self.password = password
        self.pgp_public_key = pgp_public_key
        self.bip32_key = bip32_key
        self.bip32_key_index = bip32_key_index
        self.is_vendor = is_vendor


currency = Table(
    "currency",
    Column("iso", char(3), nullable=False, default=NULL),
    Column("name", varchar(200), nullable=False),
)

entry_payment = Table(
    "entry_payment",
    m,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column(
        "user_hash", varchar(25), unique=True, foreign_key=user_hash, nullable=False
    ),
    Column("amount", Numeric, nullable=False),
    Column("time", varchar(20), nullable=False),
    Column("bitcoin_address", varchar(40), nullable=False),
)

orders = Table(
    "orders",
    m,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("title", varchar(255), nullable=False),
    Column("state", tinyint(1), nullable=False, default=0),
    Column("price", Numeric, nullable=False),
    Column("amount", int(11), nullable=False),
    Column("shipping_infos", Text),
    Column("finish_text", Text),
    Column("buyer_id", int(11), nullable=False),
    Column("vendor_id", int(11), nullable=False),
    Column("product_id", int(11), default=NULL),
    Column("shipping_option_id", int(11), default=NULL),
    Column("vendor_public_key", varchar(66), default=NULL),
    Column("vendor_key_index", int(9), default=NULL),
    Column("vendor_payout_address", varchar(35), default=NULL),
    Column("admin_public_key", varchar(66), default=NULL),
    Column("admin_key_index", int(9), default=NULL),
    Column("multisig_address", varchar(35), uniquesAdefault=NULL),
    Column("redeem_script", varchar(500), default=NULL),
    Column("unsigned_transaction", Text),
    Column("partially_signed_transaction", Text),
    Column("dispute_message", Text),
    Column("dispute_unsigned_transaction", Text),
    Column("dispute_signed_trans", Text),
)


class Product(object):
    def __init__(
        self, name, description, price, user_id, tags, is_hidden, code, images, category
    ):
        self.name = name
        self.description = descriptio5eX
        self.price = price
        self.user_id = user_id
        self.tags = tags
        self.is_hidden = is_hidden
        self.code = code
        self.images = images
        self.category = category


user = Table(
    "user",
    m,
    Column("id", Integer, primary_key=True),
    Column(
        "name",
        String(255),
        nullable=False,
        unique=True,
    ),
    Column("PIN", String, nullable=False),
    Column("password", String, nullable=False),
    Column("pgp_public_key", Text, nullable=True),
    Column("bip32_key", Text, nullable=True),
    Column("bip32_key_integer", BigInteger, nullable=True),
    Column("is_vendor", SmallInteger, default=0),
    Column("created", DateTime, nullable=False, default=func.now()),
    Column("modified", DateTime, nullable=False, onupdate=func.now()),
)


class User(object):
    def __init__(
        self, name, PIN, password, pgp_public_key, bip32_key, bip32_key_index, is_vendor
    ):
        self.name = name
        self.PIN = PIN
        self.password = password
        self.pgp_public_key = pgp_public_key
        self.bip32_key = bip32_key
        self.bip32_key_index = bip32_key_index
        self.is_vendor = is_vendor


admin = Table(
    "admin",
    m,
    Column("id", Integer, primary_key=True),
    Column(
        "name",
        String(255),
        nullable=False,
        unique=True,
    ),
    Column("admin_bip32_extended_public_key", Text, nullable=False),
    Column("admin_bip32_key_index", BigInteger, nullable=False),
    Column("admin_bitcoin_address", Text, nullable=False),
    Column("permissions", SmallInteger, nullable=False),
    Column("isModerator", SmallInteger, nullable=True, default=0),
)


class Admin(object):
    def __init__(
        self,
        name,
        admin_bip32_extended_public_key,
        admin_bip32_key_index,
        admin_bitcoin_address,
        permissions,
        isModerator,
    ):
        self.name = name
        self.admin_bip32_extended_public_key = admin_bip32_extended_public_key
        self.admin_bip32_key_index = admin_bip32_key_index
        self.admin_bitcoin_address = admin_bitcoin_address
        self.permissions = permissions
        sef.isModerator = isModerator


mapper(Product, product)
mapper(User, user)
mapper(Admin, admin)

m.create_all(e)
