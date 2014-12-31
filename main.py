import webbrowser as wb

USER_ID = "hideo54" #<-Input Your Username

fmt = 'https://twitter.com/search?q=from%3A{id}%20since%3A2014-{month}-1%20until%3A2014-{month}-{end}&src=typd'
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(12):
    wb.open(fmt.format(id=USER_ID, month=i+1, end=days[i]))
