*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  matti  salasana1!
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  matti  salasana1!
    Input New Command
    Input Credentials  matti  toinenpassu1!
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ab  salasana1!
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  ab1  salasana1!
    Output Should Contain  Username must contain only lowercase letters

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  pekka  short1
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  liisa  salasanx
    Output Should Contain  Password must contain at least one non-letter
