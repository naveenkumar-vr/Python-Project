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
class server_receive(threading.Thread):
    def __init__(self,conn,client_name):
        threading.Thread.__init__(self)
        self.conn = conn
        self.stop = False
        server_receive.client_name = client_name

    def message_receive(self):
        data = self.conn.recv(1024)
        self.conn.send('OK')
        return self.conn.recv(1024)
        raise IOError

    def run(self):
        while not self.stop:
            try:
                message = self.message_receive()
                sys.stdout.flush()
                print '\r' + server_receive.client_name + ": " + message
            except IOError:
                print("client has closed chat")
                sys.exit()

#connects the socket to the corresponding send and receive connections
def set_connections(conn1,conn2):
    connect={}
    state = conn1.recv(9)
    conn2.recv(9)
    if state == 'WILL RECV':
        connect['send'] = conn1
        connect['recv'] = conn2
    else:
        connect['recv'] = conn1
        connect['send'] = conn2
    return connect

#sendind the message
def message_send(conn, server_name, msg):
    if len(msg)<=999 and len(msg)>0:
        conn.send(str(len(msg)))
        if conn.recv(2) == 'OK':
            conn.send(msg)
    else:
        conn.send(str(999))
        if conn.recv(2) == 'OK':
            conn.send(msg[:999])
            message_send(conn, msg[1000:])


def main():
    server_name = raw_input("Enter the name: ")

    #socket initialization
    socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_object.bind((host, port))
    socket_object.listen(1)

    #waiting for connection...
    (conn1, addr1) = socket_object.accept()
    (conn2, addr2) = socket_object.accept()
    #connection established!

    connect = set_connections(conn1, conn2)

    #initializing server and client names
    conn2.send(server_name)
    client_name = conn1.recv(1024)
    receive = server_receive(connect['recv'],client_name)
    print("------------Start chatting-----------")

    #receive thread starts
    receive.start()

    #send starts
    while 1:
        send_data = raw_input("")
        while send_data=='':
            send_data = raw_input("")
        message_send(connect['send'], server_name, send_data)

if __name__=='__main__':
    try:
        main()
    except IOError:
        print "Input Output Error occured !"
    except RuntimeError:
        print "PyChat encountered a run-time error !"
    except Exception:
        print "Exception occured !"
    finally:
        print "PyChat is closing due to technical error. Reopen PyChat and try again :)"
        sys.exit(1)
