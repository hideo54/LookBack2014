import webbrowser as wb
import time

USER_ID = "hideo54" #<-Input Your Username
HUMANITY = True #<-If you think your tweet may be too many, set "False"

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if HUMANITY:
    fmt = 'https://twitter.com/search?q=from%3A{id}%20since%3A2014-{month}-1%20until%3A2014-{month}-{end}&src=typd'
    for i in range(12):
        wb.open(fmt.format(id=USER_ID, month=i+1, end=days[i]))
else:
    fmt1 = 'https://twitter.com/search?q=from%3A{id}%20since%3A2014-{month}-1%20until%3A2014-{month}-15&src=typd'
    fmt2 = 'https://twitter.com/search?q=from%3A{id}%20since%3A2014-{month}-16%20until%3A2014-{month}-{end}&src=typd'
    for i in range(12):
        wb.open(fmt1.format(id=USER_ID, month=i+1))
        wb.open(fmt2.format(id=USER_ID, month=i+1, end=days[i]))
