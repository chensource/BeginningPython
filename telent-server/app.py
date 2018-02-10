import paramiko

HOST = '10.58.8.67'
PORT = '22'
USER = 'chenshi2'
PASSWORD = '1944520cs.'


def remote_scp(host_ip, port, remote_path, local_path, username, password):
    print(host_ip, port, remote_path, local_path, username, password)
    try:
        t = paramiko.Transport((host_ip, int(port)))
        t.connect(username=username, password=password)  # 登录远程服务器
        sftp = paramiko.SFTPClient.from_transport(t)  # sftp传输协议
        src = remote_path
        des = local_path
        sftp.get(src, des,None)
        print('done~')
    except Exception as e:
        print(e)
    finally:
        t.close()


if __name__ == '__main__':
    remote_scp(HOST, PORT, '/opt', 'D:\\test', USER, PASSWORD)
