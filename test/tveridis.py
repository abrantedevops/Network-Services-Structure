import subprocess
import sys

def stop_docker_container():
    containers = ["veridis-bindm", "veridis-binds", "nginx-lan", "nginx-wan"]
    for container in containers:
        subprocess.run(["docker", "stop", container])

def test_docker_dns():
    containers = [
    {"name": "veridis-bindm"},
    {"name": "veridis-binds"}
]
    print("========================================= BIND9 =========================================")
    for container in containers:
        print()
        print("Verificando o container do Servidor DNS: " + container["name"])
        status = subprocess.run(["docker", "container", "inspect", container["name"], "--format", "{{.State.Status}}"], capture_output=True, text=True)
        print()
        print("Status: " + status.stdout.strip())
        print()
        if status.stdout.strip() == "running":
            print("\033[92m+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print("Finished. No error")
            print("\033[92m+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print()
        else:
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print("Attention! Bind9 with error.")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print()
            sys.exit(1)

def test_docker_nginx():
    containerslan = [
        {"name": "nginx-lan"},
    ]
    print("========================================= NGINX =========================================")
    for container in containerslan:
        print("Verificando o container do Servidor Proxy: " + container["name"])
        print()
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "service nginx status"]
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
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print("Attention! Nginx with error.")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print()
            sys.exit(1)
    
    containerswan = [
        {"name": "nginx-wan"},
    ]
    for container in containerswan:
        print("Verificando o container do Servidor Proxy: " + container["name"])
        print()
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "service nginx status"]
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
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print("Attention! Nginx with error.")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\033[0m")
            print()
            sys.exit(1)



# def remove_docker_container():
#     containers = ["veridis-bindm", "veridis-binds", "nginx-lan", "nginx-wan"]
#     for container in containers:
#         subprocess.run(["docker", "rm", container])


stop_docker_container()
test_docker_dns()
test_docker_nginx()
# remove_docker_container()


