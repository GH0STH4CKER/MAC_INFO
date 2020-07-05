import requests , socket , time
from colorama import Fore , init
init()
print(Fore.CYAN + "")
b1 = " ███╗░░░███╗░█████╗░░█████╗░  ██╗███╗░░██╗███████╗░█████╗░ \n"
b2 = " ████╗░████║██╔══██╗██╔══██╗  ██║████╗░██║██╔════╝██╔══██╗ \n"
b3 = " ██╔████╔██║███████║██║░░╚═╝  ██║██╔██╗██║█████╗░░██║░░██║ \n"
b4 = " ██║╚██╔╝██║██╔══██║██║░░██╗  ██║██║╚████║██╔══╝░░██║░░██║ \n"
b5 = " ██║░╚═╝░██║██║░░██║╚█████╔╝  ██║██║░╚███║██║░░░░░╚█████╔╝ \n"
b6 = " ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░  ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░ \n"
credit = "------------ [+] Tool by GHOSTH4CK3R ----------------\n"

banner = b1 + b2 + b3 + b4 + b5 + b6
print(banner,Fore.LIGHTCYAN_EX +"",credit)

try: 
    ip = socket.gethostbyname("www.google.com")
    print(Fore.LIGHTGREEN_EX + "# Internet : Active")    
except Exception as e:
    
    print(Fore.LIGHTRED_EX + "  !!No Internet !! \nExitting in 10 seconds")  
    time.sleep(10)
    exit()

url = "https://macvendors.co/api/"
print(Fore.LIGHTBLUE_EX + "")
mac = input("Enter mac address : ")
url = (url+mac+"/pipe")

response = requests.get(url)
s_code = response.status_code

if s_code == 200 :   
  data = response.text
  data = data.replace("|","\n")
  data = data.replace(f'"',"")

  data = data.splitlines()

  print(Fore.LIGHTCYAN_EX +"")
  print("Company    :",data[0])
  print("Mac Prefix :",data[1])
  print("Address    :",data[2])
  print("Start Hex  :",data[3])
  print("End Hex    :",data[4])
  print("Country    :",data[5])
  print("Type       :",data[6])

else:
    print(Fore.LIGHTRED_EX + "Connection Error !")
    print("Status Code ",s_code)

print(Fore.LIGHTGREEN_EX + "")
input("Exit >")


