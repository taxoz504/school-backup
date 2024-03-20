
from datetime import date
import os
import zipfile

today = date.today()
path = r"C:\dev\test"

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))



checkcheck = f"{today}.zip"


isExist = os.path.exists(checkcheck) 
print(isExist)

if isExist == True:
    print(f"There is already a backup from {today}")
else:
    with zipfile.ZipFile(f'{today}.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(f'{path}', zipf)
