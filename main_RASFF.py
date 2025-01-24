from codes.Crowling_RASFF import Crowling_RASFF
from codes.Oracle_upload_RASFF import OracleUploader_RASFF
import time


class Upload_RASFF:
    def __init__(
        self,
        db_user_name,
        db_password,
        db_host,
        db_port,
        db_sid,
        table_name,
        page_number,
        data_path,
    ):
        self.db_user_name = db_user_name
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_sid = db_sid
        self.table_name = table_name
        self.page_number = page_number
        self.data_path = data_path
        self.run()

    def run(self):
        oracleUploader_RASFF = OracleUploader_RASFF(
            self.db_user_name,
            self.db_password,
            self.db_host,
            self.db_port,
            self.db_sid,
            self.table_name,
        )
        oracleUploader_RASFF.dbConnect()

        crowling_rasff = Crowling_RASFF(self.page_number, self.data_path)
        RASFF_Windows_data = crowling_rasff.crowling()
        oracleUploader_RASFF.updateOracleDB(RASFF_Windows_data)
        oracleUploader_RASFF.closeOracleDB()


if __name__ == "__main__":
    db_user_name = "CIN_EDU"
    db_password = "cheminet"
    db_host = "cheminet.webhop.net"
    db_port = "4101"
    db_sid = "ORA11G"
    table_name = "RASFF_WINDOW_MAIN"
    page_number = 1
    data_path = r"C:\Users\adsta\OneDrive\바탕 화면\RASFF_crowling_class\RASFF_Window_by_Hwang.xlsx"
    start_time = time.time()
    Upload_RASFF(
        db_user_name,
        db_password,
        db_host,
        db_port,
        db_sid,
        table_name,
        page_number,
        data_path,
    )
    end_time = time.time()

    duration = end_time - start_time

    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)

    print(
        f"에어코리아 데이터 가공 및 Oracle DB 업로드 시간: {hours} 시간 {minutes}분 {seconds}초"
    )
    print("Time : ", end_time - start_time)
