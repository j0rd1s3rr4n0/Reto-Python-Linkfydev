import base64, time, sys,subprocess, signal, shutil, os
i = 0
j = 0
decod = ""
found = False
print("\n")

def deleteall():
    l = 0
    try:
        while True:
            time.sleep(0.001)
            file = 'reto_'+str(l)+'.txt'
            os.remove(file)
            subprocess.call('del',file)
            l+=1
    except Exception as e:
        e = 'e'

    
def normal_to_generic():
    src="reto-230209-164119.txt"
    dst="reto_0.txt"
    shutil.copy(src,dst)
    print("\033[95m[>] COPIANDO CONTENIDO DE "+src+" a "+dst+"\n\033[0m")

def signal_handler(sig, frame):
    found = False
    print("\033[91m[-] OPERATION CANCELED BY USER\033[0m")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

deleteall()
normal_to_generic()
time.sleep(5)
total_files = 100
processed_files = 0

while True:
    try:
        #time.sleep(0.01)
        file = "reto_"+str(i)+".txt"
        print("\033[94m[*] READING FILE "+file+" ...\n\033[0m")
        with open(file, "rb") as file:
            encoded_data = file.read()
            decoded_data = base64.b64decode(encoded_data)
            decod = decoded_data
            file.close()
            j+=1
            file2 = "reto_"+str(j)+".txt"
            print("\033[92m[+] SAVING ON "+file2+" ...\n\033[0m")

        with open(file2, "wb") as file:
            file.write(decoded_data)
            file.close()
            i=j
        processed_files += 1
        print("\033[93m[>] CONTENT OF THE FILE: "+str(decod[:5].decode('utf-8'))+" Size: "+str(len(decod))+" Bytes\n\033[0m")
        file.close()

    except:
        #print("\033[91m[-] AN ERROR OCCURRED. EXITING ...\033[0m")
        found = True
        break
if found:
    long = 100
    separator = ("="*long)
    text = "DECRYPTED TEXT"
    sep_text = (" "*int(((long-len(text))/2)))
    header = f"\033[92m[*] DATA FOUND!\033[0m \033[95m\n\n{separator}\033[0m\n \033[92m{sep_text}{text}{sep_text}\033[0m \033[95m\n{separator}"
    content = decod.decode('utf-8')
    footer = f"\n{separator}\033[0m"
    print(header)
    print(content)
    print(footer)
    deleteall()