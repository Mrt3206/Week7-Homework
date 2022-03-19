import re

input_text="The advencements in biomarine studies franky@google.com \
with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."

pattern=re.compile(r'([a-zA-Z0-9.-]+)@[a-zA-Z0-9-]+\.(com|edu|net)')

matches=pattern.finditer(input_text)
for match in matches:
    print(match.group(1))