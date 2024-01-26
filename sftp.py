import pysftp

host = 'test.rebex.net'
port = 22
username = 'demo'
password = 'password'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(host=host, port=port, username=username, password=password, cnopts=cnopts) as sftp:
    file_list = sftp.listdir()
    print(file_list)
# parimiko
