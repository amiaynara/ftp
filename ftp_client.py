import ftplib
import os

host = '192.168.1.23'   # a temporary server that I crearted on my lenovo laptop
password = 'pass'
port = 2121             # this should be more than 1023
username = 'user'

ftp_client = ftplib.FTP()
ftp_client.connect(host, port)
ftp_client.login(username, password)

# download file
max_tries = 3
#local_path = '/Users/amiaynarayan/Work/s3/analyses/692/39690/ERR194151_2.10K.fastq.gz'
#remote_path = 'ERR194151_2.10K.fastq.gz'
remote_path = 'ftp_server.py'
local_path = f'/Users/amiaynarayan/learn/ftp/{remote_path}'    # if remote path is just a name
dir_path = os.path.dirname(remote_path)
file_name = os.path.basename(remote_path)
ftp_client.cwd(f'/{dir_path}')
with open(local_path, 'wb') as hand:
  ftp_client.retrbinary(f'RETR {file_name}', hand.write)
ftp_client.quit()
