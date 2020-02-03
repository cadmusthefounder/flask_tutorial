
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer

class DietaryType:
    NORMAL = 'NORMAL'
    GLUTEN_FREE = 'GLUTEN_FREE'
    SOY_ALLERGY = 'SOY_ALLERGY'
    PEANUT_ALLERGY = 'PEANUT_ALLERGY'

Base = declarative_base()

class Lamb(Base):
    __tablename__ = 'lamb'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    weight = Column(Float,  nullable=False)
    dietary_type = Column(String, nullable=False, default=DietaryType.NORMAL)