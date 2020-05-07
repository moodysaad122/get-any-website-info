import os,socket,requests,platform

def logo():
    

    print("""                                                           \033|
               ,
               |'.             ,
               |  '-._        / )
             .'  .._  ',     /_'-,
            '   /  _'.'_\   /._)')
           :   /  '_' '_'  /  _.'
           |E |   |Q| |Q| /   /
          .'  _\  '-' '-'    /
        .'--.(S     ,__` )  /
              '-.     _.'  /
            __.--'----(   /
        _.-'     :   __\ /
       (      __.' :'  :Y
        '.   '._,  :   :|
          '.     ) :.__:|
            \    \______/
             '._L/_H____]
    hack developer: moe saad
    instagram:mohammedsaad1215
    \033""")
    print()

def menu():
    print("""
\033 1)\033 Whois Lookup   \033 8)\033 HTTP Heade        
\033 2)\033 DNS Lookup \033     9)\033 Host Finder
\033 3)\033 GeoIP Lookup   \03310)\033 IP-Locator   
\033 4)\033 Subnet Lookup  \03311)\033 Find Shared DNS  
\033 5)\033 Port Scanner   \03312)\033 Get Robots.txt   
\033 6)\033 Page Links     \03313)\033 Host DNS Finder
\033 7)\033 Zone Transfer  \03314)\033 Exit                
          """)
    print()

def GATHETOOL():

      
    try:
        
        if 1 > 2 :
              print("buffer")
        else:
            opciones()

            
    except socket.gaierror:
        GATHETOOL()
    except UnboundLocalError:
        GATHETOOL()
    except requests.exceptions.ConnectionError:
        exit
    except IndexError:
        print('?')
        GATHETOOL()



def opciones():
        logo()
        website = input('\033 Website : \033')
        
        
        menu()
        
        valorselec = input('Option: \033')   

       
		   
        if valorselec == '1':
            whois = 'https://api.hackertarget.com/whois/?q='+website
            info = requests.get(whois)
            print('\033')
            print(info.text)            
            opciones()


        elif valorselec == '2':
            dnslook = 'https://api.hackertarget.com/dnslookup/?q='+website
            info = requests.get(dnslook)
            print('\033')
            print(info.text)
            opciones()

        elif valorselec == '3':
            ipgeo = 'https://api.hackertarget.com/geoip/?q='+website
            info = requests.get(ipgeo)
            print('\033')
            print(info.text)
            opciones()

        elif valorselec == '4':
            subnet = 'http://api.hackertarget.com/subnetcalc/?q='+website
            info = requests.get(subnet)
            print('\033')
            print(info.text)
            opciones()

        elif valorselec == '5':
            port = 'https://api.hackertarget.com/nmap/?q='+website
            info = requests.get(port)
            print('\033')
            print(info.text)
            opciones()

        elif valorselec == '6':
            pagelink = 'https://api.hackertarget.com/pagelinks/?q='+website
            info = requests.get(pagelink)
            print('\033')
            print(info.text)
            opciones()

        elif valorselec == '7':
            zone = 'https://api.hackertarget.com/zonetransfer/?q='+website
            info = requests.get(zone)
            print('\033')
            print(info.text)
            opciones()

        elif valorselec == '8':
            header = "https://api.hackertarget.com/httpheaders/?q="+website
            info = requests.get(header)
            print('\033')
            print(info.text)
            opciones()

        elif valorselec == '9':
            host = "https://api.hackertarget.com/hostsearch/?q="+website
            info = requests.get(host)
            print('\033')
            print(info.text)
            opciones()

        elif valorselec == '10':
            website = socket.gethostbyname(website)
            iplt = 'https://ipinfo.io/'+website+'/json'
            info = requests.get(iplt)
            print('\033')
            print(info.text)
            opciones()

        elif valorselec == '11':
           
            shared = 'https://api.hackertarget.com/findshareddns/?q='+website
            info = requests.get(shared)
            print('\033')
            print(info.text)
            opciones()

        elif valorselec == '12':
            robots ='http://'+website+'/robots.txt'
            info = requests.get(robots)
            print('\033')
            print(info.text)
            opciones()

        elif valorselec == '13':
            hostdns = 'https://api.hackertarget.com/mtr/?q='+website
            info = requests.get(hostdns)
            print('\033')
            print(info.text)
            opciones()



        elif valorselec == '14':
            exit

        else:
           
            GATHETOOL()
GATHETOOL()
