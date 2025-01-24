import cx_Oracle as db
import warnings
import os
import pandas as pd

os.environ["NLS_LANG"] = ".UTF8"
warnings.filterwarnings("ignore")


class OracleUploader_RASFF:
    def __init__(self, db_user_name, db_password, db_host, db_port, db_sid):
        self.db_user_name = db_user_name
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_sid = db_sid
        self.con, self.cursor = self.dbConnect()

    def dbConnect(self):
        con = db.connect(
            f"{self.db_user_name}/{self.db_password}@{self.db_host}:{self.db_port}/{self.db_sid}"
        )
        cursor = con.cursor()

        return con, cursor

    def updateOracleDB(self):
        try:
            filename = r"C:\Users\adsta\OneDrive\바탕 화면\RASFF_crowling_class\RASFF_Subject_by_Hwang.xlsx"

            RASFF_subject_data = pd.read_excel(filename)
            RASFF_subject_data.fillna("NULL", inplace=True)
            RASFF_subject_data.replace("NULL", None, inplace=True)
            for _, row in RASFF_subject_data.iterrows():
                sql = """
                INSERT INTO RASFF_SUBJECT (
                    REFERENCE,
                    SUBJECT,
                    NOTIFICATION_TYPE,
                    NOTIFICATION_BASIS,
                    CLASSIFICATION,
                    RISK_DECISION
                ) VALUES (
                    :1, :2, :3, :4, :5, :6
                )
                """
                self.cursor.execute(
                    sql,
                    (
                        row["REFERENCE"],
                        row["SUBJECT"],
                        row["NOTIFICATION_TYPE"],
                        row["NOTIFICATION_BASIS"],
                        row["CLASSIFICATION"],
                        row["RISK_DECISION"],
                    ),
                )
                self.con.commit()
        except:
            pass

        try:
            filename = r"C:\Users\adsta\OneDrive\바탕 화면\RASFF_crowling_class\RASFF_Risk_by_Hwang.xlsx"
            RASFF_risk_data = pd.read_excel(filename)
            RASFF_risk_data.fillna("NULL", inplace=True)
            RASFF_risk_data.replace("NULL", None, inplace=True)
            for _, row in RASFF_risk_data.iterrows():
                sql = """
                INSERT INTO RASFF_RISK (
                    REFERENCE,
                    RISK_DECISION,
                    HAZARDS_OBSERVED,
                    NB_PERSONS_AFFENTED,
                    SYMPTOMS_ILLNESS
                ) VALUES (
                    :1, :2, :3, :4, :5
                )
                """

                self.cursor.execute(
                    sql,
                    (
                        row["REFERENCE"],
                        row["RISK_DECISION"],
                        row["HAZARDS_OBSERVED"],
                        row["NB_PERSONS_AFFENTED"],
                        row["SYMPTOMS_ILLNESS"],
                    ),
                )
                self.con.commit()
        except:
            pass

        try:
            filename = r"C:\Users\adsta\OneDrive\바탕 화면\RASFF_crowling_class\RASFF_Products_by_Hwang.xlsx"
            RASFF_Products_data = pd.read_excel(filename)
            RASFF_Products_data.fillna("NULL", inplace=True)
            RASFF_Products_data.replace("NULL", None, inplace=True)
            for _, row in RASFF_Products_data.iterrows():
                sql = """
                INSERT INTO RASFF_PRODUCTS (
                    REFERENCE,
                    CATEGORY,
                    NAME,
                    DISTRIBUTION_STATUS,
                    HAZARD,
                    MEASURES_TAKEN
                ) VALUES (
                    :1, :2, :3, :4, :5, :6
                )
                """
                self.cursor.execute(
                    sql,
                    (
                        row["REFERENCE"],
                        row["CATEGORY"],
                        row["NAME"],
                        row["DISTRIBUTION_STATUS"],
                        row["HAZARD"],
                        row["MEASURES_TAKEN"],
                    ),
                )
                self.con.commit()
        except:
            pass

        try:
            filename = r"C:\Users\adsta\OneDrive\바탕 화면\RASFF_crowling_class\RASFF_Organisation_by_Hwang.xlsx"
            RASFF_organisations_data = pd.read_excel(filename)
            RASFF_organisations_data.fillna("NULL", inplace=True)
            RASFF_organisations_data.replace("NULL", None, inplace=True)
            for _, row in RASFF_organisations_data.iterrows():
                sql = """
                INSERT INTO RASFF_ORGANISATIONS (
                    REFERENCE,
                    DATE_OF_NOTIFICATION,
                    NOTIFYING,
                    ORIGIN,
                    DISTRIBUTION,
                    OPERATOR,
                    FLAGGED_FOR_FOLLOW_UP,
                    FLAGGED_FOR_ATTENTION
                ) VALUES (
                    :1, :2, :3, :4, :5, :6, :7, :8
                )
                """
                self.cursor.execute(
                    sql,
                    (
                        row["REFERENCE"],
                        row["DATE_OF_NOTIFICATION"],
                        row["NOTIFYING"],
                        row["ORIGIN"],
                        row["DISTRIBUTION"],
                        row["OPERATOR"],
                        row["FLAGGED_FOR_FOLLOW_UP"],
                        row["FLAGGED_FOR_ATTENTION"],
                    ),
                )
                self.con.commit()
        except:
            pass

        try:
            filename = r"C:\Users\adsta\OneDrive\바탕 화면\RASFF_crowling_class\RASFF_Measures_taken_by_Hwang.xlsx"
            RASFF_Measures_taken_data = pd.read_excel(filename)
            RASFF_Measures_taken_data.fillna("NULL", inplace=True)
            RASFF_Measures_taken_data.replace("NULL", None, inplace=True)
            for _, row in RASFF_Measures_taken_data.iterrows():
                sql = """
                INSERT INTO RASFF_MEASURES_TAKEN (
                    REFERENCE,
                    COUNTRY,
                    ACTION_RA,
                    PRODUCT_NAME,
                    URL
                ) VALUES (
                    :1, :2, :3, :4, :5
                )
                """
                self.cursor.execute(
                    sql,
                    (
                        row["REFERENCE"],
                        row["COUNTRY"],
                        row["ACTION_RA"],
                        row["PRODUCT_NAME"],
                        row["URL"],
                    ),
                )
                self.con.commit()
        except:
            pass

        try:
            filename = r"C:\Users\adsta\OneDrive\바탕 화면\RASFF_crowling_class\RASFF_Hazards_by_Hwang.xlsx"
            RASFF_Hazards_data = pd.read_excel(filename)
            RASFF_Hazards_data.fillna("NULL", inplace=True)
            RASFF_Hazards_data.replace("NULL", None, inplace=True)
            for _, row in RASFF_Hazards_data.iterrows():
                sql = """
                INSERT INTO RASFF_HAZARDS (
                    REFERENCE,
                    SAMPLING,
                    HAZARD,
                    CATEGORY,
                    ANALYTICAL_RESULTS,
                    MAXIMUM
                ) VALUES (
                    :1, :2, :3, :4, :5, :6
                )
                """
                self.cursor.execute(
                    sql,
                    (
                        row["REFERENCE"],
                        row["SAMPLING"],
                        row["HAZARD"],
                        row["CATEGORY"],
                        row["ANALYTICAL_RESULTS"],
                        row["MAXIMUM"],
                    ),
                )
                self.con.commit()
        except:
            pass

        try:
            filename = r"C:\Users\adsta\OneDrive\바탕 화면\RASFF_crowling_class\RASFF_Follow_ups_by_Hwang.xlsx"
            RASFF_Follow_ups_data = pd.read_excel(filename)
            RASFF_Follow_ups_data.fillna("NULL", inplace=True)
            RASFF_Follow_ups_data.replace("NULL", None, inplace=True)
            for _, row in RASFF_Follow_ups_data.iterrows():
                sql = """
                INSERT INTO RASFF_FOLLOW_UPS (
                    REFERENCE,
                    FUP,
                    DATE_RA,
                    ORGANISATION,
                    TYPE_RA,
                    SUMMARY,
                    FLAGGED_ORGANISATIONS
                ) VALUES (
                    :1, :2, :3, :4, :5, :6, :7
                )
                """
                self.cursor.execute(
                    sql,
                    (
                        row["REFERENCE"],
                        row["FUP"],
                        row["DATE_RA"],
                        row["ORGANISATION"],
                        row["TYPE_RA"],
                        row["SUMMARY"],
                        row["FLAGGED_ORGANISATIONS"],
                    ),
                )
                self.con.commit()
        except:
            pass

    def closeOracleDB(self):
        self.cursor.close()
        self.con.close()
