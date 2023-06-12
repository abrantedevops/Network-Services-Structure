*** Settings ***
Documentation     Testes de login na página
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Chrome
${URL}            http://app02.abranteme.com.br/jornal/
${USERNAME}       abranteme
${PASSWORD}       abranteme

*** Test Cases ***
Login na Página
    Abrir Navegador
    Manipular Janela de Login
    Verificar Login com Sucesso
    Verificar Página Inicial

*** Keywords ***
Abrir Navegador
    Open Browser    ${URL}    ${BROWSER}

Manipular Janela de Login
    # Capturar o alerta de login
    ${alert_text}    Execute JavaScript    alert('Fazer login\\nhttp://app02.abranteme.com.br\\nSua conexão a este site não é particular\\nNome de usuario\\nSenha\\nCancelar Fazer login')
    # Aceitar o alerta
    Handle Alert    ACCEPT
    # Preencher as credenciais de login
    Input Text    id=username    ${USERNAME}
    Input Password    id=password    ${PASSWORD}
    Click Button    id=entrar

Verificar Login com Sucesso
    Wait Until Page Contains    Bem-vindo, ${USERNAME}
    Log    Login realizado com sucesso

Verificar Página Inicial
    Page Should Contain    Index of /jornal
    Log    Página inicial exibida com sucesso
