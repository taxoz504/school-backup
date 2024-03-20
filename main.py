
from datetime import date
import os
import zipfile
import ftplib

today = date.today()
path = r"C:\dev\test"
def ftpsendfil():
    session = ftplib.FTP('IP','USERNAME','PASSWORD')
    file = open(f'{today}.zip','rb')                  # file to send
    session.storbinary(f'STOR {today}.zip', file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))



checkcheck = f"{today}.zip"
isExist = os.path.exists(checkcheck) 

if isExist == True:
    print(f"There is already a backup from {today}")
else:
    print("Making backup, please wait")
    with zipfile.ZipFile(f'{today}.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(f'{path}', zipf)
        print("backup complate")
        print("Senting files to remote server, pleasw wait")
        ftpsendfil()
        print("Update complate")
