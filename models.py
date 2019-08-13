# coding: utf-8
from sqlalchemy import Column, Date, String
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ListBrand(Base):
    __tablename__ = 'list_brand'

    BRAND_ID = Column(String(10, 'utf8mb4_general_ci'), primary_key=True)
    BRAND_NAME = Column(String(255, 'utf8mb4_general_ci'))


class ListManu(Base):
    __tablename__ = 'list_manu'

    MANU_ID = Column(String(10, 'utf8mb4_general_ci'), primary_key=True)
    MANU_NAME = Column(String(255, 'utf8mb4_general_ci'))


class ListMission(Base):
    __tablename__ = 'list_mission'

    MISSION_NAME = Column(String(255, 'utf8mb4_general_ci'), primary_key=True)
    MISSION_STATUS = Column(TINYINT(1))
    LASTDATE = Column(Date)


class ListModel(Base):
    __tablename__ = 'list_model'

    MODEL_ID = Column(String(10, 'utf8mb4_general_ci'), primary_key=True)
    MODEL_NAME = Column(String(255, 'utf8mb4_general_ci'))
    MODEL_PRICE = Column(String(255, 'utf8mb4_general_ci'))
    SEGMENT_ID = Column(String(10, 'utf8mb4_general_ci'))
    MANU_ID = Column(String(10, 'utf8mb4_general_ci'))
    BRAND_ID = Column(String(10, 'utf8mb4_general_ci'))
    MODEL_STATUS = Column(TINYINT(1))


class ListModelCalendar(Base):
    __tablename__ = 'list_model_calendar'

    MODEL_ID = Column(String(10, 'utf8mb4_general_ci'), primary_key=True, nullable=False)
    DATE = Column(Date, primary_key=True, nullable=False)
    NEWS_TITLE = Column(String(200, 'utf8mb4_general_ci'), primary_key=True, nullable=False)
    NEWS_HREF = Column(String(200, 'utf8mb4_general_ci'))


class ListModelNewenengyType(Base):
    __tablename__ = 'list_model_newenengy_type'

    MODEL_ID = Column(String(10, 'utf8mb4_general_ci'), primary_key=True)
    ENGINE_TYPE = Column(String(100, 'utf8mb4_general_ci'))


class ListModelNewenergy(Base):
    __tablename__ = 'list_model_newenergy'

    MODEL_ID = Column(String(10, 'utf8mb4_general_ci'), primary_key=True)


class ListSegment(Base):
    __tablename__ = 'list_segment'

    SEGMENT_ID = Column(String(10, 'utf8mb4_general_ci'), primary_key=True)
    SEGMENT_NAME = Column(String(255, 'utf8mb4_general_ci'))
