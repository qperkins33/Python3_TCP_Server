Student Name: Quin Perkins
Student Class: ICS 460-02 Networks and Security
Assignment Name: TCP Web Server Assignment


Description: This program demonstrated the basics of socket programming for TCP connections in Python3. Including creating a socket, binding it to a specific address and port, and handling HTTP packets. This also offers insights into the HTTP header format.


Objective:   
- Accepts and dissects the HTTP request.     
- Retrieves the desired file from the server’s file system.   
- Constructs an HTTP response message, comprising the requested file and header lines.
- Forwards the response directly to the client.
- Returns an HTTP “404 Not Found” message if the server cannot find the requested file.


Instructions for Launching and Testing the Server:
1. Run webserver.py by typing "python3 webserver.py" in your terminal (be sure to include the correct path).
2. Identify the IP address of the host running the server, for example, 128.238.251.26 or localhost.
3. The port number is: 12000
3. To view HelloWorld.html in your browser, open a browser and enter the URL. Example: http://localhost:12000/HelloWorld.html
4. Attempt to retrieve a non-existent file. Your server should return a “404 Not Found” message. Example: http://localhost:12000/GoodbyeWorld.html


Instructions for Running and Testing the Client Program:
1. Launch the Server
2. Run webclient.py by typing "python3 webclient.py localhost 12000 HelloWorld.html" in a seperate terminal (be sure to include the correct path). The response should be:
  Connected to server.
  Server Host: localhost
  Server Port: 12000
  File Name: HelloWorld.html

  Sever Response: HTTP/1.1 200 OK
  Connection: close
  Date: Sat, 25 Jan 2025 02:52:26 GMT
  Content-Length: 139
  Content-Type: text/html

  <html>
  <body>

  <h1>Hello World!</h1>
  <h2>Hello World!</h2>
  <h3>Hello World!</h3>
  <h4>Hello World!</h4>
  <p>Hello World!</p>

  </body>
  </html>

  Connection closed.

3. Attempt to retrieve a non-existent file by typing "python3 webclient.py localhost 12000 GoodbyeWorld.html". The response should be:
  Connected to server.
  Server Host: localhost
  Server Port: 12000
  File Name: GoodbyeWorld.html

  Sever Response: HTTP/1.1 404 Not Found
  Connection: close
  Date: Sat, 25 Jan 2025 02:56:22 GMT
  Content-Length: 48
  Content-Type: text/html

  <html><body><h1>404 Not Found</h1></body></html>
  Connection closed.
