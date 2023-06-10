import subprocess

def test_docker_dns():
    containers = [
        {"name": "veridis-bindm"},
        {"name": "veridis-binds"}
    ]
    for container in containers:
        print("========================================= BIND9 =========================================")
        print()
        print("Instalada as dependências no container: " + "\033[91m"+container["name"]+"\033[0m")
        subprocess.run(["docker", "exec", container["name"], "/bin/sh", "-c", "apt install dnsutils -y"])
        print("Verificando o container do Servidor DNS: " + "\033[91m"+container["name"]+"\033[0m")
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "nslookup app01.abranteme.com.br"]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        print()
        if result.returncode == 0:
            print("\033[92m+-+-+-+-+-+-+-+-+-+\033[0m")
            print("\033[92mFinished. No error\033[0m")  
            print("\033[92m+-+-+-+-+-+-+-+-+-+\033[0m")
            print()
        else:
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print("\033[91mAttention! BIND9 with error.\033[0m")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print()
# IMPLEMENTAR OS LOGS DO BIND(9)

def test_docker_nginx():
    containerslan = [
        {"name": "nginx-lan"},
    ]
    for container in containerslan:
        print("========================================= NGINX =========================================")
        print("Verificando o container do Servidor Proxy: " + "\033[91m"+container["name"]+"\033[0m")
        print()
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "service nginx status"]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        print()
        if result.returncode == 0:
            print("\033[92m+-+-+-+-+-+-+-+-+-+\033[0m")
            print("\033[92mFinished. No error\033[0m")  
            print("\033[92m+-+-+-+-+-+-+-+-+-+\033[0m")
            print()
        else:
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print("\033[91mAttention! Nginx with error.\033[0m")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print()
    
    containerswan = [
        {"name": "nginx-wan"},
    ]
    for container in containerswan:
        print("Verificando o container do Servidor Proxy: " + "\033[91m"+container["name"]+"\033[0m")
        print()
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "service nginx status"]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        print()
        if result.returncode == 0:
            print("\033[92m+-+-+-+-+-+-+-+-+-+\033[0m")
            print("\033[92mFinished. No error\033[0m")  
            print("\033[92m+-+-+-+-+-+-+-+-+-+\033[0m")
            print()
        else:
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print("\033[91mAttention! Nginx with error.\033[0m")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print()

# def stop_docker_container():
#     containers = ["veridis-bindm", "veridis-binds", "nginx-lan", "nginx-wan"]
#     for container in containers:
#         subprocess.run(["docker", "stop", container])

# def remove_docker_container():
#     containers = ["veridis-bindm", "veridis-binds", "nginx-lan", "nginx-wan"]
#     for container in containers:
#         subprocess.run(["docker", "rm", container])


test_docker_dns()
test_docker_nginx()
# stop_docker_container()
# remove_docker_container()
