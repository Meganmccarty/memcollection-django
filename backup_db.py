import os
import datetime
# import zipfile
# from zipfile import ZipFile

BACKUP_DIR_NAME = os.getenv("BACKUP_DIR")
DAYS_TO_KEEP_BACKUP = 7
FILE_PREFIX = "db_backup_"
FILE_SUFFIX = "%Y%m%d%H%M%S"

DB_HOST = os.getenv("DATABASE_HOST")
DB_USERNAME = os.getenv("DATABASE_USER")
DB_NAME = os.getenv("DATABASE_NAME")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_PORT = os.getenv("DATABASE_PORT")

timestamp = datetime.datetime.now().strftime(FILE_SUFFIX)
backup_filename = f"{BACKUP_DIR_NAME}/{FILE_PREFIX}{timestamp}.pgdump"

os.system("PGPASSWORD='{}' pg_dump -h {} -p {} -d {} -U {} -f {} -Fc".format(
        DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, DB_USERNAME, backup_filename
    )
)

# zip_filename = f"{BACKUP_DIR_NAME}/{FILE_PREFIX}{timestamp}.zip"
# with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED) as zip:
#     zip.write(backup_filename, os.path.basename(backup_filename))
# os.remove(backup_filename)

# deleting old files
list_files = os.listdir(BACKUP_DIR_NAME)
back_date = datetime.datetime.now() - datetime.timedelta(days=DAYS_TO_KEEP_BACKUP)
back_date = back_date.strftime(FILE_SUFFIX)

length = len(FILE_PREFIX)

# deleting files older than DAYS_TO_KEEP_BACKUP days
for f in list_files:
    filename = f.split(".")[0]
    # swap out "pgdump" for "zip" if using commented out zip code above
    if "pgdump" == f.split(".")[1]:
        suffix = filename[length:]
        if suffix < back_date:
            print("Deleting file : "+f)
            os.remove(BACKUP_DIR_NAME + "/" + f)

# restoring backup (will be prompted for db password)
# pg_restore --clean --port {number} --host {host} -U {user} --dbname {dbname} thedumpfilename
