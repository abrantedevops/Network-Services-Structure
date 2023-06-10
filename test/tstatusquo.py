import subprocess
import sys

def stop_docker_container():
    containers = ["statusquo-apache"]
    for container in containers:
        subprocess.run(["docker", "stop", container])

def test_docker_web():
    containers = [
        {"name": "statusquo-apache"},
    ]
    print("========================================= APACHE =========================================")
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



# def remove_docker_container():
#     containers = ["statusquo-apache"]
#     for container in containers:
#         subprocess.run(["docker", "rm", container])


stop_docker_container()
test_docker_web()
# remove_docker_container()


