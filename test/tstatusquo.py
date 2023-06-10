import subprocess
import time

def test_docker_web():
    containers = [
        {"name": "statusquo-apache"},
    ]
    for container in containers:
        print("========================================= APACHE =========================================")
        print()
        print("Instalada as dependências no container: " + "\033[91m"+container["name"]+"\033[0m")
        subprocess.run(["docker", "exec", container["name"], "/bin/sh", "-c", "apt install curl -y"])
        print()
        print("Iniciando o Teste das Requisições LAN e WAN")
        print()
        loading_text = "Carregando"
        for _ in range(5):
            print(loading_text, end="", flush=True)
            loading_text += "."
            time.sleep(0.5)  
            print("\r", end="") 
        print()
        print()
        print("Domínio (app01 - lan): http://app01.abranteme.com.br")
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "curl app01.abranteme.com.br"]
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
            print("\033[91mAttention! app01.abranteme.com.br with error.\033[0m")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print()
        print("Domínio (app02 - lan): http://app02.abranteme.com.br")
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "curl app02.abranteme.com.br"]
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
            print("\033[91mAttention! app02.abranteme.com.br with error.\033[0m")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print()
        print("Domínio (app02/jornal - lan): http://app02.abranteme.com.br/jornal")
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "curl app02.abranteme.com.br/jornal"]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        print()
        if result.returncode == 0:
            print("\033[92m+-+-+-+-+-+-+-+-+-+\033[0m")
            print("\033[92mFinished. No error\033[0m")  
            print("\033[92m+-+-+-+-+-+-+-+-+-+\033[0m")
            print()
        else:
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print("\033[91mAttention! app01.abranteme.com.br/jornal with error.\033[0m")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print()
        print("Domínio (app01 - wan): https://app01.abranteme.com.br")
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "curl -k https://app01.abranteme.com.br"]
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
            print("\033[91mAttention! app01.abranteme.com.br with error.\033[0m")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print()
        print("Domínio (app02 - wan): https://app02.abranteme.com.br")
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "curl -k https://app02.abranteme.com.br"]
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
            print("\033[91mAttention! app02.abranteme.com.br with error.\033[0m")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print()
        print("Domínio (app02/jornal - wan): https://app02.abranteme.com.br/jornal")
        command = ["docker", "exec", container["name"], "/bin/sh", "-c", "curl -k https://app02.abranteme.com.br/jornal"]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        print()
        if result.returncode == 0:
            print("\033[92m+-+-+-+-+-+-+-+-+-+\033[0m")
            print("\033[92mFinished. No error\033[0m")  
            print("\033[92m+-+-+-+-+-+-+-+-+-+\033[0m")
            print()
        else:
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print("\033[91mAttention! app01.abranteme.com.br/jornal with error.\033[0m")
            print("\033[91m+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\033[0m")
            print()

# def stop_docker_container():
#     containers = ["statusquo-apache"]
#     for container in containers:
#         subprocess.run(["docker", "stop", container])

# def remove_docker_container():
#     containers = ["statusquo-apache"]
#     for container in containers:
#         subprocess.run(["docker", "rm", container])



test_docker_web()
# stop_docker_container()
# remove_docker_container()


