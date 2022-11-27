import os
os.system("strings -n 40 capture.pcapng | grep -x '.\{40\}' > /home/mika/Desktop/pass.txt")
with open("/home/mika/Desktop/pass.txt", "r") as pass_list:
    passwords = []
    a = 0
    for line in pass_list:
        if a%2==0:
            passwords.append(line.replace("\n","")[26:40])
        a+=1
    pass_list.close()

with open("/home/mika/Desktop/wordlist.txt","w") as wordlist:
    for i in range(len(passwords)):
        wordlist.write(passwords[i]+"\n")