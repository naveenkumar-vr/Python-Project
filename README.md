#Python Project
Introduction:

	The project is about communication between two computers. This is done by using socket programing and threading. This project has two codes, server and client, where the names says which one is ran in which computer.


About the project:

	In this project, socket programming is used because that is the easiest way communicate between two computers. 
  In this project I used two sockets, one is for sending and other is for receiving. 
  This is because always the code will compile and run in the order that we give, but here we have to run two things at the same time i.e., sending the input of server/client and receiving the input of the client/server. 
  These sockets will be found out by the function called set_connections in server, where the client will send strings like “WILL RECV” (receiving socket) and “WILL SEND” (sending socket).
  Now we have to think how to run two functions at the same the time, that’s why we use threading. Here threading is used for receiving. 
  I used to class for only receiving.  So that we can run the receiving code parallelly with sending. Therefore, the code will be running regularly in the order, where only the sending will be there.
  Now we are adding threading of receiving to run the code parallelly with code.


Conclusion:

	The project is read now. This is now can be used to chat like normal chatting using communication apps. But here we can chat in terminal using this project.
