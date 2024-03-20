from datetime import date
import os
import zipfile
import ftplib
import configparser

today = date.today()
def ftpsendfil():
    today = date.today()

    config = configparser.ConfigParser()
    config.read('settings.ini')

    ftp_ip = config['FTP']['IP']
    ftp_username = config['FTP']['USERNAME']
    ftp_password = config['FTP']['PASSWORD']
    ftp_serverpath = config['FTP']['SERVERPATH']

    session = ftplib.FTP(ftp_ip, ftp_username, ftp_password)

    # List files in the FTP server directory
    files = session.nlst(ftp_serverpath)
    print("List of files on FTP server:")
    for file in files:
        print(file)

    file = open(f'{today}.zip','rb')                  # file to send
    session.storbinary(f'STOR {ftp_serverpath}/{today}.zip', file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()

def listserverfiles():
    config = configparser.ConfigParser()
    config.read('settings.ini')

    ftp_ip = config['FTP']['IP']
    ftp_username = config['FTP']['USERNAME']
    ftp_password = config['FTP']['PASSWORD']
    ftp_serverpath = config['FTP']['SERVERPATH']

    session = ftplib.FTP(ftp_ip, ftp_username, ftp_password)

    # List files in the FTP server directory
    files = session.nlst(ftp_serverpath)
    print("List of files on FTP server:")
    for file in files:
        print(file)



    # zips a folder

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))



config = configparser.ConfigParser()
config.read('settings.ini')

path = config['Path'][r'PATH']

checkcheck = f"{today}.zip"
isExist = os.path.exists(checkcheck) 

    #   checks if a file with the same date as you run this script exist if 
    #   not zips the path given in the top of the scirpt and sends it to FTP server delared in settings.ini
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
