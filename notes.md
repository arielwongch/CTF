###CTF###

1. <website>/robots.txt

2. Python run linux command
"
import subprocess

with open("dictionary.txt") as file:
    password = file.read()

for pw in password:
    result = subprocess.run(["python", "level5.py"],input=pw,capture_output=True,text=True)
    print(result.stdout)
"




