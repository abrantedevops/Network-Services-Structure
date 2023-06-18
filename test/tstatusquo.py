import subprocess
import sys
import time

print("========================================= APACHE =========================================")
print()
data = time.strftime("%d/%m/%Y %H:%M:%S")
print("Log: " + data)

def test_docker_web():
    containers = [
        {"name": "statusquo-apache"},
    ]
    for container in containers:
        print()
        print("Verificando o container do Servidor Web: " + container["name"])
        print()
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "service apache2 status"]
        result = subprocess.run(command, capture_output=True, text=True)
        print()
        if result.returncode == 0:
            print ("Status: running")
            print()
            print("\033[92m+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print("Finished. No error")  
            print("\033[92m+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print()
        else:
            print ("Status: exited")
            print()
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print("Attention! Apache with error.")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print()
            sys.exit(1)



test_docker_web()


