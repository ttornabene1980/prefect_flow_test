import os
from prefect import flow, task, get_run_logger
import pandas as pd
import pysftp
from sqlalchemy import create_engine
from io import StringIO

# --- CONFIGURATION ---
SFTP_HOST = '10.199.146.28'
SFTP_PORT = 22
SFTP_USERNAME = 'sebc'
SFTP_PASSWORD = 'sebc'
SFTP_REMOTE_FOLDER = '/home/sebc/sorgente_mefa_memdif/tino'

DB_CONNECTION_STRING = 'postgresql+psycopg2://user:password@host:port/database'
DB_TABLE_NAME = 'your_table'

LOCAL_FOLDER = './local'
EXCEL_FILE_PATH = './local/file.xlsx'
EXCEL_COLUMN_NAME = 'filename'  # Column in Excel with file names


# --- TASKS ---
@task
def read_file_list_from_excel() -> list:
    logger = get_run_logger()
    df = pd.read_excel(EXCEL_FILE_PATH)
    logger.info(f"Loaded Excel file with {len(df)} entries.")
    
    file_list = df[EXCEL_COLUMN_NAME].dropna().tolist()
    logger.info(f"Extracted {len(file_list)} file names.")
    return file_list

@task
def upload_files_to_sftp(file_list: list):
    logger = get_run_logger()
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  # Disable for testing only

    with pysftp.Connection(SFTP_HOST, username=SFTP_USERNAME, password=SFTP_PASSWORD, cnopts=cnopts) as sftp:
        logger.info("Connected to SFTP.")
        
        for file_name in file_list:
            local_file_path = os.path.join(LOCAL_FOLDER, file_name)
            if os.path.isfile(local_file_path):
                sftp.put(local_file_path, os.path.join(SFTP_REMOTE_FOLDER, file_name))
                logger.info(f"Uploaded {file_name} to {SFTP_REMOTE_FOLDER}.")
            else:
                logger.warning(f"File not found locally: {local_file_path}")


# --- FLOW ---
@flow(name="Excel to SFTP file copy flow")
def excel_to_sftp_flow():
    file_list = read_file_list_from_excel()
    upload_files_to_sftp(file_list)

# --- ENTRY POINT ---
if __name__ == "__main__":
    excel_to_sftp_flow()
    