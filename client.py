import socket, sys
import threading

try:
    host = 'localhost'
    port = 8000
except:
    print("Incorrect parameters")
    print("i.e host and port")
    sys.exit(1)

#thread class for receiving
class client_receive(threading.Thread):
    def __init__(self,conn,server_name):
        threading.Thread.__init__(self)
        self.conn = conn
        self.stop = False
        client_receive.server_name = server_name

    def message_receive(self):
        data = self.conn.recv(1024)
        self.conn.send('OK')
        return self.conn.recv(1024)
        raise IOError

    def run(self):
        while not self.stop:
            try:
                sys.stdout.flush()
                message = '\r' + client_receive.server_name + ": " + self.message_receive()
                sys.stdout.flush()
                print message
            except IOError:
                print("client has closed chat")
                sys.exit()

#sending the message
def message_send(conn,client_name,msg):
    if len(msg)<=999 and len(msg)>0:
        conn.send(str(len(msg)))
        if conn.recv(2) == 'OK':
            conn.send(msg)
    else:
        conn.send(str(999))
        if conn.recv(2) == 'OK':
            conn.send(msg[:999])
            message_send(conn,msg[1000:])

def main():
    client_name = raw_input("Enter the name: ")

    #socket initialization
    socket_object1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_object1.connect((host,port))

    #selecting send and receive sockets
    socket_object1.send('WILL SEND')
    socket_object2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_object2.connect((host,port))
    socket_object2.send('WILL RECV')
    #connection established

    #initializing server and client names
    server_name = socket_object2.recv(1024)
    socket_object1.send(client_name)
    receive = client_receive(socket_object2,server_name)
    print("------------Start chatting------------")

    #receive thread starts
    receive.start()

    #send starts
    while 1:
        send_data = raw_input("")
        while send_data=='':
            send_data = raw_input("")
        message_send(socket_object1,client_name,send_data)

if __name__ == '__main__':
    try:
        main()
    except IOError as (errno, sterror):
        print "Input Output Error occured !"
    except Exception:
        print "Exception occured !"
    except RuntimeError:
        print "PyChat encountered a run-time error !"
    finally:
        print "PyChat is closing due to technical error. Reopen PyChatand try again :)"
        sys.exit(1)
