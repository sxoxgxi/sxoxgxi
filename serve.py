import requests
import datetime
res = requests.get('https://zenquotes.io/api/quotes')
data = res.json()
quote = data[0]['q']
author = data[0]['a']

def linkify(query: str) -> str:
    return f"https://duckduckgo.com/?q={query.replace(' ', '+')}"

with open('README.md', 'r', encoding='utf-8') as readme:
    uwu = readme.read()

startblock = uwu.index("<h4 align='center'>")
endblock = uwu.index("</a>.</h4>")
content = f"<h4 align='center'>{quote} - <a href='{linkify(author)}' target='_blank'>{author}</a>.</h4>"

newcontent = uwu[:startblock] + content + uwu[endblock+len("</a>.</h4>"):]

with open("README.md", 'w', encoding='utf-8') as newreadme:
    newreadme.write(newcontent)
with open("log.txt", 'a', encoding='utf-8') as log:
    log.write(f"{quote} - {datetime.datetime.now()}\n")
