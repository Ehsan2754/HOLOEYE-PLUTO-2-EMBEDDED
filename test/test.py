import paramiko,time
if __name__ == '__main__':
    host = "10.10.70.1"
    port = 22
    username = "root"
    password = ""

    # sshClient = paramiko.SSHClient()
    # sshClient.connect(hostname=host, username=username, password=password)
    # channel = sshClient.get_transport().open_session()
    # channel.get_pty()
    # channel.invoke_shell()

    # while True:
    #     command = input('$ ')
    #     if command == 'exit':
    #         break

    #     channel.send(command + "\n")

    #     while True:
    #         if channel.recv_ready():
    #             output = channel.recv(1024)
    #             print(output)
    #         else:
    #             time.sleep(0.5)
    #             if not(channel.recv_ready()):
    #                 break

    # sshClient.close()

########################################

    # command = "ls"

    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(host, port, username, password)
    # while True:
    #     command = input('\n$> ')
    #     stdin, stdout, stderr = ssh.exec_command(command+';\n')
    #     lines = stdout.read()
    #     print(lines.decode())

#########################################

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password, port=22)

    channel = ssh.invoke_shell()

    out = channel.recv(9999)

    channel.send('cd /mnt\n')
    channel.send('ls\n')

    while not channel.recv_ready():
        pass
    out = channel.recv(9999)
    print(out.decode("ascii"))