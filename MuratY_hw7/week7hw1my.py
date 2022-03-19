import re

pattern=re.compile(r'[a-zA-Z]{2}\d[a-zA-Z]{2}\d{2}[a-zA-Z]\d')
input_text="AABZA1111AEGTV5YH678MK4FM53B6"
matches=pattern.findall(input_text)
for match in matches:
    print(match)