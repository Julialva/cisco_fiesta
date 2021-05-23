import imaplib, email, os
import pandas as pd
class MailScrapper():
    def __init__(self):
        self.user = str(os.getenv('MAIL_USER'))
        self.password = str(os.getenv('MAIL_PASS'))
        self.imap_url = "imap.gmail.com"
        self.con = imaplib.IMAP4_SSL(self.imap_url)
        self.con.login(self.user,self.password)
    def find_mail(self,box="INBOX",criteria="(FROM julialva@cisco.com)"):
        self.con.select(box)
        result, data = self.con.search(None,criteria)
        mail_ids = data[0]
        mail_id_list = mail_ids.split()
        last_mail_id = mail_id_list[-1]
        path_file= "./data/last_mail_id.txt"
        if not os.path.exists(path_file):
            os.mkdir("./data")
        with open (path_file,"w+") as file:
            file_content = file.read()
            if str(last_mail_id) != file_content:
                file.write(str(last_mail_id))
                fetch_result, fetch_data = self.con.fetch(last_mail_id,"(RFC822)")
                raw = email.message_from_bytes(fetch_data[0][1])
                return raw
    def get_attachments(self,msg):
        for part in msg.walk():
            if part.get_content_maintype()=='multipart':
                continue
            if part.get("Content-Disposition") is None:
                continue
            
            file_name = part.get_filename()
            if str(part.get_content_type()) == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                if bool(file_name):
                    file_name = 'input_file.xlsx'
                    file_path = os.path.join("./data/",file_name)
                    with open(file_path,'wb') as file:
                        file.write(part.get_payload(decode=True))
class FakeMailScrapper:
    def get_attachments(self,raw=0):
        pass
    def find_mail(self):
        pass
