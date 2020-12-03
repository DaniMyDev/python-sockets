#import modules
import socket
import subprocess
import os


#socket config and ip fetch
port = 2000
ip = socket.gethostbyname(socket.gethostname())
address = (ip, port)


#communication settings
header = 64
msg_format = 'utf-8'
msg_disconnect = '!disconnect'


#create client socket and connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
print('client connected succesfully')


def build_array(string):
  return string.split('\n')


def create_file():
  program_array = build_array(program_str)
  f = open('program_temp.py','w+')
  for line in program_array:
    f.write(line+'\n')
  f.close()


#variables
connected = True
program_str = ''
resource = None


while connected:

  #recieve header and msg type
  length = int(client.recv(header).decode(msg_format))
  msg_type = client.recv(length).decode(msg_format)
  client.send('ok'.encode(msg_format))

  #protocol
  if msg_type == 'program':
    length = int(client.recv(header).decode(msg_format))
    program_str = client.recv(length).decode(msg_format)
    client.send('ok'.encode(msg_format))
  
  if msg_type == 'resource':
    length = int(client.recv(header).decode(msg_format))
    resource = client.recv(length)
    client.send('ok'.encode(msg_format))

  if msg_type == 'run program':
    #create temp image
    tmp_image = open('test_tmp.jpg','wb')
    tmp_image.write(resource)
    tmp_image.close()
    #create python file
    create_file()
    #run subprocess and acces output(stdout)
    process = subprocess.Popen(['python', 'program_temp.py'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    resized_tmp = open('img_resized.jpg','rb').read()
    #read resized image
    client.send(str(len(resized_tmp)).encode(msg_format))
    client.send(resized_tmp)
    os.remove('img_resized.jpg')

  if msg_type == msg_disconnect:
    connected = False
    client.send(msg_disconnect.encode(msg_format))
    client.close()
    break