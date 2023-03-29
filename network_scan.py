import socket

print("FScan\n")

url= ''
ip_address = ''

def  isHostAlive(ip_address):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((ip_address,80))
    sock.close()
    return result

def nextDo(ip_address):
    permission = input("Do you want to scan the address(y:yes/n:no)")
    print("\n")
    if(permission=='y'):
        
        port_range = [20,21,22,23,25,53,139,137,445,80, 443, 8080,8443,1433,1434,3306,3389]
        # Loop over each port in the range and try to connect
        
        for port in port_range:
            service = ''
            banner = ''
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            result = s.connect_ex((ip_address, port))
            if result == 0:
            # The port is open, so try to get the banner
                try:
                    service = socket.getservbyport(port)
                except OSError:
                    service = "unknown"
                if(service!=''):        
                    print(f"Port {port} :{service}/open")    
            else:
                try:
                    service = socket.getservbyport(port)
                except OSError:
                    service = "unknown"      
                
                if(service!=''):        
                    print(f"Port {port} :{service}/closed")
                
            s.close()



while(True):
    print("1.Enter Domain Name\n2.Enter IP Address\n3.DNS Lookup\n4.Exit\n")
    n =int(input("Enter the option\n"))
    if(n==1):
        url =input("Enter a domain name\n")
        try:
            ip_address = socket.gethostbyname(url)
            print("ip address for" +url+" is=>"+ip_address)
            if(isHostAlive(ip_address)==0):
                print(ip_address+"is up!")
                nextDo(ip_address)
            elif(isHostAlive(ip_address)==1):
                print(ip_address+"is down!") 
                      
        except socket.gaierror:
            print("Unable to resolve ip, try entering ip address")
            
    elif(n==2):
        ip_address = input("Enter the ip address\n")
        nextDo(ip_address)
        
    elif(n==3):
        url = input("Enter the domain name\n")
        ip_address = socket.gethostbyname(url)
        print("IP address is\t:"+ip_address)
        
    elif(n==4):
        break       




