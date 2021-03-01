logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(
    filename="demo.log",
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)


class User(UserMixin, db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    PIN = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
