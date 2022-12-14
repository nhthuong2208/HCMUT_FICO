from flask_sqlalchemy import SQLAlchemy
from .utils import *

db = SQLAlchemy()

COL_NAMES = create_column()


class Deserialize:
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(db.Model, Deserialize):
    __tablename__ = 'user'

    ID = db.Column(db.Integer, primary_key=True)
    SS_number = db.Column(db.String(12), unique=True, nullable=False)
    birthday = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(10), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    day_ID_publish = db.Column(db.String(10), nullable=False)
    day_employed = db.Column(db.String(10), nullable=True)
    last_modified = db.Column(db.String(10), nullable=True)

    def __init__(self, data):
        self.ID = data.get('ID')
        self.SS_number = data.get('SS_number')
        self.birthday = data.get('birthday')
        self.address = data.get('address')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.phone = data.get('phone')
        self.gender = data.get('gender')
        self.email = data.get('email')
        self.day_ID_publish = data.get('day_ID_publish')
        self.day_employed = data.get('day_employed')
        self.last_modified = data.get('last_modified')


class BankData(db.Model, Deserialize):
    __tablename__ = 'bankdata'

    ID = db.Column(db.Integer, primary_key=True)
    CODE_GENDER = db.Column(db.String(128), nullable=True)
    FLAG_OWN_CAR = db.Column(db.String(128), nullable=True)
    FLAG_OWN_REALTY = db.Column(db.String(128), nullable=True)
    CNT_CHILDREN = db.Column(db.String(128), nullable=True)
    AMT_INCOME_TOTAL = db.Column(db.String(128), nullable=True)
    AMT_CREDIT = db.Column(db.String(128), nullable=True)
    AMT_ANNUITY = db.Column(db.String(128), nullable=True)
    AMT_GOODS_PRICE = db.Column(db.String(128), nullable=True)
    REGION_POPULATION_RELATIVE = db.Column(db.String(128), nullable=True)
    DAYS_BIRTH = db.Column(db.String(128), nullable=True)
    DAYS_EMPLOYED = db.Column(db.String(128), nullable=True)
    DAYS_REGISTRATION = db.Column(db.String(128), nullable=True)
    DAYS_ID_PUBLISH = db.Column(db.String(128), nullable=True)
    OWN_CAR_AGE = db.Column(db.String(128), nullable=True)
    FLAG_MOBIL = db.Column(db.String(128), nullable=True)
    FLAG_EMP_PHONE = db.Column(db.String(128), nullable=True)
    FLAG_WORK_PHONE = db.Column(db.String(128), nullable=True)
    FLAG_CONT_MOBILE = db.Column(db.String(128), nullable=True)
    FLAG_PHONE = db.Column(db.String(128), nullable=True)
    FLAG_EMAIL = db.Column(db.String(128), nullable=True)
    CNT_FAM_MEMBERS = db.Column(db.String(128), nullable=True)
    REGION_RATING_CLIENT = db.Column(db.String(128), nullable=True)
    REGION_RATING_CLIENT_W_CITY = db.Column(db.String(128), nullable=True)
    HOUR_APPR_PROCESS_START = db.Column(db.String(128), nullable=True)
    REG_REGION_NOT_LIVE_REGION = db.Column(db.String(128), nullable=True)
    REG_REGION_NOT_WORK_REGION = db.Column(db.String(128), nullable=True)
    LIVE_REGION_NOT_WORK_REGION = db.Column(db.String(128), nullable=True)
    REG_CITY_NOT_LIVE_CITY = db.Column(db.String(128), nullable=True)
    REG_CITY_NOT_WORK_CITY = db.Column(db.String(128), nullable=True)
    LIVE_CITY_NOT_WORK_CITY = db.Column(db.String(128), nullable=True)
    EXT_SOURCE_1 = db.Column(db.String(128), nullable=True)
    EXT_SOURCE_2 = db.Column(db.String(128), nullable=True)
    EXT_SOURCE_3 = db.Column(db.String(128), nullable=True)
    APARTMENTS_AVG = db.Column(db.String(128), nullable=True)
    BASEMENTAREA_AVG = db.Column(db.String(128), nullable=True)
    YEARS_BEGINEXPLUATATION_AVG = db.Column(db.String(128), nullable=True)
    YEARS_BUILD_AVG = db.Column(db.String(128), nullable=True)
    COMMONAREA_AVG = db.Column(db.String(128), nullable=True)
    ELEVATORS_AVG = db.Column(db.String(128), nullable=True)
    ENTRANCES_AVG = db.Column(db.String(128), nullable=True)
    FLOORSMAX_AVG = db.Column(db.String(128), nullable=True)
    FLOORSMIN_AVG = db.Column(db.String(128), nullable=True)
    LANDAREA_AVG = db.Column(db.String(128), nullable=True)
    LIVINGAPARTMENTS_AVG = db.Column(db.String(128), nullable=True)
    LIVINGAREA_AVG = db.Column(db.String(128), nullable=True)
    NONLIVINGAPARTMENTS_AVG = db.Column(db.String(128), nullable=True)
    NONLIVINGAREA_AVG = db.Column(db.String(128), nullable=True)
    APARTMENTS_MODE = db.Column(db.String(128), nullable=True)
    BASEMENTAREA_MODE = db.Column(db.String(128), nullable=True)
    YEARS_BEGINEXPLUATATION_MODE = db.Column(db.String(128), nullable=True)
    YEARS_BUILD_MODE = db.Column(db.String(128), nullable=True)
    COMMONAREA_MODE = db.Column(db.String(128), nullable=True)
    ELEVATORS_MODE = db.Column(db.String(128), nullable=True)
    ENTRANCES_MODE = db.Column(db.String(128), nullable=True)
    FLOORSMAX_MODE = db.Column(db.String(128), nullable=True)
    FLOORSMIN_MODE = db.Column(db.String(128), nullable=True)
    LANDAREA_MODE = db.Column(db.String(128), nullable=True)
    LIVINGAPARTMENTS_MODE = db.Column(db.String(128), nullable=True)
    LIVINGAREA_MODE = db.Column(db.String(128), nullable=True)
    NONLIVINGAPARTMENTS_MODE = db.Column(db.String(128), nullable=True)
    NONLIVINGAREA_MODE = db.Column(db.String(128), nullable=True)
    APARTMENTS_MEDI = db.Column(db.String(128), nullable=True)
    BASEMENTAREA_MEDI = db.Column(db.String(128), nullable=True)
    YEARS_BEGINEXPLUATATION_MEDI = db.Column(db.String(128), nullable=True)
    YEARS_BUILD_MEDI = db.Column(db.String(128), nullable=True)
    COMMONAREA_MEDI = db.Column(db.String(128), nullable=True)
    ELEVATORS_MEDI = db.Column(db.String(128), nullable=True)
    ENTRANCES_MEDI = db.Column(db.String(128), nullable=True)
    FLOORSMAX_MEDI = db.Column(db.String(128), nullable=True)
    FLOORSMIN_MEDI = db.Column(db.String(128), nullable=True)
    LANDAREA_MEDI = db.Column(db.String(128), nullable=True)
    LIVINGAPARTMENTS_MEDI = db.Column(db.String(128), nullable=True)
    LIVINGAREA_MEDI = db.Column(db.String(128), nullable=True)
    NONLIVINGAPARTMENTS_MEDI = db.Column(db.String(128), nullable=True)
    NONLIVINGAREA_MEDI = db.Column(db.String(128), nullable=True)
    TOTALAREA_MODE = db.Column(db.String(128), nullable=True)
    OBS_30_CNT_SOCIAL_CIRCLE = db.Column(db.String(128), nullable=True)
    DEF_30_CNT_SOCIAL_CIRCLE = db.Column(db.String(128), nullable=True)
    OBS_60_CNT_SOCIAL_CIRCLE = db.Column(db.String(128), nullable=True)
    DEF_60_CNT_SOCIAL_CIRCLE = db.Column(db.String(128), nullable=True)
    DAYS_LAST_PHONE_CHANGE = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_2 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_3 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_4 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_5 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_6 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_7 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_8 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_9 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_10 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_11 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_12 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_13 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_14 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_15 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_16 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_17 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_18 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_19 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_20 = db.Column(db.String(128), nullable=True)
    FLAG_DOCUMENT_21 = db.Column(db.String(128), nullable=True)
    AMT_REQ_CREDIT_BUREAU_HOUR = db.Column(db.String(128), nullable=True)
    AMT_REQ_CREDIT_BUREAU_DAY = db.Column(db.String(128), nullable=True)
    AMT_REQ_CREDIT_BUREAU_WEEK = db.Column(db.String(128), nullable=True)
    AMT_REQ_CREDIT_BUREAU_MON = db.Column(db.String(128), nullable=True)
    AMT_REQ_CREDIT_BUREAU_QRT = db.Column(db.String(128), nullable=True)
    AMT_REQ_CREDIT_BUREAU_YEAR = db.Column(db.String(128), nullable=True)
    APP_CREDIT_TO_ANNUITY_RATIO = db.Column(db.String(128), nullable=True)
    APP_CREDIT_TO_GOODS_RATIO = db.Column(db.String(128), nullable=True)
    APP_INC_PER_CHLD = db.Column(db.String(128), nullable=True)
    APP_EMPLOY_TO_BIRTH_RATIO = db.Column(db.String(128), nullable=True)
    APP_EMPLOY_TO_BIRTH_18_RATIO = db.Column(db.String(128), nullable=True)
    APP_BIRTH_TO_EMPLOY_RATIO = db.Column(db.String(128), nullable=True)
    APP_INCOME_TO_ANNUITY_RATIO = db.Column(db.String(128), nullable=True)
    APP_ANNUITY_TO_INCOME_RATIO = db.Column(db.String(128), nullable=True)
    APP_EXT_SOURCES_MEAN = db.Column(db.String(128), nullable=True)
    APP_EXT_SOURCES_MAX = db.Column(db.String(128), nullable=True)
    APP_EXT_SOURCES_MIN = db.Column(db.String(128), nullable=True)
    APP_CAR_TO_BIRTH_RATIO = db.Column(db.String(128), nullable=True)
    APP_CAR_TO_EMPLOY_RATIO = db.Column(db.String(128), nullable=True)
    APP_PHONE_TO_BIRTH_RATIO = db.Column(db.String(128), nullable=True)
    APP_PHONE_TO_EMPLOYED_RATIO = db.Column(db.String(128), nullable=True)
    APP_CREDIT_TO_INCOME_RATIO = db.Column(db.String(128), nullable=True)
    APP_PAYMENT_RATE = db.Column(db.String(128), nullable=True)
    APP_INCOME_CREDIT_PERC = db.Column(db.String(128), nullable=True)
    APP_INCOME_PER_PERSON = db.Column(db.String(128), nullable=True)
    NAME_CONTRACT_TYPE_Cash_loans = db.Column(db.String(128), nullable=True)
    NAME_CONTRACT_TYPE_Revolving_loans = db.Column(
        db.String(128), nullable=True)
    NAME_TYPE_SUITE_Children = db.Column(db.String(128), nullable=True)
    NAME_TYPE_SUITE_Family = db.Column(db.String(128), nullable=True)
    NAME_TYPE_SUITE_Group_of_people = db.Column(db.String(128), nullable=True)
    NAME_TYPE_SUITE_Other_A = db.Column(db.String(128), nullable=True)
    NAME_TYPE_SUITE_Other_B = db.Column(db.String(128), nullable=True)
    NAME_TYPE_SUITE_Spouse_partner = db.Column(db.String(128), nullable=True)
    NAME_TYPE_SUITE_Unaccompanied = db.Column(db.String(128), nullable=True)
    NAME_INCOME_TYPE_Businessman = db.Column(db.String(128), nullable=True)
    NAME_INCOME_TYPE_Commercial_associate = db.Column(
        db.String(128), nullable=True)
    NAME_INCOME_TYPE_Maternity_leave = db.Column(db.String(128), nullable=True)
    NAME_INCOME_TYPE_Pensioner = db.Column(db.String(128), nullable=True)
    NAME_INCOME_TYPE_State_servant = db.Column(db.String(128), nullable=True)
    NAME_INCOME_TYPE_Student = db.Column(db.String(128), nullable=True)
    NAME_INCOME_TYPE_Unemployed = db.Column(db.String(128), nullable=True)
    NAME_INCOME_TYPE_Working = db.Column(db.String(128), nullable=True)
    NAME_EDUCATION_TYPE_Academic_degree = db.Column(
        db.String(128), nullable=True)
    NAME_EDUCATION_TYPE_Higher_education = db.Column(
        db.String(128), nullable=True)
    NAME_EDUCATION_TYPE_Incomplete_higher = db.Column(
        db.String(128), nullable=True)
    NAME_EDUCATION_TYPE_Lower_secondary = db.Column(
        db.String(128), nullable=True)
    NAME_EDUCATION_TYPE_Secondary_secondary_special = db.Column(
        db.String(128), nullable=True)
    NAME_FAMILY_STATUS_Civil_marriage = db.Column(
        db.String(128), nullable=True)
    NAME_FAMILY_STATUS_Married = db.Column(db.String(128), nullable=True)
    NAME_FAMILY_STATUS_Separated = db.Column(db.String(128), nullable=True)
    NAME_FAMILY_STATUS_Single_not_married = db.Column(
        db.String(128), nullable=True)
    NAME_FAMILY_STATUS_Unknown = db.Column(db.String(128), nullable=True)
    NAME_FAMILY_STATUS_Widow = db.Column(db.String(128), nullable=True)
    NAME_HOUSING_TYPE_Co_op_apartment = db.Column(
        db.String(128), nullable=True)
    NAME_HOUSING_TYPE_House_apartment = db.Column(
        db.String(128), nullable=True)
    NAME_HOUSING_TYPE_Municipal_apartment = db.Column(
        db.String(128), nullable=True)
    NAME_HOUSING_TYPE_Office_apartment = db.Column(
        db.String(128), nullable=True)
    NAME_HOUSING_TYPE_Rented_apartment = db.Column(
        db.String(128), nullable=True)
    NAME_HOUSING_TYPE_With_parents = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Accountants = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Cleaning_staff = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Cooking_staff = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Core_staff = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Drivers = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_HR_staff = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_High_skill_tech_staff = db.Column(
        db.String(128), nullable=True)
    OCCUPATION_TYPE_IT_staff = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Laborers = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Low_skill_Laborers = db.Column(
        db.String(128), nullable=True)
    OCCUPATION_TYPE_Managers = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Medicine_staff = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Private_service_staff = db.Column(
        db.String(128), nullable=True)
    OCCUPATION_TYPE_Realty_agents = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Sales_staff = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Secretaries = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Security_staff = db.Column(db.String(128), nullable=True)
    OCCUPATION_TYPE_Waiters_barmen_staff = db.Column(
        db.String(128), nullable=True)
    WEEKDAY_APPR_PROCESS_START_FRIDAY = db.Column(
        db.String(128), nullable=True)
    WEEKDAY_APPR_PROCESS_START_MONDAY = db.Column(
        db.String(128), nullable=True)
    WEEKDAY_APPR_PROCESS_START_SATURDAY = db.Column(
        db.String(128), nullable=True)
    WEEKDAY_APPR_PROCESS_START_SUNDAY = db.Column(
        db.String(128), nullable=True)
    WEEKDAY_APPR_PROCESS_START_THURSDAY = db.Column(
        db.String(128), nullable=True)
    WEEKDAY_APPR_PROCESS_START_TUESDAY = db.Column(
        db.String(128), nullable=True)
    WEEKDAY_APPR_PROCESS_START_WEDNESDAY = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Advertising = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Agriculture = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Bank = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Business_Entity_Type_1 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Business_Entity_Type_2 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Business_Entity_Type_3 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Cleaning = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Construction = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Culture = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Electricity = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Emergency = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Government = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Hotel = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Housing = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_1 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_10 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_11 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_12 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_13 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_2 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_3 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_4 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_5 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_6 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_7 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_8 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Industry_type_9 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Insurance = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Kindergarten = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Legal_Services = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Medicine = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Military = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Mobile = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Other = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Police = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Postal = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Realtor = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Religion = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Restaurant = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_School = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Security = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Security_Ministries = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Self_employed = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Services = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Telecom = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Trade_type_1 = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Trade_type_2 = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Trade_type_3 = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Trade_type_4 = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Trade_type_5 = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Trade_type_6 = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Trade_type_7 = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_Transport_type_1 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Transport_type_2 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Transport_type_3 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_Transport_type_4 = db.Column(
        db.String(128), nullable=True)
    ORGANIZATION_TYPE_University = db.Column(db.String(128), nullable=True)
    ORGANIZATION_TYPE_XNA = db.Column(db.String(128), nullable=True)
    FONDKAPREMONT_MODE_not_specified = db.Column(db.String(128), nullable=True)
    FONDKAPREMONT_MODE_org_spec_account = db.Column(
        db.String(128), nullable=True)
    FONDKAPREMONT_MODE_reg_oper_account = db.Column(
        db.String(128), nullable=True)
    FONDKAPREMONT_MODE_reg_oper_spec_account = db.Column(
        db.String(128), nullable=True)
    HOUSETYPE_MODE_block_of_flats = db.Column(db.String(128), nullable=True)
    HOUSETYPE_MODE_specific_housing = db.Column(db.String(128), nullable=True)
    HOUSETYPE_MODE_terraced_house = db.Column(db.String(128), nullable=True)
    WALLSMATERIAL_MODE_Block = db.Column(db.String(128), nullable=True)
    WALLSMATERIAL_MODE_Mixed = db.Column(db.String(128), nullable=True)
    WALLSMATERIAL_MODE_Monolithic = db.Column(db.String(128), nullable=True)
    WALLSMATERIAL_MODE_Others = db.Column(db.String(128), nullable=True)
    WALLSMATERIAL_MODE_Panel = db.Column(db.String(128), nullable=True)
    WALLSMATERIAL_MODE_Stone_brick = db.Column(db.String(128), nullable=True)
    WALLSMATERIAL_MODE_Wooden = db.Column(db.String(128), nullable=True)
    EMERGENCYSTATE_MODE_No = db.Column(db.String(128), nullable=True)
    EMERGENCYSTATE_MODE_Yes = db.Column(db.String(128), nullable=True)
    BURO_DAYS_CREDIT_MEAN = db.Column(db.String(128), nullable=True)
    BURO_DAYS_CREDIT_VAR = db.Column(db.String(128), nullable=True)
    BURO_DAYS_CREDIT_ENDDATE_MEAN = db.Column(db.String(128), nullable=True)
    BURO_DAYS_CREDIT_UPDATE_MEAN = db.Column(db.String(128), nullable=True)
    BURO_CREDIT_DAY_OVERDUE_MEAN = db.Column(db.String(128), nullable=True)
    BURO_AMT_CREDIT_MAX_OVERDUE_MEAN = db.Column(db.String(128), nullable=True)
    BURO_AMT_CREDIT_SUM_MEAN = db.Column(db.String(128), nullable=True)
    BURO_AMT_CREDIT_SUM_SUM = db.Column(db.String(128), nullable=True)
    BURO_AMT_CREDIT_SUM_DEBT_MEAN = db.Column(db.String(128), nullable=True)
    BURO_AMT_CREDIT_SUM_DEBT_SUM = db.Column(db.String(128), nullable=True)
    BURO_AMT_CREDIT_SUM_OVERDUE_MEAN = db.Column(db.String(128), nullable=True)
    BURO_AMT_CREDIT_SUM_LIMIT_MEAN = db.Column(db.String(128), nullable=True)
    BURO_AMT_CREDIT_SUM_LIMIT_SUM = db.Column(db.String(128), nullable=True)
    BURO_AMT_ANNUITY_MAX = db.Column(db.String(128), nullable=True)
    BURO_AMT_ANNUITY_MEAN = db.Column(db.String(128), nullable=True)
    BURO_CNT_CREDIT_PROLONG_SUM = db.Column(db.String(128), nullable=True)
    BURO_MONTHS_BALANCE_MIN_MIN = db.Column(db.String(128), nullable=True)
    BURO_MONTHS_BALANCE_MAX_MAX = db.Column(db.String(128), nullable=True)
    BURO_MONTHS_BALANCE_SIZE_MEAN = db.Column(db.String(128), nullable=True)
    BURO_MONTHS_BALANCE_SIZE_SUM = db.Column(db.String(128), nullable=True)
    BURO_CREDIT_ACTIVE_Active_MEAN = db.Column(db.String(128), nullable=True)
    BURO_CREDIT_ACTIVE_Bad_debt_MEAN = db.Column(db.String(128), nullable=True)
    BURO_CREDIT_ACTIVE_Closed_MEAN = db.Column(db.String(128), nullable=True)
    BURO_CREDIT_ACTIVE_Sold_MEAN = db.Column(db.String(128), nullable=True)
    BURO_CREDIT_ACTIVE_nan_MEAN = db.Column(db.String(128), nullable=True)
    BURO_CREDIT_CURRENCY_currency_1_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_CURRENCY_currency_2_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_CURRENCY_currency_3_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_CURRENCY_currency_4_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_CURRENCY_nan_MEAN = db.Column(db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Another_type_of_loan_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Car_loan_MEAN = db.Column(db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Cash_loan__non_earmarked__MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Consumer_credit_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Credit_card_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Interbank_credit_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Loan_for_business_development_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Loan_for_purchase_of_shares__margin_lending__MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Loan_for_the_purchase_of_equipment_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Loan_for_working_capital_replenishment_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Microloan_MEAN = db.Column(db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Mobile_operator_loan_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Mortgage_MEAN = db.Column(db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Real_estate_loan_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_Unknown_type_of_loan_MEAN = db.Column(
        db.String(128), nullable=True)
    BURO_CREDIT_TYPE_nan_MEAN = db.Column(db.String(128), nullable=True)
    BURO_STATUS_0_MEAN_MEAN = db.Column(db.String(128), nullable=True)
    BURO_STATUS_1_MEAN_MEAN = db.Column(db.String(128), nullable=True)
    BURO_STATUS_2_MEAN_MEAN = db.Column(db.String(128), nullable=True)
    BURO_STATUS_3_MEAN_MEAN = db.Column(db.String(128), nullable=True)
    BURO_STATUS_4_MEAN_MEAN = db.Column(db.String(128), nullable=True)
    BURO_STATUS_5_MEAN_MEAN = db.Column(db.String(128), nullable=True)
    BURO_STATUS_C_MEAN_MEAN = db.Column(db.String(128), nullable=True)
    BURO_STATUS_X_MEAN_MEAN = db.Column(db.String(128), nullable=True)
    BURO_STATUS_nan_MEAN_MEAN = db.Column(db.String(128), nullable=True)
    ACTIVE_DAYS_CREDIT_MEAN = db.Column(db.String(128), nullable=True)
    ACTIVE_DAYS_CREDIT_VAR = db.Column(db.String(128), nullable=True)
    ACTIVE_DAYS_CREDIT_ENDDATE_MEAN = db.Column(db.String(128), nullable=True)
    ACTIVE_DAYS_CREDIT_UPDATE_MEAN = db.Column(db.String(128), nullable=True)
    ACTIVE_CREDIT_DAY_OVERDUE_MEAN = db.Column(db.String(128), nullable=True)
    ACTIVE_AMT_CREDIT_MAX_OVERDUE_MEAN = db.Column(
        db.String(128), nullable=True)
    ACTIVE_AMT_CREDIT_SUM_MEAN = db.Column(db.String(128), nullable=True)
    ACTIVE_AMT_CREDIT_SUM_SUM = db.Column(db.String(128), nullable=True)
    ACTIVE_AMT_CREDIT_SUM_DEBT_MEAN = db.Column(db.String(128), nullable=True)
    ACTIVE_AMT_CREDIT_SUM_DEBT_SUM = db.Column(db.String(128), nullable=True)
    ACTIVE_AMT_CREDIT_SUM_OVERDUE_MEAN = db.Column(
        db.String(128), nullable=True)
    ACTIVE_AMT_CREDIT_SUM_LIMIT_MEAN = db.Column(db.String(128), nullable=True)
    ACTIVE_AMT_CREDIT_SUM_LIMIT_SUM = db.Column(db.String(128), nullable=True)
    ACTIVE_AMT_ANNUITY_MAX = db.Column(db.String(128), nullable=True)
    ACTIVE_AMT_ANNUITY_MEAN = db.Column(db.String(128), nullable=True)
    ACTIVE_CNT_CREDIT_PROLONG_SUM = db.Column(db.String(128), nullable=True)
    ACTIVE_MONTHS_BALANCE_MIN_MIN = db.Column(db.String(128), nullable=True)
    ACTIVE_MONTHS_BALANCE_MAX_MAX = db.Column(db.String(128), nullable=True)
    ACTIVE_MONTHS_BALANCE_SIZE_MEAN = db.Column(db.String(128), nullable=True)
    ACTIVE_MONTHS_BALANCE_SIZE_SUM = db.Column(db.String(128), nullable=True)
    CLOSED_DAYS_CREDIT_MEAN = db.Column(db.String(128), nullable=True)
    CLOSED_DAYS_CREDIT_VAR = db.Column(db.String(128), nullable=True)
    CLOSED_DAYS_CREDIT_ENDDATE_MEAN = db.Column(db.String(128), nullable=True)
    CLOSED_DAYS_CREDIT_UPDATE_MEAN = db.Column(db.String(128), nullable=True)
    CLOSED_CREDIT_DAY_OVERDUE_MEAN = db.Column(db.String(128), nullable=True)
    CLOSED_AMT_CREDIT_MAX_OVERDUE_MEAN = db.Column(
        db.String(128), nullable=True)
    CLOSED_AMT_CREDIT_SUM_MEAN = db.Column(db.String(128), nullable=True)
    CLOSED_AMT_CREDIT_SUM_SUM = db.Column(db.String(128), nullable=True)
    CLOSED_AMT_CREDIT_SUM_DEBT_MEAN = db.Column(db.String(128), nullable=True)
    CLOSED_AMT_CREDIT_SUM_DEBT_SUM = db.Column(db.String(128), nullable=True)
    CLOSED_AMT_CREDIT_SUM_OVERDUE_MEAN = db.Column(
        db.String(128), nullable=True)
    CLOSED_AMT_CREDIT_SUM_LIMIT_MEAN = db.Column(db.String(128), nullable=True)
    CLOSED_AMT_CREDIT_SUM_LIMIT_SUM = db.Column(db.String(128), nullable=True)
    CLOSED_AMT_ANNUITY_MAX = db.Column(db.String(128), nullable=True)
    CLOSED_AMT_ANNUITY_MEAN = db.Column(db.String(128), nullable=True)
    CLOSED_CNT_CREDIT_PROLONG_SUM = db.Column(db.String(128), nullable=True)
    CLOSED_MONTHS_BALANCE_MIN_MIN = db.Column(db.String(128), nullable=True)
    CLOSED_MONTHS_BALANCE_MAX_MAX = db.Column(db.String(128), nullable=True)
    CLOSED_MONTHS_BALANCE_SIZE_MEAN = db.Column(db.String(128), nullable=True)
    CLOSED_MONTHS_BALANCE_SIZE_SUM = db.Column(db.String(128), nullable=True)

    def __init__(self, data):
        self.ID = data.get('ID')
        self.CODE_GENDER = data.get('CODE_GENDER')
        self.FLAG_OWN_CAR = data.get('FLAG_OWN_CAR')
        self.FLAG_OWN_REALTY = data.get('FLAG_OWN_REALTY')
        self.CNT_CHILDREN = data.get('CNT_CHILDREN')
        self.AMT_INCOME_TOTAL = data.get('AMT_INCOME_TOTAL')
        self.AMT_CREDIT = data.get('AMT_CREDIT')
        self.AMT_ANNUITY = data.get('AMT_ANNUITY')
        self.AMT_GOODS_PRICE = data.get('AMT_GOODS_PRICE')
        self.REGION_POPULATION_RELATIVE = data.get(
            'REGION_POPULATION_RELATIVE')
        self.DAYS_BIRTH = data.get('DAYS_BIRTH')
        self.DAYS_EMPLOYED = data.get('DAYS_EMPLOYED')
        self.DAYS_REGISTRATION = data.get('DAYS_REGISTRATION')
        self.DAYS_ID_PUBLISH = data.get('DAYS_ID_PUBLISH')
        self.OWN_CAR_AGE = data.get('OWN_CAR_AGE')
        self.FLAG_MOBIL = data.get('FLAG_MOBIL')
        self.FLAG_EMP_PHONE = data.get('FLAG_EMP_PHONE')
        self.FLAG_WORK_PHONE = data.get('FLAG_WORK_PHONE')
        self.FLAG_CONT_MOBILE = data.get('FLAG_CONT_MOBILE')
        self.FLAG_PHONE = data.get('FLAG_PHONE')
        self.FLAG_EMAIL = data.get('FLAG_EMAIL')
        self.CNT_FAM_MEMBERS = data.get('CNT_FAM_MEMBERS')
        self.REGION_RATING_CLIENT = data.get('REGION_RATING_CLIENT')
        self.REGION_RATING_CLIENT_W_CITY = data.get(
            'REGION_RATING_CLIENT_W_CITY')
        self.HOUR_APPR_PROCESS_START = data.get('HOUR_APPR_PROCESS_START')
        self.REG_REGION_NOT_LIVE_REGION = data.get(
            'REG_REGION_NOT_LIVE_REGION')
        self.REG_REGION_NOT_WORK_REGION = data.get(
            'REG_REGION_NOT_WORK_REGION')
        self.LIVE_REGION_NOT_WORK_REGION = data.get(
            'LIVE_REGION_NOT_WORK_REGION')
        self.REG_CITY_NOT_LIVE_CITY = data.get('REG_CITY_NOT_LIVE_CITY')
        self.REG_CITY_NOT_WORK_CITY = data.get('REG_CITY_NOT_WORK_CITY')
        self.LIVE_CITY_NOT_WORK_CITY = data.get('LIVE_CITY_NOT_WORK_CITY')
        self.EXT_SOURCE_1 = data.get('EXT_SOURCE_1')
        self.EXT_SOURCE_2 = data.get('EXT_SOURCE_2')
        self.EXT_SOURCE_3 = data.get('EXT_SOURCE_3')
        self.APARTMENTS_AVG = data.get('APARTMENTS_AVG')
        self.BASEMENTAREA_AVG = data.get('BASEMENTAREA_AVG')
        self.YEARS_BEGINEXPLUATATION_AVG = data.get(
            'YEARS_BEGINEXPLUATATION_AVG')
        self.YEARS_BUILD_AVG = data.get('YEARS_BUILD_AVG')
        self.COMMONAREA_AVG = data.get('COMMONAREA_AVG')
        self.ELEVATORS_AVG = data.get('ELEVATORS_AVG')
        self.ENTRANCES_AVG = data.get('ENTRANCES_AVG')
        self.FLOORSMAX_AVG = data.get('FLOORSMAX_AVG')
        self.FLOORSMIN_AVG = data.get('FLOORSMIN_AVG')
        self.LANDAREA_AVG = data.get('LANDAREA_AVG')
        self.LIVINGAPARTMENTS_AVG = data.get('LIVINGAPARTMENTS_AVG')
        self.LIVINGAREA_AVG = data.get('LIVINGAREA_AVG')
        self.NONLIVINGAPARTMENTS_AVG = data.get('NONLIVINGAPARTMENTS_AVG')
        self.NONLIVINGAREA_AVG = data.get('NONLIVINGAREA_AVG')
        self.APARTMENTS_MODE = data.get('APARTMENTS_MODE')
        self.BASEMENTAREA_MODE = data.get('BASEMENTAREA_MODE')
        self.YEARS_BEGINEXPLUATATION_MODE = data.get(
            'YEARS_BEGINEXPLUATATION_MODE')
        self.YEARS_BUILD_MODE = data.get('YEARS_BUILD_MODE')
        self.COMMONAREA_MODE = data.get('COMMONAREA_MODE')
        self.ELEVATORS_MODE = data.get('ELEVATORS_MODE')
        self.ENTRANCES_MODE = data.get('ENTRANCES_MODE')
        self.FLOORSMAX_MODE = data.get('FLOORSMAX_MODE')
        self.FLOORSMIN_MODE = data.get('FLOORSMIN_MODE')
        self.LANDAREA_MODE = data.get('LANDAREA_MODE')
        self.LIVINGAPARTMENTS_MODE = data.get('LIVINGAPARTMENTS_MODE')
        self.LIVINGAREA_MODE = data.get('LIVINGAREA_MODE')
        self.NONLIVINGAPARTMENTS_MODE = data.get('NONLIVINGAPARTMENTS_MODE')
        self.NONLIVINGAREA_MODE = data.get('NONLIVINGAREA_MODE')
        self.APARTMENTS_MEDI = data.get('APARTMENTS_MEDI')
        self.BASEMENTAREA_MEDI = data.get('BASEMENTAREA_MEDI')
        self.YEARS_BEGINEXPLUATATION_MEDI = data.get(
            'YEARS_BEGINEXPLUATATION_MEDI')
        self.YEARS_BUILD_MEDI = data.get('YEARS_BUILD_MEDI')
        self.COMMONAREA_MEDI = data.get('COMMONAREA_MEDI')
        self.ELEVATORS_MEDI = data.get('ELEVATORS_MEDI')
        self.ENTRANCES_MEDI = data.get('ENTRANCES_MEDI')
        self.FLOORSMAX_MEDI = data.get('FLOORSMAX_MEDI')
        self.FLOORSMIN_MEDI = data.get('FLOORSMIN_MEDI')
        self.LANDAREA_MEDI = data.get('LANDAREA_MEDI')
        self.LIVINGAPARTMENTS_MEDI = data.get('LIVINGAPARTMENTS_MEDI')
        self.LIVINGAREA_MEDI = data.get('LIVINGAREA_MEDI')
        self.NONLIVINGAPARTMENTS_MEDI = data.get('NONLIVINGAPARTMENTS_MEDI')
        self.NONLIVINGAREA_MEDI = data.get('NONLIVINGAREA_MEDI')
        self.TOTALAREA_MODE = data.get('TOTALAREA_MODE')
        self.OBS_30_CNT_SOCIAL_CIRCLE = data.get('OBS_30_CNT_SOCIAL_CIRCLE')
        self.DEF_30_CNT_SOCIAL_CIRCLE = data.get('DEF_30_CNT_SOCIAL_CIRCLE')
        self.OBS_60_CNT_SOCIAL_CIRCLE = data.get('OBS_60_CNT_SOCIAL_CIRCLE')
        self.DEF_60_CNT_SOCIAL_CIRCLE = data.get('DEF_60_CNT_SOCIAL_CIRCLE')
        self.DAYS_LAST_PHONE_CHANGE = data.get('DAYS_LAST_PHONE_CHANGE')
        self.FLAG_DOCUMENT_2 = data.get('FLAG_DOCUMENT_2')
        self.FLAG_DOCUMENT_3 = data.get('FLAG_DOCUMENT_3')
        self.FLAG_DOCUMENT_4 = data.get('FLAG_DOCUMENT_4')
        self.FLAG_DOCUMENT_5 = data.get('FLAG_DOCUMENT_5')
        self.FLAG_DOCUMENT_6 = data.get('FLAG_DOCUMENT_6')
        self.FLAG_DOCUMENT_7 = data.get('FLAG_DOCUMENT_7')
        self.FLAG_DOCUMENT_8 = data.get('FLAG_DOCUMENT_8')
        self.FLAG_DOCUMENT_9 = data.get('FLAG_DOCUMENT_9')
        self.FLAG_DOCUMENT_10 = data.get('FLAG_DOCUMENT_10')
        self.FLAG_DOCUMENT_11 = data.get('FLAG_DOCUMENT_11')
        self.FLAG_DOCUMENT_12 = data.get('FLAG_DOCUMENT_12')
        self.FLAG_DOCUMENT_13 = data.get('FLAG_DOCUMENT_13')
        self.FLAG_DOCUMENT_14 = data.get('FLAG_DOCUMENT_14')
        self.FLAG_DOCUMENT_15 = data.get('FLAG_DOCUMENT_15')
        self.FLAG_DOCUMENT_16 = data.get('FLAG_DOCUMENT_16')
        self.FLAG_DOCUMENT_17 = data.get('FLAG_DOCUMENT_17')
        self.FLAG_DOCUMENT_18 = data.get('FLAG_DOCUMENT_18')
        self.FLAG_DOCUMENT_19 = data.get('FLAG_DOCUMENT_19')
        self.FLAG_DOCUMENT_20 = data.get('FLAG_DOCUMENT_20')
        self.FLAG_DOCUMENT_21 = data.get('FLAG_DOCUMENT_21')
        self.AMT_REQ_CREDIT_BUREAU_HOUR = data.get(
            'AMT_REQ_CREDIT_BUREAU_HOUR')
        self.AMT_REQ_CREDIT_BUREAU_DAY = data.get('AMT_REQ_CREDIT_BUREAU_DAY')
        self.AMT_REQ_CREDIT_BUREAU_WEEK = data.get(
            'AMT_REQ_CREDIT_BUREAU_WEEK')
        self.AMT_REQ_CREDIT_BUREAU_MON = data.get('AMT_REQ_CREDIT_BUREAU_MON')
        self.AMT_REQ_CREDIT_BUREAU_QRT = data.get('AMT_REQ_CREDIT_BUREAU_QRT')
        self.AMT_REQ_CREDIT_BUREAU_YEAR = data.get(
            'AMT_REQ_CREDIT_BUREAU_YEAR')
        self.APP_CREDIT_TO_ANNUITY_RATIO = data.get(
            'APP_CREDIT_TO_ANNUITY_RATIO')
        self.APP_CREDIT_TO_GOODS_RATIO = data.get('APP_CREDIT_TO_GOODS_RATIO')
        self.APP_INC_PER_CHLD = data.get('APP_INC_PER_CHLD')
        self.APP_EMPLOY_TO_BIRTH_RATIO = data.get('APP_EMPLOY_TO_BIRTH_RATIO')
        self.APP_EMPLOY_TO_BIRTH_18_RATIO = data.get(
            'APP_EMPLOY_TO_BIRTH_18_RATIO')
        self.APP_BIRTH_TO_EMPLOY_RATIO = data.get('APP_BIRTH_TO_EMPLOY_RATIO')
        self.APP_INCOME_TO_ANNUITY_RATIO = data.get(
            'APP_INCOME_TO_ANNUITY_RATIO')
        self.APP_ANNUITY_TO_INCOME_RATIO = data.get(
            'APP_ANNUITY_TO_INCOME_RATIO')
        self.APP_EXT_SOURCES_MEAN = data.get('APP_EXT_SOURCES_MEAN')
        self.APP_EXT_SOURCES_MAX = data.get('APP_EXT_SOURCES_MAX')
        self.APP_EXT_SOURCES_MIN = data.get('APP_EXT_SOURCES_MIN')
        self.APP_CAR_TO_BIRTH_RATIO = data.get('APP_CAR_TO_BIRTH_RATIO')
        self.APP_CAR_TO_EMPLOY_RATIO = data.get('APP_CAR_TO_EMPLOY_RATIO')
        self.APP_PHONE_TO_BIRTH_RATIO = data.get('APP_PHONE_TO_BIRTH_RATIO')
        self.APP_PHONE_TO_EMPLOYED_RATIO = data.get(
            'APP_PHONE_TO_EMPLOYED_RATIO')
        self.APP_CREDIT_TO_INCOME_RATIO = data.get(
            'APP_CREDIT_TO_INCOME_RATIO')
        self.APP_PAYMENT_RATE = data.get('APP_PAYMENT_RATE')
        self.APP_INCOME_CREDIT_PERC = data.get('APP_INCOME_CREDIT_PERC')
        self.APP_INCOME_PER_PERSON = data.get('APP_INCOME_PER_PERSON')
        self.NAME_CONTRACT_TYPE_Cash_loans = data.get(
            'NAME_CONTRACT_TYPE_Cash_loans')
        self.NAME_CONTRACT_TYPE_Revolving_loans = data.get(
            'NAME_CONTRACT_TYPE_Revolving_loans')
        self.NAME_TYPE_SUITE_Children = data.get('NAME_TYPE_SUITE_Children')
        self.NAME_TYPE_SUITE_Family = data.get('NAME_TYPE_SUITE_Family')
        self.NAME_TYPE_SUITE_Group_of_people = data.get(
            'NAME_TYPE_SUITE_Group_of_people')
        self.NAME_TYPE_SUITE_Other_A = data.get('NAME_TYPE_SUITE_Other_A')
        self.NAME_TYPE_SUITE_Other_B = data.get('NAME_TYPE_SUITE_Other_B')
        self.NAME_TYPE_SUITE_Spouse_partner = data.get(
            'NAME_TYPE_SUITE_Spouse_partner')
        self.NAME_TYPE_SUITE_Unaccompanied = data.get(
            'NAME_TYPE_SUITE_Unaccompanied')
        self.NAME_INCOME_TYPE_Businessman = data.get(
            'NAME_INCOME_TYPE_Businessman')
        self.NAME_INCOME_TYPE_Commercial_associate = data.get(
            'NAME_INCOME_TYPE_Commercial_associate')
        self.NAME_INCOME_TYPE_Maternity_leave = data.get(
            'NAME_INCOME_TYPE_Maternity_leave')
        self.NAME_INCOME_TYPE_Pensioner = data.get(
            'NAME_INCOME_TYPE_Pensioner')
        self.NAME_INCOME_TYPE_State_servant = data.get(
            'NAME_INCOME_TYPE_State_servant')
        self.NAME_INCOME_TYPE_Student = data.get('NAME_INCOME_TYPE_Student')
        self.NAME_INCOME_TYPE_Unemployed = data.get(
            'NAME_INCOME_TYPE_Unemployed')
        self.NAME_INCOME_TYPE_Working = data.get('NAME_INCOME_TYPE_Working')
        self.NAME_EDUCATION_TYPE_Academic_degree = data.get(
            'NAME_EDUCATION_TYPE_Academic_degree')
        self.NAME_EDUCATION_TYPE_Higher_education = data.get(
            'NAME_EDUCATION_TYPE_Higher_education')
        self.NAME_EDUCATION_TYPE_Incomplete_higher = data.get(
            'NAME_EDUCATION_TYPE_Incomplete_higher')
        self.NAME_EDUCATION_TYPE_Lower_secondary = data.get(
            'NAME_EDUCATION_TYPE_Lower_secondary')
        self.NAME_EDUCATION_TYPE_Secondary_secondary_special = data.get(
            'NAME_EDUCATION_TYPE_Secondary_secondary_special')
        self.NAME_FAMILY_STATUS_Civil_marriage = data.get(
            'NAME_FAMILY_STATUS_Civil_marriage')
        self.NAME_FAMILY_STATUS_Married = data.get(
            'NAME_FAMILY_STATUS_Married')
        self.NAME_FAMILY_STATUS_Separated = data.get(
            'NAME_FAMILY_STATUS_Separated')
        self.NAME_FAMILY_STATUS_Single_not_married = data.get(
            'NAME_FAMILY_STATUS_Single_not_married')
        self.NAME_FAMILY_STATUS_Unknown = data.get(
            'NAME_FAMILY_STATUS_Unknown')
        self.NAME_FAMILY_STATUS_Widow = data.get('NAME_FAMILY_STATUS_Widow')
        self.NAME_HOUSING_TYPE_Co_op_apartment = data.get(
            'NAME_HOUSING_TYPE_Co_op_apartment')
        self.NAME_HOUSING_TYPE_House_apartment = data.get(
            'NAME_HOUSING_TYPE_House_apartment')
        self.NAME_HOUSING_TYPE_Municipal_apartment = data.get(
            'NAME_HOUSING_TYPE_Municipal_apartment')
        self.NAME_HOUSING_TYPE_Office_apartment = data.get(
            'NAME_HOUSING_TYPE_Office_apartment')
        self.NAME_HOUSING_TYPE_Rented_apartment = data.get(
            'NAME_HOUSING_TYPE_Rented_apartment')
        self.NAME_HOUSING_TYPE_With_parents = data.get(
            'NAME_HOUSING_TYPE_With_parents')
        self.OCCUPATION_TYPE_Accountants = data.get(
            'OCCUPATION_TYPE_Accountants')
        self.OCCUPATION_TYPE_Cleaning_staff = data.get(
            'OCCUPATION_TYPE_Cleaning_staff')
        self.OCCUPATION_TYPE_Cooking_staff = data.get(
            'OCCUPATION_TYPE_Cooking_staff')
        self.OCCUPATION_TYPE_Core_staff = data.get(
            'OCCUPATION_TYPE_Core_staff')
        self.OCCUPATION_TYPE_Drivers = data.get('OCCUPATION_TYPE_Drivers')
        self.OCCUPATION_TYPE_HR_staff = data.get('OCCUPATION_TYPE_HR_staff')
        self.OCCUPATION_TYPE_High_skill_tech_staff = data.get(
            'OCCUPATION_TYPE_High_skill_tech_staff')
        self.OCCUPATION_TYPE_IT_staff = data.get('OCCUPATION_TYPE_IT_staff')
        self.OCCUPATION_TYPE_Laborers = data.get('OCCUPATION_TYPE_Laborers')
        self.OCCUPATION_TYPE_Low_skill_Laborers = data.get(
            'OCCUPATION_TYPE_Low_skill_Laborers')
        self.OCCUPATION_TYPE_Managers = data.get('OCCUPATION_TYPE_Managers')
        self.OCCUPATION_TYPE_Medicine_staff = data.get(
            'OCCUPATION_TYPE_Medicine_staff')
        self.OCCUPATION_TYPE_Private_service_staff = data.get(
            'OCCUPATION_TYPE_Private_service_staff')
        self.OCCUPATION_TYPE_Realty_agents = data.get(
            'OCCUPATION_TYPE_Realty_agents')
        self.OCCUPATION_TYPE_Sales_staff = data.get(
            'OCCUPATION_TYPE_Sales_staff')
        self.OCCUPATION_TYPE_Secretaries = data.get(
            'OCCUPATION_TYPE_Secretaries')
        self.OCCUPATION_TYPE_Security_staff = data.get(
            'OCCUPATION_TYPE_Security_staff')
        self.OCCUPATION_TYPE_Waiters_barmen_staff = data.get(
            'OCCUPATION_TYPE_Waiters_barmen_staff')
        self.WEEKDAY_APPR_PROCESS_START_FRIDAY = data.get(
            'WEEKDAY_APPR_PROCESS_START_FRIDAY')
        self.WEEKDAY_APPR_PROCESS_START_MONDAY = data.get(
            'WEEKDAY_APPR_PROCESS_START_MONDAY')
        self.WEEKDAY_APPR_PROCESS_START_SATURDAY = data.get(
            'WEEKDAY_APPR_PROCESS_START_SATURDAY')
        self.WEEKDAY_APPR_PROCESS_START_SUNDAY = data.get(
            'WEEKDAY_APPR_PROCESS_START_SUNDAY')
        self.WEEKDAY_APPR_PROCESS_START_THURSDAY = data.get(
            'WEEKDAY_APPR_PROCESS_START_THURSDAY')
        self.WEEKDAY_APPR_PROCESS_START_TUESDAY = data.get(
            'WEEKDAY_APPR_PROCESS_START_TUESDAY')
        self.WEEKDAY_APPR_PROCESS_START_WEDNESDAY = data.get(
            'WEEKDAY_APPR_PROCESS_START_WEDNESDAY')
        self.ORGANIZATION_TYPE_Advertising = data.get(
            'ORGANIZATION_TYPE_Advertising')
        self.ORGANIZATION_TYPE_Agriculture = data.get(
            'ORGANIZATION_TYPE_Agriculture')
        self.ORGANIZATION_TYPE_Bank = data.get('ORGANIZATION_TYPE_Bank')
        self.ORGANIZATION_TYPE_Business_Entity_Type_1 = data.get(
            'ORGANIZATION_TYPE_Business_Entity_Type_1')
        self.ORGANIZATION_TYPE_Business_Entity_Type_2 = data.get(
            'ORGANIZATION_TYPE_Business_Entity_Type_2')
        self.ORGANIZATION_TYPE_Business_Entity_Type_3 = data.get(
            'ORGANIZATION_TYPE_Business_Entity_Type_3')
        self.ORGANIZATION_TYPE_Cleaning = data.get(
            'ORGANIZATION_TYPE_Cleaning')
        self.ORGANIZATION_TYPE_Construction = data.get(
            'ORGANIZATION_TYPE_Construction')
        self.ORGANIZATION_TYPE_Culture = data.get('ORGANIZATION_TYPE_Culture')
        self.ORGANIZATION_TYPE_Electricity = data.get(
            'ORGANIZATION_TYPE_Electricity')
        self.ORGANIZATION_TYPE_Emergency = data.get(
            'ORGANIZATION_TYPE_Emergency')
        self.ORGANIZATION_TYPE_Government = data.get(
            'ORGANIZATION_TYPE_Government')
        self.ORGANIZATION_TYPE_Hotel = data.get('ORGANIZATION_TYPE_Hotel')
        self.ORGANIZATION_TYPE_Housing = data.get('ORGANIZATION_TYPE_Housing')
        self.ORGANIZATION_TYPE_Industry_type_1 = data.get(
            'ORGANIZATION_TYPE_Industry_type_1')
        self.ORGANIZATION_TYPE_Industry_type_10 = data.get(
            'ORGANIZATION_TYPE_Industry_type_10')
        self.ORGANIZATION_TYPE_Industry_type_11 = data.get(
            'ORGANIZATION_TYPE_Industry_type_11')
        self.ORGANIZATION_TYPE_Industry_type_12 = data.get(
            'ORGANIZATION_TYPE_Industry_type_12')
        self.ORGANIZATION_TYPE_Industry_type_13 = data.get(
            'ORGANIZATION_TYPE_Industry_type_13')
        self.ORGANIZATION_TYPE_Industry_type_2 = data.get(
            'ORGANIZATION_TYPE_Industry_type_2')
        self.ORGANIZATION_TYPE_Industry_type_3 = data.get(
            'ORGANIZATION_TYPE_Industry_type_3')
        self.ORGANIZATION_TYPE_Industry_type_4 = data.get(
            'ORGANIZATION_TYPE_Industry_type_4')
        self.ORGANIZATION_TYPE_Industry_type_5 = data.get(
            'ORGANIZATION_TYPE_Industry_type_5')
        self.ORGANIZATION_TYPE_Industry_type_6 = data.get(
            'ORGANIZATION_TYPE_Industry_type_6')
        self.ORGANIZATION_TYPE_Industry_type_7 = data.get(
            'ORGANIZATION_TYPE_Industry_type_7')
        self.ORGANIZATION_TYPE_Industry_type_8 = data.get(
            'ORGANIZATION_TYPE_Industry_type_8')
        self.ORGANIZATION_TYPE_Industry_type_9 = data.get(
            'ORGANIZATION_TYPE_Industry_type_9')
        self.ORGANIZATION_TYPE_Insurance = data.get(
            'ORGANIZATION_TYPE_Insurance')
        self.ORGANIZATION_TYPE_Kindergarten = data.get(
            'ORGANIZATION_TYPE_Kindergarten')
        self.ORGANIZATION_TYPE_Legal_Services = data.get(
            'ORGANIZATION_TYPE_Legal_Services')
        self.ORGANIZATION_TYPE_Medicine = data.get(
            'ORGANIZATION_TYPE_Medicine')
        self.ORGANIZATION_TYPE_Military = data.get(
            'ORGANIZATION_TYPE_Military')
        self.ORGANIZATION_TYPE_Mobile = data.get('ORGANIZATION_TYPE_Mobile')
        self.ORGANIZATION_TYPE_Other = data.get('ORGANIZATION_TYPE_Other')
        self.ORGANIZATION_TYPE_Police = data.get('ORGANIZATION_TYPE_Police')
        self.ORGANIZATION_TYPE_Postal = data.get('ORGANIZATION_TYPE_Postal')
        self.ORGANIZATION_TYPE_Realtor = data.get('ORGANIZATION_TYPE_Realtor')
        self.ORGANIZATION_TYPE_Religion = data.get(
            'ORGANIZATION_TYPE_Religion')
        self.ORGANIZATION_TYPE_Restaurant = data.get(
            'ORGANIZATION_TYPE_Restaurant')
        self.ORGANIZATION_TYPE_School = data.get('ORGANIZATION_TYPE_School')
        self.ORGANIZATION_TYPE_Security = data.get(
            'ORGANIZATION_TYPE_Security')
        self.ORGANIZATION_TYPE_Security_Ministries = data.get(
            'ORGANIZATION_TYPE_Security_Ministries')
        self.ORGANIZATION_TYPE_Self_employed = data.get(
            'ORGANIZATION_TYPE_Self_employed')
        self.ORGANIZATION_TYPE_Services = data.get(
            'ORGANIZATION_TYPE_Services')
        self.ORGANIZATION_TYPE_Telecom = data.get('ORGANIZATION_TYPE_Telecom')
        self.ORGANIZATION_TYPE_Trade_type_1 = data.get(
            'ORGANIZATION_TYPE_Trade_type_1')
        self.ORGANIZATION_TYPE_Trade_type_2 = data.get(
            'ORGANIZATION_TYPE_Trade_type_2')
        self.ORGANIZATION_TYPE_Trade_type_3 = data.get(
            'ORGANIZATION_TYPE_Trade_type_3')
        self.ORGANIZATION_TYPE_Trade_type_4 = data.get(
            'ORGANIZATION_TYPE_Trade_type_4')
        self.ORGANIZATION_TYPE_Trade_type_5 = data.get(
            'ORGANIZATION_TYPE_Trade_type_5')
        self.ORGANIZATION_TYPE_Trade_type_6 = data.get(
            'ORGANIZATION_TYPE_Trade_type_6')
        self.ORGANIZATION_TYPE_Trade_type_7 = data.get(
            'ORGANIZATION_TYPE_Trade_type_7')
        self.ORGANIZATION_TYPE_Transport_type_1 = data.get(
            'ORGANIZATION_TYPE_Transport_type_1')
        self.ORGANIZATION_TYPE_Transport_type_2 = data.get(
            'ORGANIZATION_TYPE_Transport_type_2')
        self.ORGANIZATION_TYPE_Transport_type_3 = data.get(
            'ORGANIZATION_TYPE_Transport_type_3')
        self.ORGANIZATION_TYPE_Transport_type_4 = data.get(
            'ORGANIZATION_TYPE_Transport_type_4')
        self.ORGANIZATION_TYPE_University = data.get(
            'ORGANIZATION_TYPE_University')
        self.ORGANIZATION_TYPE_XNA = data.get('ORGANIZATION_TYPE_XNA')
        self.FONDKAPREMONT_MODE_not_specified = data.get(
            'FONDKAPREMONT_MODE_not_specified')
        self.FONDKAPREMONT_MODE_org_spec_account = data.get(
            'FONDKAPREMONT_MODE_org_spec_account')
        self.FONDKAPREMONT_MODE_reg_oper_account = data.get(
            'FONDKAPREMONT_MODE_reg_oper_account')
        self.FONDKAPREMONT_MODE_reg_oper_spec_account = data.get(
            'FONDKAPREMONT_MODE_reg_oper_spec_account')
        self.HOUSETYPE_MODE_block_of_flats = data.get(
            'HOUSETYPE_MODE_block_of_flats')
        self.HOUSETYPE_MODE_specific_housing = data.get(
            'HOUSETYPE_MODE_specific_housing')
        self.HOUSETYPE_MODE_terraced_house = data.get(
            'HOUSETYPE_MODE_terraced_house')
        self.WALLSMATERIAL_MODE_Block = data.get('WALLSMATERIAL_MODE_Block')
        self.WALLSMATERIAL_MODE_Mixed = data.get('WALLSMATERIAL_MODE_Mixed')
        self.WALLSMATERIAL_MODE_Monolithic = data.get(
            'WALLSMATERIAL_MODE_Monolithic')
        self.WALLSMATERIAL_MODE_Others = data.get('WALLSMATERIAL_MODE_Others')
        self.WALLSMATERIAL_MODE_Panel = data.get('WALLSMATERIAL_MODE_Panel')
        self.WALLSMATERIAL_MODE_Stone_brick = data.get(
            'WALLSMATERIAL_MODE_Stone_brick')
        self.WALLSMATERIAL_MODE_Wooden = data.get('WALLSMATERIAL_MODE_Wooden')
        self.EMERGENCYSTATE_MODE_No = data.get('EMERGENCYSTATE_MODE_No')
        self.EMERGENCYSTATE_MODE_Yes = data.get('EMERGENCYSTATE_MODE_Yes')
        self.BURO_DAYS_CREDIT_MEAN = data.get('BURO_DAYS_CREDIT_MEAN')
        self.BURO_DAYS_CREDIT_VAR = data.get('BURO_DAYS_CREDIT_VAR')
        self.BURO_DAYS_CREDIT_ENDDATE_MEAN = data.get(
            'BURO_DAYS_CREDIT_ENDDATE_MEAN')
        self.BURO_DAYS_CREDIT_UPDATE_MEAN = data.get(
            'BURO_DAYS_CREDIT_UPDATE_MEAN')
        self.BURO_CREDIT_DAY_OVERDUE_MEAN = data.get(
            'BURO_CREDIT_DAY_OVERDUE_MEAN')
        self.BURO_AMT_CREDIT_MAX_OVERDUE_MEAN = data.get(
            'BURO_AMT_CREDIT_MAX_OVERDUE_MEAN')
        self.BURO_AMT_CREDIT_SUM_MEAN = data.get('BURO_AMT_CREDIT_SUM_MEAN')
        self.BURO_AMT_CREDIT_SUM_SUM = data.get('BURO_AMT_CREDIT_SUM_SUM')
        self.BURO_AMT_CREDIT_SUM_DEBT_MEAN = data.get(
            'BURO_AMT_CREDIT_SUM_DEBT_MEAN')
        self.BURO_AMT_CREDIT_SUM_DEBT_SUM = data.get(
            'BURO_AMT_CREDIT_SUM_DEBT_SUM')
        self.BURO_AMT_CREDIT_SUM_OVERDUE_MEAN = data.get(
            'BURO_AMT_CREDIT_SUM_OVERDUE_MEAN')
        self.BURO_AMT_CREDIT_SUM_LIMIT_MEAN = data.get(
            'BURO_AMT_CREDIT_SUM_LIMIT_MEAN')
        self.BURO_AMT_CREDIT_SUM_LIMIT_SUM = data.get(
            'BURO_AMT_CREDIT_SUM_LIMIT_SUM')
        self.BURO_AMT_ANNUITY_MAX = data.get('BURO_AMT_ANNUITY_MAX')
        self.BURO_AMT_ANNUITY_MEAN = data.get('BURO_AMT_ANNUITY_MEAN')
        self.BURO_CNT_CREDIT_PROLONG_SUM = data.get(
            'BURO_CNT_CREDIT_PROLONG_SUM')
        self.BURO_MONTHS_BALANCE_MIN_MIN = data.get(
            'BURO_MONTHS_BALANCE_MIN_MIN')
        self.BURO_MONTHS_BALANCE_MAX_MAX = data.get(
            'BURO_MONTHS_BALANCE_MAX_MAX')
        self.BURO_MONTHS_BALANCE_SIZE_MEAN = data.get(
            'BURO_MONTHS_BALANCE_SIZE_MEAN')
        self.BURO_MONTHS_BALANCE_SIZE_SUM = data.get(
            'BURO_MONTHS_BALANCE_SIZE_SUM')
        self.BURO_CREDIT_ACTIVE_Active_MEAN = data.get(
            'BURO_CREDIT_ACTIVE_Active_MEAN')
        self.BURO_CREDIT_ACTIVE_Bad_debt_MEAN = data.get(
            'BURO_CREDIT_ACTIVE_Bad_debt_MEAN')
        self.BURO_CREDIT_ACTIVE_Closed_MEAN = data.get(
            'BURO_CREDIT_ACTIVE_Closed_MEAN')
        self.BURO_CREDIT_ACTIVE_Sold_MEAN = data.get(
            'BURO_CREDIT_ACTIVE_Sold_MEAN')
        self.BURO_CREDIT_ACTIVE_nan_MEAN = data.get(
            'BURO_CREDIT_ACTIVE_nan_MEAN')
        self.BURO_CREDIT_CURRENCY_currency_1_MEAN = data.get(
            'BURO_CREDIT_CURRENCY_currency_1_MEAN')
        self.BURO_CREDIT_CURRENCY_currency_2_MEAN = data.get(
            'BURO_CREDIT_CURRENCY_currency_2_MEAN')
        self.BURO_CREDIT_CURRENCY_currency_3_MEAN = data.get(
            'BURO_CREDIT_CURRENCY_currency_3_MEAN')
        self.BURO_CREDIT_CURRENCY_currency_4_MEAN = data.get(
            'BURO_CREDIT_CURRENCY_currency_4_MEAN')
        self.BURO_CREDIT_CURRENCY_nan_MEAN = data.get(
            'BURO_CREDIT_CURRENCY_nan_MEAN')
        self.BURO_CREDIT_TYPE_Another_type_of_loan_MEAN = data.get(
            'BURO_CREDIT_TYPE_Another_type_of_loan_MEAN')
        self.BURO_CREDIT_TYPE_Car_loan_MEAN = data.get(
            'BURO_CREDIT_TYPE_Car_loan_MEAN')
        self.BURO_CREDIT_TYPE_Cash_loan__non_earmarked__MEAN = data.get(
            'BURO_CREDIT_TYPE_Cash_loan__non_earmarked__MEAN')
        self.BURO_CREDIT_TYPE_Consumer_credit_MEAN = data.get(
            'BURO_CREDIT_TYPE_Consumer_credit_MEAN')
        self.BURO_CREDIT_TYPE_Credit_card_MEAN = data.get(
            'BURO_CREDIT_TYPE_Credit_card_MEAN')
        self.BURO_CREDIT_TYPE_Interbank_credit_MEAN = data.get(
            'BURO_CREDIT_TYPE_Interbank_credit_MEAN')
        self.BURO_CREDIT_TYPE_Loan_for_business_development_MEAN = data.get(
            'BURO_CREDIT_TYPE_Loan_for_business_development_MEAN')
        self.BURO_CREDIT_TYPE_Loan_for_purchase_of_shares__margin_lending__MEAN = data.get(
            'BURO_CREDIT_TYPE_Loan_for_purchase_of_shares__margin_lending__MEAN')
        self.BURO_CREDIT_TYPE_Loan_for_the_purchase_of_equipment_MEAN = data.get(
            'BURO_CREDIT_TYPE_Loan_for_the_purchase_of_equipment_MEAN')
        self.BURO_CREDIT_TYPE_Loan_for_working_capital_replenishment_MEAN = data.get(
            'BURO_CREDIT_TYPE_Loan_for_working_capital_replenishment_MEAN')
        self.BURO_CREDIT_TYPE_Microloan_MEAN = data.get(
            'BURO_CREDIT_TYPE_Microloan_MEAN')
        self.BURO_CREDIT_TYPE_Mobile_operator_loan_MEAN = data.get(
            'BURO_CREDIT_TYPE_Mobile_operator_loan_MEAN')
        self.BURO_CREDIT_TYPE_Mortgage_MEAN = data.get(
            'BURO_CREDIT_TYPE_Mortgage_MEAN')
        self.BURO_CREDIT_TYPE_Real_estate_loan_MEAN = data.get(
            'BURO_CREDIT_TYPE_Real_estate_loan_MEAN')
        self.BURO_CREDIT_TYPE_Unknown_type_of_loan_MEAN = data.get(
            'BURO_CREDIT_TYPE_Unknown_type_of_loan_MEAN')
        self.BURO_CREDIT_TYPE_nan_MEAN = data.get('BURO_CREDIT_TYPE_nan_MEAN')
        self.BURO_STATUS_0_MEAN_MEAN = data.get('BURO_STATUS_0_MEAN_MEAN')
        self.BURO_STATUS_1_MEAN_MEAN = data.get('BURO_STATUS_1_MEAN_MEAN')
        self.BURO_STATUS_2_MEAN_MEAN = data.get('BURO_STATUS_2_MEAN_MEAN')
        self.BURO_STATUS_3_MEAN_MEAN = data.get('BURO_STATUS_3_MEAN_MEAN')
        self.BURO_STATUS_4_MEAN_MEAN = data.get('BURO_STATUS_4_MEAN_MEAN')
        self.BURO_STATUS_5_MEAN_MEAN = data.get('BURO_STATUS_5_MEAN_MEAN')
        self.BURO_STATUS_C_MEAN_MEAN = data.get('BURO_STATUS_C_MEAN_MEAN')
        self.BURO_STATUS_X_MEAN_MEAN = data.get('BURO_STATUS_X_MEAN_MEAN')
        self.BURO_STATUS_nan_MEAN_MEAN = data.get('BURO_STATUS_nan_MEAN_MEAN')
        self.ACTIVE_DAYS_CREDIT_MEAN = data.get('ACTIVE_DAYS_CREDIT_MEAN')
        self.ACTIVE_DAYS_CREDIT_VAR = data.get('ACTIVE_DAYS_CREDIT_VAR')
        self.ACTIVE_DAYS_CREDIT_ENDDATE_MEAN = data.get(
            'ACTIVE_DAYS_CREDIT_ENDDATE_MEAN')
        self.ACTIVE_DAYS_CREDIT_UPDATE_MEAN = data.get(
            'ACTIVE_DAYS_CREDIT_UPDATE_MEAN')
        self.ACTIVE_CREDIT_DAY_OVERDUE_MEAN = data.get(
            'ACTIVE_CREDIT_DAY_OVERDUE_MEAN')
        self.ACTIVE_AMT_CREDIT_MAX_OVERDUE_MEAN = data.get(
            'ACTIVE_AMT_CREDIT_MAX_OVERDUE_MEAN')
        self.ACTIVE_AMT_CREDIT_SUM_MEAN = data.get(
            'ACTIVE_AMT_CREDIT_SUM_MEAN')
        self.ACTIVE_AMT_CREDIT_SUM_SUM = data.get('ACTIVE_AMT_CREDIT_SUM_SUM')
        self.ACTIVE_AMT_CREDIT_SUM_DEBT_MEAN = data.get(
            'ACTIVE_AMT_CREDIT_SUM_DEBT_MEAN')
        self.ACTIVE_AMT_CREDIT_SUM_DEBT_SUM = data.get(
            'ACTIVE_AMT_CREDIT_SUM_DEBT_SUM')
        self.ACTIVE_AMT_CREDIT_SUM_OVERDUE_MEAN = data.get(
            'ACTIVE_AMT_CREDIT_SUM_OVERDUE_MEAN')
        self.ACTIVE_AMT_CREDIT_SUM_LIMIT_MEAN = data.get(
            'ACTIVE_AMT_CREDIT_SUM_LIMIT_MEAN')
        self.ACTIVE_AMT_CREDIT_SUM_LIMIT_SUM = data.get(
            'ACTIVE_AMT_CREDIT_SUM_LIMIT_SUM')
        self.ACTIVE_AMT_ANNUITY_MAX = data.get('ACTIVE_AMT_ANNUITY_MAX')
        self.ACTIVE_AMT_ANNUITY_MEAN = data.get('ACTIVE_AMT_ANNUITY_MEAN')
        self.ACTIVE_CNT_CREDIT_PROLONG_SUM = data.get(
            'ACTIVE_CNT_CREDIT_PROLONG_SUM')
        self.ACTIVE_MONTHS_BALANCE_MIN_MIN = data.get(
            'ACTIVE_MONTHS_BALANCE_MIN_MIN')
        self.ACTIVE_MONTHS_BALANCE_MAX_MAX = data.get(
            'ACTIVE_MONTHS_BALANCE_MAX_MAX')
        self.ACTIVE_MONTHS_BALANCE_SIZE_MEAN = data.get(
            'ACTIVE_MONTHS_BALANCE_SIZE_MEAN')
        self.ACTIVE_MONTHS_BALANCE_SIZE_SUM = data.get(
            'ACTIVE_MONTHS_BALANCE_SIZE_SUM')
        self.CLOSED_DAYS_CREDIT_MEAN = data.get('CLOSED_DAYS_CREDIT_MEAN')
        self.CLOSED_DAYS_CREDIT_VAR = data.get('CLOSED_DAYS_CREDIT_VAR')
        self.CLOSED_DAYS_CREDIT_ENDDATE_MEAN = data.get(
            'CLOSED_DAYS_CREDIT_ENDDATE_MEAN')
        self.CLOSED_DAYS_CREDIT_UPDATE_MEAN = data.get(
            'CLOSED_DAYS_CREDIT_UPDATE_MEAN')
        self.CLOSED_CREDIT_DAY_OVERDUE_MEAN = data.get(
            'CLOSED_CREDIT_DAY_OVERDUE_MEAN')
        self.CLOSED_AMT_CREDIT_MAX_OVERDUE_MEAN = data.get(
            'CLOSED_AMT_CREDIT_MAX_OVERDUE_MEAN')
        self.CLOSED_AMT_CREDIT_SUM_MEAN = data.get(
            'CLOSED_AMT_CREDIT_SUM_MEAN')
        self.CLOSED_AMT_CREDIT_SUM_SUM = data.get('CLOSED_AMT_CREDIT_SUM_SUM')
        self.CLOSED_AMT_CREDIT_SUM_DEBT_MEAN = data.get(
            'CLOSED_AMT_CREDIT_SUM_DEBT_MEAN')
        self.CLOSED_AMT_CREDIT_SUM_DEBT_SUM = data.get(
            'CLOSED_AMT_CREDIT_SUM_DEBT_SUM')
        self.CLOSED_AMT_CREDIT_SUM_OVERDUE_MEAN = data.get(
            'CLOSED_AMT_CREDIT_SUM_OVERDUE_MEAN')
        self.CLOSED_AMT_CREDIT_SUM_LIMIT_MEAN = data.get(
            'CLOSED_AMT_CREDIT_SUM_LIMIT_MEAN')
        self.CLOSED_AMT_CREDIT_SUM_LIMIT_SUM = data.get(
            'CLOSED_AMT_CREDIT_SUM_LIMIT_SUM')
        self.CLOSED_AMT_ANNUITY_MAX = data.get('CLOSED_AMT_ANNUITY_MAX')
        self.CLOSED_AMT_ANNUITY_MEAN = data.get('CLOSED_AMT_ANNUITY_MEAN')
        self.CLOSED_CNT_CREDIT_PROLONG_SUM = data.get(
            'CLOSED_CNT_CREDIT_PROLONG_SUM')
        self.CLOSED_MONTHS_BALANCE_MIN_MIN = data.get(
            'CLOSED_MONTHS_BALANCE_MIN_MIN')
        self.CLOSED_MONTHS_BALANCE_MAX_MAX = data.get(
            'CLOSED_MONTHS_BALANCE_MAX_MAX')
        self.CLOSED_MONTHS_BALANCE_SIZE_MEAN = data.get(
            'CLOSED_MONTHS_BALANCE_SIZE_MEAN')
        self.CLOSED_MONTHS_BALANCE_SIZE_SUM = data.get(
            'CLOSED_MONTHS_BALANCE_SIZE_SUM')
