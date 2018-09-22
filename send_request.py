#!/usr/bin/env python3
import sys
import requests

data = """
title ModuleQ full system use case diagram

!definelong userDoes(action, direction = "d")
User -direction-> (action)
!enddefinelong

!definelong userDoesAuth(parent, action)
(parent) <|-- (action)
userDoes(action, u)
!enddefinelong

!define LIf Log in from
!define LIftFTf Log in for the first time from


Actor User


rectangle auth {

usecase LogIn as "Log in
--return--
moduleq auth token"


usecase LoginFirst as "Log in for the first time
==
Create user
Create default account
Create OAuth token"

LogIn <|-- LoginFirst

userDoesAuth(LoginFirst, LIftFTf browser)
userDoesAuth(LoginFirst, LIftFTf teams as guest)
userDoesAuth(LoginFirst, LIftFTf teams as master)


usecase LoginAsUsual as "Login as usual
==
Update OAuth token
Update last seen date/time"

LogIn <|-- LoginAsUsual

userDoesAuth(LoginAsUsual, LIf browser)
userDoesAuth(LoginAsUsual, LIf Teams)

}

userDoes(Accept priority)
userDoes(Reject priority)
userDoes(Open priorities in browser)
userDoes(Open priorities in tab)
userDoes("Type 'help' in Teams")
userDoes(Type unknown command)
userDoes(Enter organization name in Teams)
"""

print(requests.post(sys.argv[1], data).text)
