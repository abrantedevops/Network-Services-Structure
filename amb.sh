#!/bin/bash

instalar_virtualbox() {
  while true; do
    read -p "Deseja instalar o VirtualBox ? (S/n): " escolha
    escolha=$(echo $escolha | tr '[:upper:]' '[:lower:]')
    if [ "$escolha" = "s" ] || [ "$escolha" = "sim" ] || [ "$escolha" = "y" ] || [ "$escolha" = "yes" ]; then
      echo "Instalando o VirtualBox..."
      sudo apt update -y
      sudo apt install -y virtualbox virtualbox-ext-pack
      echo "VirtualBox instalado com sucesso!"
      break
    elif [ "$escolha" = "n" ] || [ "$escolha" = "não" ] || [ "$escolha" = "no" ] || [ "$escolha" = "nao" ]; then
      echo "Instalação do VirtualBox cancelada."
      break
    else
      echo "Opção inválida. Responda com 'S' ou 'N' para sim ou não."
    fi
  done
}

instalar_vagrant() {
  while true; do
    read -p "Deseja instalar o Vagrant ? (S/n): " escolha
    escolha=$(echo $escolha | tr '[:upper:]' '[:lower:]')
    if [ "$escolha" = "s" ] || [ "$escolha" = "sim" ] || [ "$escolha" = "y" ] || [ "$escolha" = "yes" ]; then
      echo "Instalando o Vagrant..."
      sudo apt update -y
      sudo apt install -y vagrant
      echo "Vagrant instalado com sucesso!"
      break
    elif [ "$escolha" = "n" ] || [ "$escolha" = "não" ] || [ "$escolha" = "no" ] || [ "$escolha" = "nao" ]; then
      echo "Instalação do Vagrant cancelada."
      break
    else
      echo "Opção inválida. Responda com 'S' ou 'N' para sim ou não."
    fi
  done
}

instalar_ansible() {
  while true; do
    read -p "Deseja instalar o Ansible ? (S/n): " escolha
    escolha=$(echo $escolha | tr '[:upper:]' '[:lower:]')
    if [ "$escolha" = "s" ] || [ "$escolha" = "sim" ] || [ "$escolha" = "y" ] || [ "$escolha" = "yes" ]; then
      echo "Instalando o Ansible..."
      sudo apt update -y
      sudo apt install -y ansible 
      sudo pip install --upgrande pip
      sudo pip install --upgrade ansible
      echo "Ansible instalado com sucesso!"
      break
    elif [ "$escolha" = "n" ] || [ "$escolha" = "não" ] || [ "$escolha" = "no" ] || [ "$escolha" = "nao" ]; then
      echo "Instalação do Ansible cancelada."
      break
    else
      echo "Opção inválida. Responda com 'S' ou 'N' para sim ou não."
    fi
  done
}

# Menu principal
echo "Instalação de Dependências!"
instalar_virtualbox
instalar_vagrant
instalar_ansible
echo "Processo Finalizado."
