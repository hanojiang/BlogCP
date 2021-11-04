/*@!Encoding:936*/
// ---------------------------------------------------
// node global variables.
// ---------------------------------------------------
variables
{
  const int gMTU = 1500;                  // tcp mtu
  const dword gIPV4_STR_SIZE = 16;        // IPv4 string size
  const dword gINVALID_SOCKET = ~0;       // invalid socket constant
  dword gListenPort = 13400;              // port to send udp to.
  dword gClientSocket = gINVALID_SOCKET;  // client side: a demo client's socket.
  char gClientTcpBuffer[gMTU];            // tcp receive buffer of client
  //char gServerIpAddrStr[gIPV4_STR_SIZE] = "127.0.0.1"; // the IP of the server
  char gServerIpAddrStr[gIPV4_STR_SIZE] = "172.31.7.1"; // the IP of the server
  
  message 0x401 gWakeup_tbox;
  message 0x459 gDoipAct;
  msTimer gSendWakeTimer;
  msTimer gSendDoipActTimer;
  
  timer gStartTcpConnect;
  timer gStopWakeup;
  timer gRestartSimu;
  
  byte gStopWakeupFlag = 0;
  dword gTestNumber = 0;
}

on timer gSendWakeTimer
{
  gWakeup_tbox.byte(0) = 0x03;
  gWakeup_tbox.dlc = 1;
  output(gWakeup_tbox);
  if (0 == gStopWakeupFlag)
  {
    setTimer(gSendWakeTimer, 20);
  }
  
  
}

on timer gSendDoipActTimer
{
  gDoipAct.dlc = 8;
  gDoipAct.byte(4) = 0x10;
  output(gDoipAct);
  if (0 == gStopWakeupFlag)
  {
    setTimer(gSendDoipActTimer, 100);
  }
  
  
}

on timer gStartTcpConnect
{
  clientConnect();
}


on timer gStopWakeup
{
  gStopWakeupFlag = 1;
}

on timer gRestartSimu
{
  gTestNumber ++;
  
  write("*******************************TEST NUMBER %d **********************************************",gTestNumber);
  gStopWakeupFlag = 0;
  setTimer(gSendWakeTimer, 20);
  setTimer(gSendDoipActTimer, 100);
  setTimer(gStartTcpConnect, 10);
  setTimer(gStopWakeup, 20);
  //clientConnect();
  setTimer(gRestartSimu,60);
}
// ---------------------------------------------------
// Interaction: Client connects to server
// ---------------------------------------------------
on key 'c'
{
  clientConnect();
}

// ---------------------------------------------------
// Interaction: Client disconnects from server.
// ---------------------------------------------------
on key 'd'
{
  clientDisconnect();
}

// ---------------------------------------------------
// Interaction: Client sends a request to the server
// ---------------------------------------------------
on key 's'
{
  clientSendRequest();
}

// ---------------------------------------------------
// Interaction: Stop measurement
// ---------------------------------------------------
on key 'q'
{
  stop();
}

// ---------------------------------------------------
// Connection operation completes
// ---------------------------------------------------
void OnTcpConnect( dword socket, long result)
{
  writeLineEx(1, 1, " [ C: OnTcpConnect called. (result: %d)]", result);
  if (result == 0)
  {
    if (socket == gClientSocket)
    {
      write("C: Client connected to server done. (socket: %d, result: %d)", socket, result);
      clientSendRequest();
      startReceive(gClientSocket, gClientTcpBuffer);
    }
  }
}

// ---------------------------------------------------
// When asynchronous TcpSend completes...
// ---------------------------------------------------
void OnTcpSend( dword socket, long result, char buffer[], dword size)
{
  writeLineEx(1, 1, " [ C: OnTcpSend called. (result: %d)]", result);
  if (result == 0)
  {
    if (socket != gINVALID_SOCKET)
    {
      if (socket == gClientSocket)
      {
        write("C: Client sent %d bytes to server done. (socket %d, result: %d)", size, socket, result);
      }
    }
  }
}

// ---------------------------------------------------
// When receiving data on socket...
// ---------------------------------------------------
void OnTcpReceive( dword socket, long result, dword address, dword port, char buffer[], dword size)
{
  dword i;
  byte sendDiagData[14] = {
    0x02, 0xfd, 0x80, 0x01, 0x00,0x00,0x00,0x06,  0x0f,0x00,0x10,0x00, 0x10, 0x03
  };
  writeLineEx(1, 1, " [ C: OnTcpReceive called. (result: %d) ]", result);
  if (result == 0)
  {
    if (socket == gClientSocket)
    {
      // client receives from server...
      write("C: Client received %d bytes from server: %s (result: %d)", size, buffer, result);
      
//      for(i=0; i<size;i++)
//      {
//        write("%x",buffer[i]);
//        
//      }
      // check server's answer...
      if (strstr(buffer, "WELCOME") >= 0)
      {
        write("C: Server told us WELCOME. Connection established.");
      }
      else if (strstr(buffer, "ANSWER") >= 0)
      {
        write("C: Received server answer: %s", buffer);
      }
      
      startReceive(gClientSocket, gClientTcpBuffer);
      if(size == 21)
      {
        sendTcpData(gClientSocket, sendDiagData, 14);
      }
      else if(size == 18)
      {
        clientDisconnect();
      }
      // continue receiving data on valid socket.
      //startReceive(gClientSocket, gClientTcpBuffer);
      // show menu...
      showMenu(1);
    }
    else if (socket != gINVALID_SOCKET)
    {
      writeLineEx(1, 3, " [ C: UNIMPLEMENTED: Received %d bytes on socket %d from 0x%x:%d with data: %s (result: %d) ]", size, socket, address, port, buffer, result);
    }
  }
}

// ---------------------------------------------------
// TCP socket receives a close notification
// ( remote closed )
// ---------------------------------------------------
void OnTcpClose( dword socket, long result)
{
  if (socket == gClientSocket)
  {
    TcpClose(gClientSocket);
    gClientSocket = gINVALID_SOCKET;
    writeLineEx(1, 1, " [ C: OnTcpClose called. (socket: %d, result: %d) ]", socket, result);
    showMenu(0);
  }
}

// ---------------------------------------------------
// connect a client...
// ---------------------------------------------------
void clientConnect()
{
  dword result;
  if (gClientSocket != gINVALID_SOCKET)
  {
    writeLineEx(1, 2, " [ C: The client is already connected. ]");
    return;
  }
  writeLineEx(1, 1, " [ C: DEMO connecting one client... ]");
  gClientSocket = TcpOpen( 0, 0 );
  if (gClientSocket == gINVALID_SOCKET)
  {
    writeLineEx(1, 3, " [ C: TcpOpen: FAILED. ]");
  }
  else
  {
    result = TcpConnect( gClientSocket, IpGetAddressAsNumber(gServerIpAddrStr), gListenPort );
    if ( result == -1 )
    {
      result = IpGetLastSocketError(gClientSocket);
      if (result != 10035)
      {
        writeLineEx( 1, 3, " [ C: TcpConnect for client failed with error %d ]", result );
      }
    }
    else
    {
      writeLineEx(1, 3, " [ C: TcpConnect for client failed with error %d ]", result);
    };
    // => Connection established in callback OnTcpConnect...
  }
}

// ---------------------------------------------------
// client disconnects...
// ---------------------------------------------------
void clientDisconnect()
{
  if (gClientSocket != gINVALID_SOCKET)
  {
    write("C: Disconnecting from server. (socket %d)", gClientSocket);
    TcpClose(gClientSocket);
    gClientSocket = gINVALID_SOCKET;
    //showMenu(0);
  }
}

// ---------------------------------------------------
// client sends a request to server.
// ---------------------------------------------------
void clientSendRequest()
{
  // if client is connected...
  byte sendData[19] = {
    0x02, 0xfd, 0x00, 0x05, 0x00, 0x00, 0x00,0x0b,0x0f,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
  };
  
  if (gClientSocket != gINVALID_SOCKET)
  {
    write("C: Sending data to server. (socket %d)", gClientSocket);
    sendTcpData(gClientSocket, sendData, 19);
    //sendTcpData(gClientSocket, sendData, 14);
  }
  
}

// ---------------------------------------------------
// show a little write menu to let you know what you can do next.
// ---------------------------------------------------
void showMenu(int connected)
{
//  write("--------------[MENU]--------------------");
//  if (!connected)
//  {
//    write("- Press 'c' to connect client ...");
//  }
//  else
//  {
//    write("- Press 's' to send message to server...");
//    write("- Press 'd' to disconnect from server...");
//    write("- Press 'x' to let server disconnect client...");
//  }
//  write("- Press 'q' to stop measurement...");
//  write("----------------------------------------");
}

// ---------------------------------------------------
// send tcp data.
// ---------------------------------------------------
void sendTcpData( dword socket, byte data[], dword size )
{
 long result;
  //dword size;
  //size = elcount(data);
  result = TcpSend(socket, data, size);
  if (result == 0)
  {
    // sending took place immediately.
    //writeLineEx(1, 1, " [ C: Synchronous sending: '%s' on socket %d ]", data, socket);
    //OnTcpSend(socket, result, data, size); // trigger callback manually
  }
  else
  {
    if (result == -1)
    {
      result = IpGetLastSocketError(socket);
      if (result == 997)
      {
        // sending is done asynchronously.
       // writeLineEx(1, 1, " [ C: Asynchronous sending: '%s' on socket %d ]", data, socket);
        // => OnTcpSend is called when done sending.
      }
      else
      {
        writeLineEx( 1, 3, " [ C: sendTcpData: Error sending data. (%d) ]", result);
      }
    }
    else
    {
      writeLineEx( 1, 3, " [ C: sendTcpData: Error sending data. (%d) ]", result);
    }
  }
}
on start
{
  //showMenu(0);
  
  
  setTimer(gSendWakeTimer, 20);
  setTimer(gSendDoipActTimer, 100);
  setTimer(gStartTcpConnect, 10);
  setTimer(gStopWakeup, 20);
  //clientConnect();
  setTimer(gRestartSimu,60);
  
}

// ---------------------------------------------------
// start receiving on given socket into given buffer.
// ---------------------------------------------------
void startReceive ( dword socket, char buffer[] )
{
  long result;
  result = TcpReceive( socket, buffer, elcount(buffer) );
  if (result == -1)
  {
    result = IpGetLastSocketError(socket);
    if (result != 997) // not asynchronous
    {
      // failure
      writeLineEx( 1, 3, "S: TcpReceive error %d", result);
    }
  }
  else if (result != 0) // synchronous sending failed
  {
    // failure
    writeLineEx( 1, 3, "S: TcpReceive error %d", result);
  }
}