# python-sockets

## Objetive
Underestanding how to setup a server-client socket communication from scratch and try to use this to send a program to be executed on multiple sockets at the same time (slaves); This was very challenging because It needs an implementation of at least a simple protocol of comunication that can control the process, the program that is going to be sended is an image compressor made with pillow module.

## Usage
You need to have python installed and running on your machine, for this example I am using PIL module, so you have to installed it to use this program. Here is how to install it.
```bash
pip install pillow
```

Once you have all the setup, run the server.py and then run 3 times the client.py

```bash
python server.py
python client.py
```

## Cheking the result
You will have 3 Images as a result on a folder once the program finishs execution.
