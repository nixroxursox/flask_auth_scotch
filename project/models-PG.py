import datetime
import flask_sqlalchemy
from decouple import config
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

# dbs = "postgresql+psycopg2://postgres:passw0rd@localhost:5432/webauth"

dbs = (
    "postgresql+psycopg2://postgres:"
    + config("DB_PASS")
    + "@localhost:5432/"
    + config("DB_NAME")
)

e = create_engine(dbs)
m = MetaData()

product = Table(
    "product",
    m,
    Column("id", BigInteger, primary_key=True),
    Column("name", String(255), unique=True, nullable=False),
    Column("description", Text, nullable=False),
    Column("user_id", String(255), unique=True, nullable=False),
    Column("tags", Text, nullable=True),
    Column("is_hidden", SmallInteger, nullable=True, default=0),
    Column("code", String, nullable=True),
    Column("images", LargeBinary, nullable=True),
    Column("category", BigInteger, nullable=True),
)


class product(object):
    def __init__(
        self, name, description, user_id, tags, is_hidden, code, images, category
    ):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.tags = tags
        self.is_hidden = is_hidden
        self.code = code
        self.images = images
        self.category = category


btc_payments = Table(
    "btc_payments",
    m,
    Column("address", String(205), nullable=False, primary_key=True),
    Column("tx_id", String(64), unique=True, nullable=False),
    Column("value", Numeric, unique=True, nullable=True),
    Column("vout", BigInteger, nullable=False),
    Column("pk_script", String(150), nullable=False),
)


class btc_payments(object):
    def __init__(self, address, value, vout, pk_script):
        self.address = address
        self.tx_id = tx_id
        self.value = value
        self.vout = vout
        self.pk_script = pk_script


btc_transactions = Table(
    "btc_transactions",
    m,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("tx_id", String(64), unique=True, nullable=False),
    Column("raw_tx", Text, nullable=False),
)


class btc_transactions(object):
    def __init__(self, tx_id, raw_tx):
        self.name = tx_id
        self.raw_tx = raw_tx


captchas = Table(
    "captchas",
    m,
    Column("code", Integer, nullable=False, primary_key=True),
    Column("length", String(55), nullable=False),
    Column("image", LargeBinary, nullable=True),
)


class captchas(object):
    def __init__(self, code, length, image):
        self.code = code
        self.length = length
        self.image = image


config = Table(
    "config",
    m,
    Column("id", BigInteger, autoincrement=True, primary_key=True),
    Column("name", String(1001), unique=True, nullable=False),
    Column("value", Text, nullable=False),
)


class config(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class user(object):
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
    m,
    Column("iso", String(3), nullable=False, default=""),
    Column("name", String(200), nullable=False),
)


class currency(object):
    def __init__(self, iso, name):
        self.ISO = iso
        self.name = name


entry_payment = Table(
    "entry_payment",
    m,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("user_hash", String(25), unique=True, nullable=False),
    Column("amount", Numeric, nullable=False),
    Column("time", String(20), nullable=False),
    Column("bitcoin_address", String(40), nullable=False),
)


class entry_payment(object):
    def __init__(self, user_hash, amount, time, bitcoin_address):
        self.user_hash = user_hash
        self.amount = amount
        self.time = time
        self.bitcoin_address = bitcoin_address


orders = Table(
    "orders",
    m,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("title", String(255), nullable=False),
    Column("state", Integer, nullable=False, default=0),
    Column("price", Numeric, nullable=False),
    Column("amount", BigInteger, nullable=False),
    Column("shipping_infos", Text),
    Column("finish_text", Text),
    Column("buyer_id", BigInteger, nullable=False),
    Column("vendor_id", BigInteger, nullable=False),
    Column("product_id", BigInteger, default=""),
    Column("shipping_option_id", BigInteger, default=""),
    Column("vendor_public_key", String(66), default=""),
    Column("vendor_key_index", BigInteger, default=""),
    Column("vendor_payout_address", String(35), default=""),
    Column("admin_public_key", String(66), default=""),
    Column("admin_key_index", BigInteger, default=""),
    Column("multisig_address", String(35), unique=True, default=""),
    Column("redeem_script", String(500), default=""),
    Column("unsigned_transaction", Text),
    Column("partially_signed_transaction", Text),
    Column("dispute_message", Text),
    Column("dispute_unsigned_transaction", Text),
    Column("dispute_signed_trans", Text),
)


class orders(object):
    def __init__(
        self,
        title,
        state,
        price,
        shipping_infos,
        finish_text,
        buyer_id,
        vendor_id,
        product_id,
        shipping_option_id,
        vendor_public_key,
        admin_key_index,
        multisig_address,
        redeem_script,
        unsigned_transaction,
        partially_signed_transaction,
        dispute_message,
        dispute_unsigned_transaction,
        dispute_signed_trans,
    ):
        self.title = title
        self.state = state
        self.price = price
        self.shipping_infos = shipping_infos
        self.finish_text = finish_text
        self.buyer_id = buyer_id
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.shipping_option_id = shipping_option_id
        self.vendor_public_key = vendor_public_key
        self.admin_key_index = admin_key_index
        self.multisig_address = multisig_address
        self.redeem_script = redeem_script
        self.unsigned_transaction = unsigned_transaction
        self.partially_signed_transaction = partially_signed_transaction
        self.dispute_message = dispute_message
        self.dispute_unsigned_transaction = dispute_unsigned_transaction
        self.dispute_signed_trans = dispute_signed_trans


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


mapper(product, product)
mapper(User, user)
mapper(Admin, admin)
mapper(orders, orders)
mapper(captchas, captchas)
mapper(currency, currency)
mapper(entry_payment, entry_payment)
mapper(config, config)

m.create_all(e)
