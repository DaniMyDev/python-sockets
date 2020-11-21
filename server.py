#import libraries
import socket
import threading

#server config and ip fetch
port = 2000
ip = socket.gethostbyname(socket.gethostname())
address = (ip, port)

#communication settings
header = 64
msg_format = 'utf-8'
msg_disconnect = '!disconnect'

#create socket instance and establish a connection
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)
print('server succesfully created')

#define in start function
#this is bind to the client socket
#in particular
def handle_client(conn, addr):

  print(f"{addr} connected")
  connected = True

  while connected:

    #send header and msg type
    conn.send(str(len('program')).encode(msg_format))
    conn.send('program'.encode(msg_format))
    res = conn.recv(header).decode(msg_format)
    if res == 'not ok':
      return False

    #send the program
    conn.send(str(len(program_str)).encode(msg_format))
    conn.send(program_str.encode(msg_format))
    res = conn.recv(header).decode(msg_format)
    if res == 'not ok':
      return False

    #send header and msg type
    conn.send(str(len('resource')).encode(msg_format))
    conn.send('resource'.encode(msg_format))
    res = conn.recv(header).decode(msg_format)
    if res == 'not ok':
      return False

    #send img size and img bytes
    conn.send(str(len(img_b)).encode(msg_format))
    conn.send(img_b)
    res = conn.recv(header).decode(msg_format)
    if res == 'not ok':
      return False

    #send header and msg type
    conn.send(str(len('run program')).encode(msg_format))
    conn.send('run program'.encode(msg_format))
    res = conn.recv(header)
    if res == 'not ok':
      return False

    #get response
    res_length = int(conn.recv(header).decode(msg_format))
    res = conn.recv(res_length)
    f = open('response.jpg','wb')
    f.write(res)

    f.close()

    #send disconnected
    conn.send(str(len(msg_disconnect)).encode(msg_format))
    conn.send(msg_disconnect.encode(msg_format))
    res = conn.recv(header).decode(msg_format)

    if res == msg_disconnect:
      connected = False
      conn.close()
  

def start():
  server.listen()
  print(f"server is listening on {ip}")
  while True:
    # wait for a new connection and
    # store the result and create thread
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"active connections: {threading.activeCount() - 1}")
  pass

#we want to concatenate a string with the lines on 
#the txt file that contains the program.
program_str = ''
with open('program.txt') as txt:
  for line in txt:
    program_str += line

#get then image data encoded
img = open('test.jpg','rb')
img_b = img.read()
img.close()


print ('server is starting...')
start()