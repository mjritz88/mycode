import os
import paramiko

def main():
    SRC = '/home/student/static/filestocopy'
    DEST = '/home/bender'
    USER = 'bender'
    PW = 'alta3'
    IP = '10.10.2.3'
    PORT = 22

    files = []

    try:
        files = os.listdir(SRC)

        if files:
            t = paramiko.Transport(IP, PORT)

            t.connect(username=USER, password=PW)

            sftp = paramiko.SFTPClient.from_transport(t)

            for file in files:
                if not os.path.isdir(SRC + '/' + file):
                    print(f'Copying file "{file}" to {USER}')
                    sftp.put(SRC + '/' + file, DEST + '/' + file)

            sftp.close()
        else:
            print(f'There are no files in the {SRC} directory.')

    except FileNotFoundError:
        print(f'{SRC}: directory not found')


##### BEGINNING OF MAIN #####

main()
