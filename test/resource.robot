*** Settings ***
Documentation     Testes de login na página
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Chrome
${URL}            http://www.testyou.in/Login.aspx
${USERNAME}       abranteme
${PASSWORD}       abranteme

*** Test Cases ***
Login com sucesso
    Open Browser    ${URL}    ${BROWSER}
    Input Text      //input[@name='ctl00$CPHContainer$txtUserLogin']    ${USERNAME}
    Input Text      //input[@name='ctl00$CPHContainer$txtPassword']     ${PASSWORD}
    Click Button    //input[@name='ctl00$CPHContainer$btnLoginn']
    Sleep           5s
    Close Browser

Login com falha
    Open Browser    ${URL}    ${BROWSER}
    Input Text      //input[@name='ctl00$CPHContainer$txtUserLogin']    ${USERNAME}
    Input Text      //input[@name='ctl00$CPHContainer$txtPassword']     ${PASSWORD}
    Click Button    //input[@name='ctl00$CPHContainer$btnLoginn']
    Sleep           5s
    Close Browser

