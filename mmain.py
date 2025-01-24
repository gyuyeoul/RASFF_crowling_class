from Oracle_uploader import OracleUploader_RASFF
from Crowling import crowling_rasff_details
import time


class Upload_RASFF:
    def __init__(
        self,
        db_user_name,
        db_password,
        db_host,
        db_port,
        db_sid,
        page_number,
        rasff_part,
    ):
        self.db_user_name = db_user_name
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_sid = db_sid
        self.page_number = page_number
        self.rasff_part = rasff_part
        self.run()

    def run(self):
        oracleUploader_RASFF = OracleUploader_RASFF(
            self.db_user_name,
            self.db_password,
            self.db_host,
            self.db_port,
            self.db_sid,
        )
        oracleUploader_RASFF.dbConnect()

        crowling_rasff = crowling_rasff_details(self.page_number, self.rasff_part)
        crowling_rasff.rasff()
        oracleUploader_RASFF.updateOracleDB()
        oracleUploader_RASFF.closeOracleDB()


if __name__ == "__main__":
    db_user_name = "CIN_EDU"
    db_password = "cheminet"
    db_host = "cheminet.webhop.net"
    db_port = "4101"
    db_sid = "ORA11G"
    page_number = 10
    rasff_part = (
        "subject, hazards, measure taken, risk, organisations, follow ups, products"
    )
    # "subject, hazards, measure taken, risk, organisations, follow ups, products"
    start_time = time.time()
    Upload_RASFF(
        db_user_name, db_password, db_host, db_port, db_sid, page_number, rasff_part
    )
    end_time = time.time()

    duration = end_time - start_time

    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)

    print(f"Oracle DB 업로드 시간: {hours} 시간 {minutes}분 {seconds}초")
    print("Time : ", end_time - start_time)
