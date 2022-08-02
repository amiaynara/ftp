import ftplib
import os

host = '192.168.1.23'
password = 'pass'
port = 2121
username = 'user'

ftp_client = ftplib.FTP()
ftp_client.connect(host, port)
ftp_client.login(username, password)

# download file
max_tries = 3
#local_path = '/Users/amiaynarayan/Work/s3/analyses/692/39690/ERR194151_2.10K.fastq.gz'
#remote_path = 'ERR194151_2.10K.fastq.gz'
local_path = '/Users/amiaynarayan/Work/s3/analyses/692/39690/local_mac'
remote_path = 'ftp_server.py'
dir_path = os.path.dirname(remote_path)
file_name = os.path.basename(remote_path)
ftp_client.cwd(f'/{dir_path}')
print('Changing directory ', f'/{dir_path}')
print('on the local the file should be named as : ', local_path)
print('directory was changed, to ', dir_path,'and file we will search there is', f'{file_name}')
with open(local_path, 'wb') as hand:
  ftp_client.retrbinary(f'RETR {file_name}', hand.write)
ftp_client.quit()
