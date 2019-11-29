# Python Program to Get IP Address 
import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)
print("find your ip address with ip finder made by http.zygote")
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)
