*** Settings ***
Documentation     Teste de Login em app02.abranteme.com.br/jornal
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Chrome
${URL}            http://app02.abranteme.com.br/jornal
${USERNAME}       abranteme
${PASSWORD}       abranteme

*** Test Cases ***
Verificação em Andamento
    Open Browser    ${URL}    ${BROWSER}
    Input Text      //input[@name='my_username']    ${USERNAME}
    Input Text      //input[@name='my_password']     ${PASSWORD}
    Click Button    //input[@name='my_login']
    Sleep           5s
    Page Should Contain    Index of /jornal
    Close Browser
