#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import subprocess
import sys


# In[2]:


subprocess.call('clear', shell=True)


# In[3]:


sub = input('enter subdomain: ')


# In[4]:


#finding the IP address of the subdomain
try:
    subdomain_ip = socket.gethostbyname(sub)
    print('success')
except socket.gaierror:
    print('error')


# In[5]:


print(subdomain_ip)


# In[6]:


#defining the list, that later on will contain tuples of port and service
list_port_service = []


# In[ ]:


try:
    for port in range (1,65535):
        #checking progress
        if port % 50 == 0 :
            print(port)
        #checking if the port is open, if so - append it with the service it provides
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((subdomain_ip, port))
        if result == 0:
            port_service = socket.getservbyport(port, 'tcp')
            print('port: {}, service: {}'.format(port, port_service))
            list_port_service.append((port, port_service))
    sock.close()
#Handling possible errors
except KeyboardInterrupt:
    print ("you pressed ctrl+c")
    sys.exit()
except socket.gaierror:
    print ("subdomain could not be resolved")
    sys.exit()
except socket.error:
    print ("couldn't connect to server")
    sys.exit()


# In[8]:


print(list_port_service)

