import requests
import datetime

url = 'https://zenquotes.io/api/quotes'
response = requests.get(url)

try:
    data = response.json()
    quote = data[0]['q']
    author = data[0]['a']
except (requests.exceptions.RequestException, ValueError, KeyError) as uwu:
    quote = "Error while fetching quote."
    author = f"{uwu}"


def linkify(query: str) -> str:
    return f"https://duckduckgo.com/?q={query.replace(' ', '+')}"


with open('README.md', 'r', encoding='utf-8') as readme:
    content = readme.read()

startblock = content.index("<h4 align='center'>")
endblock = content.index("</a>.</h4>")
new_content = f"<h4 align='center'>{quote} - <a href='{linkify(author)}' target='_blank'>{author}</a>.</h4>"

new_content = content[:startblock] + new_content + \
    content[endblock+len("</a>.</h4>"):]

with open("README.md", 'w', encoding='utf-8') as newreadme, \
        open("log.txt", 'a', encoding='utf-8') as log:
    newreadme.write(new_content)
    log.write(f"{quote} - {datetime.datetime.now()}\n")
