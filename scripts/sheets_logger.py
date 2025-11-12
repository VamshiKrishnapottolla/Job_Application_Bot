import gspread
from google.oauth2.service_account import Credentials

def log_to_google_sheets(job_info):
    creds = Credentials.from_service_account_file("config/google_service_account.json")
    client = gspread.authorize(creds)
    sheet = client.open("Job Tracker").sheet1
    sheet.append_row([
        job_info["title"],
        job_info["company"],
        job_info["link"],
        job_info["status"]
    ])
