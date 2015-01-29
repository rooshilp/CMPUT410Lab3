#!/usr/bin/env python

import cgi 

form = cgi.FieldStorage()

val1 = form.getvalue('birthday')
val2 = form.getvalue('hobby')
val3 = form.getvalue('happy')

if val3 == "on":
    val3 = "happy"
else:
    val3 = "not happy"

print """Content-type: text/html

<!DOCTYPE html>
<head>
<title>Page 1</title>
</head>
<body>
<p> Your Birthday is %s. Your main hobby is %s. You are %s.</p>
<form method="post" action="page2.py">
What is your first name? <input name="first"/></br>
What is your last name? <input name="last"/></br>
Are you male or female? 
Male: <input name="gender" value="male" type="radio"/>
Female: <input name="gender" value="female" type="radio"/><br/>
<input type="submit" value="Submit">
</form>""" % (val1, val2, val3)   
    