import sys
import atheris
import paramiko
import socket

def fuzz_test(data):
    with paramiko.SSHClient() as ssh:
        try:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(data, timeout=0.5, username='user', password='pass')
        except paramiko.AuthenticationException as e:
            pass
        except socket.gaierror as e:
            pass

def main():
    atheris.Setup(sys.argv, fuzz_test)
    atheris.Fuzz()

if __name__ == "__main__":
    main()

# Including the exception handling for socket.gaierror to catch the 'Name or service not known' error
# Setting the missing host key policy to AutoAddPolicy to skip host key verification for the fuzzing tests.
