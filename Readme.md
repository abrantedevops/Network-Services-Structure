<h1>Mãos à obra: Provisionando sistemas e serviços com Vagrant, Ansible e Docker</h1>

<p align="center" style="display: flex; justify-content: center;">
  <a href="https://www.vagrantup.com/downloads" target="_blank" style="margin-right: 0.5rem;">
    <img src="https://img.shields.io/badge/Vagrant-1868F2?style=for-the-badge&logo=Vagrant&logoColor=white" alt="Vagrant version" style="max-width:100%;">
  </a>

  <a href="https://www.ansible.com/" target="_blank" style="margin-right: 0.5rem;">
    <img src="https://img.shields.io/badge/Ansible-000000?style=for-the-badge&logo=ansible&logoColor=white" alt="Ansible version" style="max-width:100%;">
  </a>

  <a href="https://www.docker.com/" target="_blank" style="margin-right: 0.5rem;">
    <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" alt="Docker version" style="max-width:100%;">
  </a>
</p>

<p align="center">

<img alt="Repository size" src="https://img.shields.io/github/repo-size/abrantedevops/Network-Services-Structure">

<img  alt="made by" src="https://img.shields.io/badge/made%20by-Abrante%20DevOps-blueviolet">

</p>


<p align="center"><img src="./img/bellsoft-s-docker-hub-images-overview.webp" alt="Scope" style="max-width:100%"></p>

<p align="justify">Infraestrutura como código (IaC) é uma prática de desenvolvimento de software que se enquadra na abordagem DevOps. Ela envolve a automação e gerenciamento da infraestrutura de um sistema de computador usando código, assim, as tecnologias empregadas neste tutorial, em conjunto o Vagrant, o Ansible e o Docker fornecem uma poderosa combinação de ferramentas para a criação, provisionamento e implantação de infraestrutura e aplicativos como código. Eles permitem definir, compartilhar e gerenciar toda a pilha de infraestrutura, desde a configuração do sistema até a execução de aplicativos, de forma automatizada e escalável.</p>

<h2>Escopo</h2>

<p align="justify">A base deste tutorial consiste basicamente no provisionamento de servidores Linux bem como algumas configurações de gerenciamento de disco, hardening Linux, BIND9, Nginx e Apache. A seguir, temos uma imagem que ilustra a arquitetura do cenário proposto.</p>

<p align="center"><img src="./img/scope.drawio.png" alt="Scope" style="max-width:100%"></p>

<p align="justify">Comentando com mais detalhes, temos: <br>
- Instalação e configuração realizadas no Virtual Box, utilização do sistema Debian versão 11 bullseye64, adição de 3 HDs de 10GB para o gerenciamento de disco no Server-Veridis, adição de 2 interfaces de rede para o Server-Veridis e Server-Statusquo.
</p>

<p align="justify">
- O gerenciamento de disco compreendeu o uso de 3 discos para redundância completa dos dados, onde no Server-Veridis foram criadas as seguintes partições:
/dados/www (Tipo ext4, 2 Gbits)
/dados/jornal (Tipo ext4, 3 Gbits)
Em seguida, foram criados RAID para cada partição. Por fim, foi criado um LVM para cada RAID, sendo para /dados/www e /dados/jornal.
</p>

<p align="justify">
- Com relação aos Requisitos de Rede foi feita a configuração dos 3 primeiros endereços IPs da 2ª subrede de 8 IPs da faixa 200.200.200.32/27 para a inteface WAN. Para a interface LAN foi utilizada a rede 10.0.128.0/23.
</p>

<p align="justify">
- No Server-Veridis, para a segurança de Acesso ao Sistema foram implementados os procedimentos de: Acesso remoto permitido somente por meio de chaves de criptografia assimétrica, Restrição de acesso local para o usuário root, Acesso local permitido apenas para o usuário suporte, Configuração do tempo de inatividade para realizar logout automático após 5 minutos de inatividade, Acesso de super usuário deve ser realizado com o comando sudo.
</p>

<p align="justify">
- Para o Serviço DNS foi configurado o serviço de DNS primário para responder pelo domínio abranteme.com.br. Foram definidos os seguintes requisitos: TTL máximo padrão dos registros: 24h, fácil identificação da última alteração no arquivo de zona, verificação de alterações no servidor primário a cada 1 hora pelo servidor secundário (slave), configuração de 2 views: View Externa: Atendimento de requisições de DNS apenas da interface WAN, registros: DNS Primário (ns01.abranteme.com.br), DNS Secundário (ns02.abranteme.com.br), Portal WEB (www.abranteme.com.br), Aplicação 01 (app01.abranteme.com.br) e Aplicação 02 (app02.abranteme.com.br). Na View Interna: Atendimento de requisições apenas da LAN, permitir uso como servidor recursivo, registros: DNS Primário (ns01.abranteme.com.br), Portal WEB (www.abranteme.com.br), Aplicação 01 (app01.abranteme.com.br) e Aplicação 02 (app02.abranteme.com.br).
</p>

<p align="justify">
- Para o Serviço WEB foi utilizado no Server-Veridis o Nginx como Proxy WEB e Load Balancer para os serviços. A comunicação entre cliente e Nginx (Internet - Interface WAN) obrigatoriamente via HTTPS, e entre Nginx e Apache apenas HTTP. A configuração do Apache (Server-Statusquo) foi realizada com os seguintes requisitos: Atendimento de requisições na porta 8000, Impedimento de listagem de conteúdo de diretórios pelo acesso WEB, Não permitir criação de links simbólicos, Configuração de 2 virtual hosts: app01.abranteme.com.br: Diretório do site: /dados/www/app01, Adição de arquivo index.html para testes do "App01", app02.abranteme.com.br: Diretório do site: /dados/www/app02, Adição de arquivo index.html para testes do "App02", Acesso com autenticação do usuário "jornalista" ao diretório para obtenção dos arquivos postados, Leitura do conteúdo do diretório do serviço SFTP (/dados/jornal) pelo Apache.
</p>

<p align="justify">
- Ao acessar app02.abranteme.com.br/jornal, com usuário e senha "abranteme"  é possível ter acesso aos arquivos de log de teste da autenticação do usuário. Esse diretório está localizado no container statusquo-apache em /dados/www/app02/jornal, enquanto que os arquivos de logs estão sendo compartilhados a partir de um volume criado via docker-compose na VM Server-statusquo no diretórior /home/vagrant/reports
</p>

<p align="justify">
- Para o Serviço SFTP foi configurado o servidor OpenSSH para atender requisições SFTP na porta 22, com os seguintes requisitos: Criação de usuário "jornalista" com acesso ao diretório /dados/jornal.
</p>


<h2>Gerenciando o Cenário</h2>
<p align="justify">
A estrutura do tutorial envolvendo o Vagrant e o Ansible e o Docker está ilustrada na imagem abaixo. Foram configurados três máquinas virtuais a partir do arquivo vagrantfile, sendo elas: Server-Veridis, Server-Statusquo e Client-Host. Em seguida, para cada uma das máquinas virtuais o ansible é inicializado a partir dos arquivos de configuração playbook.yml, que por sua vez envia o arquivo docker-compose.yml para dentro de cada uma das VMs. Por fim, para as VMs Server-Veridis e Server-Statusquo o docker é utilizado para a criação de containers dos serviços de DNS, Nginx e Apache a partir das imagens que foram anteriormente criadas mediante modificação de acordo com as necessidades para atender os requisitos do tutorial. A VM do Cliente-Host é utilizada para testar a parte do acesso remoto ao servidor Veridis, bem como o serviço de SFTP.
</p>

<p align="center"><img src="./img/devops_drawio.png" alt="Scope" style="max-width:100%"></p>

<h2>Pipeline CI/CD</h2>

<p align="justify">
Para a criação do pipeline CI/CD foi utilizado o GitHub Actions, que é uma ferramenta de integração e entrega contínua incorporado ao GitHub. A branch "dev" foi configurada para ser a branch de teste, onde a build das imagens Docker (CI) são realizadas e encaminhadas ao registry (CD). A pipeline foi configurada para executar as seguintes etapas:
</p>

- Build das imagens Docker: É responsável por construir a imagem docker do servodpr DNS Primário e Secundário, do servidor proxy Nginx para requisições LAN e WAN e por fim do servidor web Apache que contém os virtual hosts para os serviços app01 e app02.

- Testes dos Serviços: São realizados com o auxílio de scripts que verificam se os serviços do BIND9, Nginx e Apache estão ativos e respondendo corretamente através dos containers criados a partir das imagens Docker da etapa anterior.

- Vulnerabilidades: Após os testes é iniciado a análise de vulnerabilidades com o auxílio da ferramenta Trivy, que é um scanner de código aberto para imagens e artefatos de contêiner.

- Push: Após a conclusão das etapas anteriores, as imagens são encaminhadas ao registry Dockerhub para que possam ser baixadas e utilizadas no tutorial.


<h3>Deployment</h3>
<p align="justify">
Após o push das imagens para o registry, é necessário de um processo para automatizar as atualizações dos containers que estão em execução nas VMs. Para isso, foi utilizado o serviço Watch Tower, que irá baixar a nova imagem, remover o container antigo e iniciar um novo container com as mesmas opções que foram usadas inicialmente. O Watch Tower é executado a partir dos arquivos docker-compose, que estão configurados para monitorar em um intervalo de 5 minutos, caso seja identificado uma nova versão o Watch Tower irá baixar a nova imagem e reiniciar o container. Com isso, finalizamos o pipeline de CI/CD com integração, entrega e deploy contínuo. A imagem abaixo ilustra todo esse processo.
</p>

<p align="center"><img src="./img/pipelinections.png" alt="Scope" style="max-width:100%"></p>


<h2>Ambiente do Tutorial</h2>

- É necessário que o provider de virtualização, o Vagrant e o Ansible estejam instalados na máquina real. Para isso siga as instruções de instalação, que pode ser encontrado aqui: <a href="https://www.virtualbox.org/wiki/Downloads" target="_blank">VirtualBox</a>,
<a href="https://developer.hashicorp.com/vagrant/downloads" target="_blank">Vagrant</a>,
<a href="https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html" target="_blank">Ansible</a>

- O ambiente foi provisionado e testado a partir das seguintes versões: Sistema operacional Ubuntu 20.04.6 LTS (Focal Fossa), VirtualBox 6.1.26, Vagrant 2.3.4 e Ansible 2.12.10.

<p align="justify">
<b style="color:red;">Importante:</b> Caso opte por usar outra distribuição Linux, esteja seguro que conhece bem o gerenciador de pacotes, sistema de arquivos e comandos que sejam necessários para resolver eventuais imprevistos que possam ocorrer na sua opção GNU/Linux, você será responsável pelo troubleshooting da distribuição que escolher. Se você não está totalmente seguro, sinta-se a vontade para baixar e utilizar a VM já configurada e testadas acessando aqui: <a href="https://archive.org/details/ubuntu-nss" target="_blank">VM DevOps</a>
</p>

<h2>Pré-requisitos e Indicações</h2>

- Antes de começar, certifique-se de adicionar no arquivo hosts da máquina real a seguinte linha de configuração:
```bash
192.168.57.7	www.abranteme.com.br	www.app01.abranteme.com.br	app01.abranteme.com.br	www.app02.abranteme.com.br  app02.abranteme.com.br
```

- Os serviços podem ser inicializados a partir do comando abaixo:


```bash
# Clone este repositório
$ git clone https://github.com/abrantedevops/Network-Services-Structure.git

# Acesse a pasta no terminal/cmd em que está o arquivo Vagrantfile
$ cd detools

# Para criar todas as máquinas virtuais e executar o tutorial
$ vagrant up

# Após a finalização do processo, basta acessar os endereços abaixo com http ou https para testar os serviços:
www.abranteme.com.br
app01.abranteme.com.br
app02.abranteme.com.br
app02.abranteme.com.br/jornal


# Para acessar o servidor Veridis, Statusquo ou Client-Host a partir da máquina real, utilize os seguintes comandos:
$ vagrant ssh veridis
$ vagrant ssh statusquo
$ vagrant ssh client

# Para o acesso remoto ao servidor Veridis foi criado um par de chaves de criptografia assimétrica, logo de dentro da VM Client-Host alterne para o usuário suporte e acesse o servidor Veridis com o comando abaixo:
$ su suporte
$ passord: 1234
$ ssh suporte@10.0.128.1

# Do mesmo modo, para testar o serviço SFTP, pode ser utilizado o comando abaixo a partir da VM Client-Host:
$ su jornalista
$ password: 1234
$ sftp jornalista@10.0.128.1

# Caso queira criar apenas uma das máquinas virtuais:
$ vagrant up veridis
$ vagrant up statusquo
$ vagrant up client

# Atenção: Como em toda execução do Vagrantfile são criados discos rígidos virtuais (destinados ao gerenciamento de disco) na VM Veridis, caso queira levantar novamente as VMs, é necessário executar o comando abaixo para não dar erro de disco já existente:
$ vagrant destroy -f
```

<h2>Referências</h2>

- <a href="https://www.virtualbox.org/" target="_blank">VirtualBox</a>
- <a href="https://www.vagrantup.com/" target="_blank">Vagrant</a>
- <a href="https://www.ansible.com/" target="_blank">Ansible</a>
- <a href="https://www.docker.com/" target="_blank">Docker</a>
- <a href="https://docs.docker.com/compose/" target="_blank">Docker Compose</a>
- <a href="https://hub.docker.com/r/abrantedevops/network_services_structure" target="_blank">Repositório Docker Hub</a>
- <a href="https://www.nginx.com/" target="_blank">Nginx</a>
- <a href="https://httpd.apache.org/" target="_blank">Apache</a>
- <a href="https://www.isc.org/bind/" target="_blank">Bind9</a>
- <a href="https://bell-sw.com/blog/bellsoft-s-docker-hub-images-overview/" target="_blank">Visão Geral das Imagens</a>
- <a href="https://trivy.dev/" target="_blank">Trivy</a>
- <a href="https://github.com/features/actions" target="_blank">GitHub Actions</a>
- <a href="https://robotframework.org/" target="_blank">Robot Framework</a>
- <a href="https://containrrr.dev/watchtower/" target="_blank">Watchtower</a>


<h2>Licença</h2>

MIT License

Copyright (c) 2012-2024 Thiago Abrante de Souza

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

<h1>Contato</h1>


- [Thiago A. Souza](mailto:thiago.souza@see.pb.gov.br)


















