from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, Lamb, DietaryType

class Database:

    def __init__(self, filename):
        connection_url = 'sqlite:///{}'.format(filename)
        self._engine = create_engine(connection_url)
        self._Session = sessionmaker(bind=self._engine)
        self._session = None
        self._define_tables()

    def create_lamb(self, name, weight, dietary_type):
        lamb = Lamb(
            name=name, 
            weight=weight, 
            dietary_type=dietary_type
        )
        self._session.add(lamb)
        return lamb

    def get_lamb(self, id):
        lamb = self._session.query(Lamb).get(id)
        return lamb

    def update_lamb(self, id, name, weight, dietary_type):
        lamb = self.get_lamb(id)
        lamb.name = name
        lamb.weight = weight
        lamb.dietary_type = dietary_type
        self._session.add(lamb)
        return lamb

    def delete_lamb(self, id):
        lamb = self.get_lamb(id)
        self._session.delete(lamb)
        return lamb

    def commit(self):
        self._session.commit()

    def connect(self):
        self._session = self._Session()

    def disconnect(self):
        if self._session is not None:
            self._session.commit()
            self._session.close()
            self._session = None

    def __enter__(self):
        self.connect()

    def __exit__(self, exception_type, exception_value, traceback):
        self.disconnect()

    def _define_tables(self):
        Base.metadata.create_all(bind=self._engine)