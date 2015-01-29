#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

val1 = form.getvalue('first')
val2 = form.getvalue('last')
val3 = form.getvalue('gender')

print  """Content-type: text/html

    <!DOCTYPE html>
    <head>
    <title>Page 2</title>
    </head>
    <body>
    <p> Hello %s %s! You are a %s.</p>
    <form method="post" action="page1.py">
    When is your birthday? (DD/MM/YYYY) <input name="birthday"/></br>
    What is your main hobby? <input name="hobby"/></br>
    Are you happy? <input name="happy" type="checkbox"/><br/>
    <input type="submit" value="Submit">
    </form>""" % (val1, val2, val3) 