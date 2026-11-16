*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  Salasana123
    Output Should Contain  New user registered
    

Register With Already Taken Username And Valid Password
    Create User  pekka  Salasana123
    Input Credentials  pekka  Salasana123
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  ab  Password123
    Output Should Contain  Invalid username

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle123  Password123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  kalle  short1
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  password
    Output Should Contain  Invalid password

