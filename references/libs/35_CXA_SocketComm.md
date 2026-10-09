# 35 CXA_SocketComm

## 35.1 Introduction and overview

The CXA_SocketComm library contains functions and function blocks to estab‐
lish a connection to and data transfer via TCP (Transmission Control Protocol)
and UDP (User Datagram Protocol).
TCP and UDP are IP-based internet data transport protocols.
While TCP is a connection-oriented protocol that establishes connections and
maintains them while the application transfers data, UDP is a package-ori‐
ented connection-free protocol that sends data packages within a network
from one application to another.
CXA_SocketComm supports synchronous and asynchronous communication.
The synchronous communication is supported by functions.
Function blocks are used for the asynchronous communication. It is not rec‐
ommended to use functions and function blocks within the same TCP or UDP
connection.
The IP-based communication is not real-time capable. That means that it
cannot be guaranteed that data reaches its target within a specific time slot.
Thus, it should only be used for pure data exchange.
It is not to be used for process synchronization and controlling time-critical
inputs/outputs.
The CXA_SocketComm library uses SysSockets library functions. The IP-based
communication is only executed by the operating system of the control. Thus,
there can be differences in the runtime behavior on different controls.
The basic function package PLC is sufficient for the library of the ctrlX system.

I/O time response of the function blocks
Every function block supports the common error structure and the defined
behavior with the outputs "Error", "ErrorID" and "ErrorIdent".
All function blocks with the "Enable" input and "Done" output have the same
level-controlled runtime behavior. A rising edge at the "Enable" input starts
the execution. A falling edge stops the execution and resets all binary out‐
puts.

                                                                  TCP       1344

If "Done" is TRUE, the function block has successfully completed its task. The
function block remains in this state until "Enable" is reset. No further actions
are performed.
If there is an error, "Error" is set and "ErrorID" and "ErrorIdent" contain the
error code. "Done" and "Error" are reset when "Enable" is reset.

## 35.2 TCP

### 35.2.1 Introduction and overview

TCP is a connection-orientated IP protocol. Before data is exchanged, the
client has to be connected to an open TCP server port. The data flow is based
on characters. The sent data is subdivided into data packages by the TCP
protocol, transferred and recombined into a character stream at the other side
(server or client).
The order of the characters are sent is always maintained. If an error occurs
during transmission, the package in question is automatically resent. There‐
fore, data cannot be lost. A connection loss is reported in an error code at
next read or write access.
TCP is suitable for non-cyclic communication, when data has to reliably reach
the receiver. A good example is a log file. It is not important when the data
reaches its target but it has to reach the remote host.
The following chart shows a TCP connection with subsequent data transmis‐
sion via TCP.

1058 /    ctrlX PLC Engineering
1344      TCP

TCP server example
The following example shows a simple TCP server application, which sends an
ASCII text using the CXA_SocketComm library.
When started, the program opens a TCP server on port 4242 and waits for an
incoming connection. After the connection has been set up, the text is sent
and the connection is closed. The program opens the server port again and
waits for further incoming connections.
Einfaches TCP-Server-Programm (Deklaration)
(* This very simple test program waits for an incomming TCP connection on port
4242. *)
(* After the connection is established, it sends the string "Hello
World!"           *)
(* and closes the
connection                                                         *)

PROGRAM PLC_PRG
VAR
  (* used function block instances *)
  fbTCPConnectionAsync: IL_TCPConnectionAsync;
  fbTCPSendAsync: IL_TCPSendAsync;

  (* variables *)
  udiSocket: RTS_IEC_HANDLE; (* socket handle *)
  strHello: STRING := 'Hello World!$r$n'; (* text to send *)
END_VAR

                                                                     TCP       1344

Einfaches TCP-Server-Programm (Implementation)
(* Check if connection is established *)
IF fbTCPConnectionAsync.Done = FALSE THEN
  (* No connection established yet => setup server mode and wait *)
  fbTCPConnectionAsync(Enable:=TRUE, Server:=TRUE, Port:=4242,
Socket=>udiSocket);
  IF fbTCPConnectionAsync.Error = TRUE THEN
(* error while establishing connection => reset everything *)
fbTCPConnectionAsync(Enable:=FALSE, Socket=>udiSocket);
  END_IF
ELSE
  (* connection established => send text *)

  fbTCPSendAsync(Execute:=TRUE, Socket:=udiSocket, ValueAdr:=ADR(strHello),
NoOfBytes:=LEN(strHello));
  IF fbTCPSendAsync.Done=TRUE OR fbTCPSendAsync.Error=TRUE THEN
(* text completely send or some error => close connection *)
fbTCPSendAsync(Execute:=FALSE);
fbTCPConnectionAsync(Enable:=FALSE, Socket=>udiSocket);
  END_IF
END_IF
Use the Windows "Telnet" program to connect to the control. The first param‐
eter is the IP address, the second parameter is the port:
     Telnet 192.168.1.1 4242

     TCP client example
     The following example shows a TCP client, which connects to a TCP server at
     port 4242. After the connection has been set up, the string sends "Hello" and
     waits for a response. Once the response package is received, the connection
     is closed.
Einfaches TCP-Client-Programm (Deklaration)
PROGRAM PLC_PRG
VAR
  fbConnection: IL_TCPConnectionAsync;
  fbSend: IL_TCPSendAsync;
  fbRecv: IL_TCPRecvAsync;

udiSocket: RTS_IEC_HANDLE := SOCKET_INVALID;

strSend: STRING := 'Hello';
strRecv: STRING;

  iState: INT := 0;
END_VAR
Einfaches TCP-Client-Programm (Implementation)
CASE iState OF

0:
  fbConnection(Enable:=FALSE);
  fbSend(Execute:=FALSE);
  fbRecv(Execute:=FALSE);
  diSocket := SOCKET_INVALID;
  iState := 1;

1:
  fbConnection(Enable:=TRUE, Server:=FALSE, Address:='192.168.42.254',

1060 /    ctrlX PLC Engineering
1344      TCP

Port:=4242);
  IF fbConnection.Done=TRUE THEN
    (* Connection established *)
    udiSocket := fbConnection.Socket;
    iState := 2;
  END_IF

2:
  (* Send some data *)
  fbSend(Execute:=TRUE, Socket:=udiSocket, ValueAdr:=ADR(strSend),
NoOfBytes:=LEN(strSend));
  IF fbSend.Done=TRUE THEN
(* Send done *)
    fbSend(Execute:=FALSE);
    iState := 3;
  END_IF

3:
  (* Receive some data *)
  fbRecv(Execute:=TRUE, Socket:=udiSocket, ValueAdr:=ADR(strRecv),
NoOfBytes:=SIZEOF(strRecv)-1);
  IF fbRecv.Done=TRUE THEN
    (* Received some data *)
    strRecv := LEFT(strRecv, UDINT_TO_INT(fbRecv.NoOfRecBytes)); (* end of
string marker *)
    fbRecv(Execute:=FALSE);
    iState := 4;
  END_IF

4:
  (* Close the connection *)
  fbConnection(Enable:=FALSE);
  diSocket := SOCKET_INVALID;

END_CASE

TCP cyclic - example
The following example shows a simple TCO application cyclically exchanging a
data structure between two devices using the CXA_SocketComm library.
Upon start, the program opens a TCP server on the port 50001 and waits
for an incoming connection (server) or tries to establish a connection to the
remote host (client). After the connection has been set up, the data structure
is cyclically exchanged between the two communication partners. The pro‐
gram opens the server port again and waits for further incoming connections.
TCP-Server-Programm
PROGRAM Client
VAR
  fbIL_TCPCyclic: IL_TCPCyclic;

   SendData: MY_STRUCTURE;
  RecvData: MY_STRUCTURE;

bEnable: BOOL;
bInOperation: BOOL;
bError: BOOL;
nErrorCode: ERROR_CODE;
nErrorIdent: ERROR_STRUCT;

TCP       1344

  nStatus: IL_CONN_STATUS;
  tResponseTime: TIME;
  bDoneSend: BOOL;
  bDoneRecv: BOOL;
END_VAR

fbIL_TCPCyclic(
  Enable:= bEnable,
  Mode:= Cyclic_Client,
  IpAddress:= '192.168.0.10',
  Port:= 50001,
  SendDataAdr:= ADR(SendData),

                  CXA_SocketComm
  RecvDataAdr:= ADR(RecvData),
  SizeOfSendData:= SIZEOF(SendData),
  SizeOfRecvData:= SIZEOF(RecvData),
  Timeout:= T#1500MS,
  InOperation=> bInOperation,
  Error=> bError,
  ErrorID=> nErrorCode,
  ErrorIdent=> nErrorIdent,
  Status=> nStatus,
  ResponseTime=> tResponseTime,
  DoneSend=> bDoneSend,
  DoneRecv=> bDoneRecv);
TCP-Client-Programm
PROGRAM Server
VAR
  fbIL_TCPCyclic: IL_TCPCyclic;

  SendData: MY_STRUCTURE;
  RecvData: MY_STRUCTURE;

  bEnable: BOOL;
  bInOperation: BOOL;
  bError: BOOL;
  nErrorCode: ERROR_CODE;
  nErrorIdent: ERROR_STRUCT;
  nStatus: IL_CONN_STATUS;
  tResponseTime: TIME;
  bDoneSend: BOOL;
  bDoneRecv: BOOL;
END_VAR

fbIL_TCPCyclic(
  Enable:= bEnable,
  Mode:= Cyclic_Server,
  IpAddress:= '192.168.0.10',
  Port:= 50001,
  SendDataAdr:= ADR(SendData),
  RecvDataAdr:= ADR(RecvData),
  SizeOfSendData:= SIZEOF(SendData),
  SizeOfRecvData:= SIZEOF(RecvData),
  Timeout:= T#1500MS,
  InOperation=> bInOperation,
  Error=> bError,
  ErrorID=> nErrorCode,
  ErrorIdent=> nErrorIdent,

1062 /    ctrlX PLC Engineering
1344      TCP

   Status=> nStatus,
   ResponseTime=> tResponseTime,
   DoneSend=> bDoneSend,
   DoneRecv=> bDoneRecv);
Datenstruktur
// Example of a data structure
TYPE MY_STRUCTURE :
STRUCT
  bTestBool   : BOOL;
  byTestByte : BYTE;
  uiTestUInt : UINT;
  rTestReal   : REAL;
  tTestTime   : TIME;
  strTest     : STRING(22) := 'Hello World';
  dwTest      : DWORD;
END_STRUCT
END_TYPE

### 35.2.2 Asynchronous function blocks

Introduction and overview
The TCP asynchronous function blocks are used in cyclic tasks and have to
be called cyclically. Normally, multiple calls are required to complete an oper‐
ation.
A function block starts with a rising edge at “Execute" and operates until
either "Done" or "Error" is TRUE. To start a new operation, reset “Execute" and
set it again.
A new TCP connection can be set up with ⮫ Chapter IL_TCPConnectionAsync
on page 1062. The connection is set up at a rising edge at “Enable” and closed
at a falling edge at “Enable”.
Once the connection has been set up, data can be exchanged with ⮫ Chapter
IL_TCPSendAsync on page 1067 and ⮫ Chapter IL_TCPRecvAsync on page 1069
or ⮫ Chapter IL_TCPRecvPacketAsync on page 1071 via the connection.
TCP is a character stream-based protocol that guarantees the order and con‐
sistency of transmitted data. Received data is merged again internally to form
a marking current. If a package-based communication is required, the user is
responsible for identifying the package header.

IL_TCPConnectionAsync
Brief description
The function block IL_TCPConnectionAsync establishes either a TCP server or
a TCP client depending on the "Server” input.

                                                                           TCP        1344

         Interface description

Table 915: Interface variables of the IL_TCPConnectionAsync function block
               Name            Type             Description
VAR_INPUT      Enable          BOOL             Starts at a rising edge
                                                Binary outputs are reset at a falling edge
               Server          BOOL             TRUE: TCP server is created
                                                FALSE: TCP client is created.
               Address         STRING           If "Server" is set, this input is not used and the indi‐
                                                vidual IP address is used. If "Server" is FALSE, this
                                                input contains the IP address of the device to be
                                                connected
               Port            UINT             The TCP port at which incoming connections are
                                                expected or to which they are to be connected
           KeepAliveTi‐ UDINT                   "Keep-Alive" timeout option, unit in milliseconds
           meMS
VAR_OUTPUT Done         BOOL                TRUE indicates that the connection was successfully
                                            set up
               Active          BOOL         TRUE indicates that the function block is waiting for
                                            the connection to be set up
               Error           BOOL         TRUE indicates an error
               ErrorID         ⮫ ERROR_CODE Error class
               ErrorIdent  ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
                           T              on page 1066 )
               Socket      RTS_IEC_HANDL Contains the socket handle of the new connection
                           E
               SocketState ⮫ SC_STATE_TYP Displays the status of the created socket.
                           E

Table 916: Min./max. and default values of the IL_TCPConnectionAsync function block inputs
Name           Type              Min. value     Max. value    Default value   Effective
Enable         BOOL              FALSE          TRUE          FALSE           Continuous
Server         BOOL              FALSE          TRUE          FALSE           Rising edge at "Enable"
Address        STRING                                         ''              Rising edge at "Enable"
Port           UINT              0              65535         0               Rising edge at "Enable"
KeepAliveTi‐   UDINT             0              4294967295    10000           Rising edge at "Enable"
meMS

1064 /    ctrlX PLC Engineering
1344      TCP

SC_STATE_TYPE (ENUM)
The enumeration "SC_STATE_TYPE" specifies the state of the created socket.
Element                  Value          Description
SC_CREATE                1              Creating a new socket and return the socket handle.
SC_IOCTL                 2              I/O control of a socket.
SC_KEEP_ALIVE            4              Retain the connections.
SC_REUSE                 5              Allow reuse of local address.
SC_BIND                  6              Connect a socket to a socket address and a port number.
SC_LISTEN                7              Listening for new connections on a TCP server socket.
SC_CONNECT               8              Establishing a connection as a client to a TCP server.
SC_WAIT                  9              Check a number of sockets for activity.
SC_ACCEPT                10             Accept the next incoming TCP connection.
SC_ACCEPT_IOCTL          11             I/O control of a connection socket.
SC_WAIT_CONNECT          12             Check a number of sockets for activity.
SC_ERROR_STATE           16             Received a specific error from the socket.
SC_END                   17             Close a socket.

Functional description
The function block IL_TCPConnectionAsync establishes either a TCP server or
a TCP client depending on the "Server” input. Processing starts at a rising
edge at "Enable". The function block has to be called cyclically until "Done" or
"Error" are TRUE.
In server mode, the function block opens a socket at the TCP port specified
in "Port". If another TCP client connects to this port, the connection is estab‐
lished. The socket handle belonging to this connection is displayed at the
"Socket" output and the "Done" output is set. While the system is waiting for
an incoming connection, the "Active" output is set.
In client mode, the function block connects to the IP address specified in
"Address" on the TCP target port specified in "Port". After a successfully
established connection, the socket handle is displayed at the "Socket" output
and the "Done" output is set. While waiting for a connection, the "Active"
output is set.
Once a connection is established, the "Socket" output contains the socket
handle of the connection.
In case of error, the "Error" output is set. SOCKET_INVALID is displayed at the
"Socket" output. The error class and the exact error code can be read at the
"ErrorID" and "ErrorIdent" outputs.
If "Enable" is set to FALSE before "Done" is TRUE, no connection is estab‐
lished and all internal resources are enabled. If "Enable" is set to FALSE after
a connection is established, the connection is closed. Any errors that occur
during connection termination are handled internally and are not output to the
error outputs. After "Enable" was set to FALSE, the "Socket" output is set to
SOCKET_INVALID.
The "Active" output can be used as timeout indicator during connection setup.
Typical timeouts for connection setup range from 2 to 10 seconds.
IL_TCPCloseAsync is not to be used on sockets created with IL_TCPConnectio‐
nAsync.

                                                               TCP       1344

Signal-time diagrams

1066 /    ctrlX PLC Engineering
1344      TCP

 server

 Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 917: Error codes generated by IL_TCPConnectionAsync
ErrorID                   Additional1  Additional2 Description
OTHER_ERROR              16#0A0F.0101 16#0C23.100 Socket could not be created
                                            1
OTHER_ERROR              16#0A0F.0101 16#0C23.100 Error when setting I/O mode
                                            2
OTHER_ERROR              16#0A0F.0101 16#0C23.100 Could not connect socket to port
                                            3

                                                               TCP       1344

ErrorID              Additional1  Additional2 Description
OTHER_ERROR         16#0A0F.0101 16#0C23.100 Socket could not go into list mode.
                  4
OTHER_ERROR         16#0A0F.0101 16#0C23.100 Could not accept incoming connection.
                  5
OTHER_ERROR         16#0A0F.0101 16#0C23.100 Error when connecting to another device.
                  6
INPUT_INVALID_ERROR 16#0A0F.0101 16#0C23.020 Destination address invalid
                  8
COMMUNICA‐          16#0A0F.0101 16#0C23.020 Remote host denied connection establish‐
TION_ERROR                             9      ment

COMMUNICA‐          16#0A0F.0101 16#0C23.020 No route to target device
TION_ERROR                             C
Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
codes of the CXA_Table on page 1131.

IL_TCPSendAsync
Brief description
The function block IL_TCPSendAsync sends data via a connection established
with ⮫ Chapter IL_TCPConnectionAsync on page 1062.

Interface description

Table 918: Interface variables of the IL_TCPSendAsync function block
              Name           Type            Description
VAR_INPUT     Execute        BOOL            Starts at a rising edge
              Socket         UDINT           IL_TCPConnectionAsync or IL_TCPInitialAsync socket
                                             handle
              ValueAdr       POINTER TO      Initial address of data to be sent
                             BYTE
           NoOfBytes         UDINT        Number of characters to be sent
VAR_OUTPUT Done              BOOL         TRUE indicates that all data was successfully sent
           Active            BOOL         TRUE indicates that the function block sends data
           Error             BOOL         TRUE indicates an error
           ErrorID           ⮫ ERROR_CODE Error class
              ErrorIdent     ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
                             T             on page 1068 )
              NoOfSend‐      UDINT         Number of bytes actually sent
              Bytes

1068 /    ctrlX PLC Engineering
1344      TCP

Table 919: Min./max. and default values of the IL_TCPSendAsync function block inputs
Name               Type         Min. value      Max. value  Default value Applied
Execute            BOOL                                     FALSE         Continuous
Socket             UDINT        0               16#FFFFFFFF SOCKET_INVA Rising edge at “Exe‐
                                                            LID           cute”
ValueAdr           POINTER TO                               0             Rising edge at “Exe‐
                   BYTE                                                   cute”
NoOfBytes          UDINT        0               16#FFFFFFFF 0             Rising edge at “Exe‐
                                                                          cute”

Functional Description
The function block IL_TCPSendAsync sends data via a connection set up with
⮫ Chapter IL_TCPConnectionAsync on page 1062.
Transmission begins at a rising edge at "Execute".
The function block has to be called cyclically until "Done" or "Error" is TRUE.

The buffer to be sent is applied to the "ValueAdr" input. The number of char‐
acters to be sent is applied at the "NoOfBytes" input.
If "Execute" is reset before "Done" is TRUE, the transmission is interrupted.
The number of bytes already sent can be retrieved at the "NoOfSentBytes"
output.
The "Active" output is set during data transmission. "Active" can be used as a
timeout indicator. Typical transmission timeouts range from 1 to 2 seconds.
During transmission ("Active" is TRUE), the number of bytes already sent can
be retrieved at the "NoOfSentBytes" output. Generally all bytes are sent in
one call.
IL_TCPSendAsync ensures that all bytes were sent before setting "Done".

IL_TCPSendAsync detects an interrupted connection. This is displayed by the
relevant error code.

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 920: Error codes generated by IL_TCPSendAsync
ErrorID              Additional1 Additional2 Description
OTHER_ERROR         16#0A0F.010 16#0C23.00 General error
                          1          01
INPUT_RANGE_ERROR 16#0A0F.010 16#0C23.00 Input "ValueAdr" is not set
                          1          06
INPUT_RANGE_ERROR 16#0A0F.010 16#0C23.00 Input "NoOfBytes" is 0
                          1          0F
INPUT_INVALID_ERROR 16#0A0F.010 16#0C23.02 Socket handle invalid
                          1          02
COMMUNICA‐          16#0A0F.010 16#0C23.02 Connection was closed
TION_ERROR                1          0E
COMMUNICA‐          16#0A0F.010 16#0C23.02 Remote host closed the connection
TION_ERROR                1          11
                       Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                       codes of the CXA_Table on page 1131.

                                                                TCP        1344

IL_TCPRecvAsync
Brief description
The function block IL_TCPRecvAsync receives data via a connection set up
with ⮫ Chapter IL_TCPConnectionAsync on page 1062.

Interface description

Table 921: Interface variables of the IL_TCPRecvAsync function block
              Name            Type          Description
VAR_INPUT     Execute         BOOL          Starts at a rising edge
                                            Binary outputs are reset at a falling edge
              Socket          RTS_IEC_HANDL IL_TCPConnectionAsync or IL_TCPInitialAsync socket
                              E             handle
              ValueAdr        POINTER TO    Initial address of the reception buffer
                              BYTE
           NoOfBytes          UDINT         Size of the received data buffer
VAR_OUTPUT Done               BOOL          TRUE indicates that all data was successfully
                                            received
              Active          BOOL          TRUE indicates that the function block is waiting for
                                            incoming data
              Error           BOOL          TRUE indicates an error
              ErrorID         ⮫ ERROR_CODE Error class
              ErrorIdent      ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
                              T             on page 1070 )
              NoOfRec‐        UDINT         Number of bytes received
              Bytes

Table 922: Min./max. and default values of the IL_TCPRecvAsync function block inputs
Name           Type        Min. value           Max. value  Default value Applied
Execute        BOOL                                         FALSE         Continuous
Socket         RTS_IEC_HAN 0                    16#FFFFFFFF SOCKET_INVA Rising edge at “Exe‐
               DLE                                          LID           cute”
ValueAdr       POINTER TO                                   0             Rising edge at “Exe‐
               BYTE                                                       cute”
NoOfBytes      UDINT       0                    16#FFFFFFFF 0             Rising edge at “Exe‐
                                                                          cute”

Functional Description
The function block IL_TCPRecvAsync receives data via a connection set up
with ⮫ Chapter IL_TCPConnectionAsync on page 1062.

1070 /    ctrlX PLC Engineering
1344      TCP

Transmission begins at a rising edge at "Execute".
The function block has to be called cyclically until "Done" or "Error" is TRUE.

If "Execute" is reset before "Done" is TRUE, the reception is interrupted. Only
a new rising edge at "Execute" initiates a new transmission.
The "Active" output is set while it is ready to receive.
“Active” remains TRUE until data is received.
The number of bytes received can be lower than the buffer size.
To receive the exact buffer size, use the function block ⮫ IL_TCPRecvPacketA‐
sync on page 1071. "Active" can be used as a timeout indicator.
If the number of the bytes sent by the remote host is higher than the buffer
size, only the number of bytes entered into "NoOfBytes" are copied to the
buffer. The remaining bytes are copied at next call.
"Active" can be used as a timeout indicator. Typical reception timeouts range
from 1 to 2 seconds.
IL_TCPRecvAsync detects a connection abort. This is displayed by the relevant
error code.

Signal-time diagram

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 923: Error codes generated by IL_TCPRecvAsync
ErrorID              Additional1 Additional2 Description
OTHER_ERROR         16#0A0F.010 16#0C23.00 General error
                          1          01
INPUT_RANGE_ERROR 16#0A0F.010 16#0C23.00 Input "ValueAdr" is not set
                          1          06
INPUT_RANGE_ERROR 16#0A0F.010 16#0C23.00 Input "NoOfBytes" is 0
                          1          0F
INPUT_INVALID_ERROR 16#0A0F.010 16#0C23.02 Socket handle invalid.
                          1          02
COMMUNICA‐          16#0A0F.010 16#0C23.02 Connection was closed
TION_ERROR                1          0E
COMMUNICA‐          16#0A0F.010 16#0C23.02 Remote host closed the connection
TION_ERROR                1          11
                     Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                     codes of the CXA_Table on page 1131.

                                                                  TCP       1344

IL_TCPRecvPacketAsync
Brief description
The function block IL_TCPRecvPacketAsync receives a defined number of
bytes via a connection established with ⮫ Chapter IL_TCPConnectionAsync
on page 1062.

Interface description

Table 924: Interface variables of the IL_TCPRecvPacketAsync function
              Name            Type             Description
VAR_INPUT     Execute         BOOL             Starts at a rising edge
                                               Binary outputs are reset at a falling edge
              Socket          UDINT            IL_TCPConnectionAsync or IL_TCPInitialAsync socket
                                               handle
              ValueAdr        POINTER TO       Initial address of the reception buffer
                              BYTE
           NoOfBytes          UDINT        Number of bytes to be received
VAR_OUTPUT Done               BOOL         TRUE indicates that all data was successfully
                                           received
              Active          BOOL         TRUE indicates that the function block is waiting for
                                           incoming data
              Error           BOOL         TRUE indicates an error
              ErrorID         ⮫ ERROR_CODE Error class
              ErrorIdent      ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
                              T             on page 1072 )
              NoOfRec‐        UDINT         Number of bytes copied to the reception buffer
              Bytes

Table 925: Min., max. and default values of the inputs of the IL_TCPRecvPacketAsync function
block
Name           Type             Min. value     Max. value  Default value Applied
Execute        BOOL                                        FALSE         Continuous
Socket         UDINT            0              16#FFFFFFFF SOCKET_INVA Rising edge at “Exe‐
                                                           LID           cute”
ValueAdr       POINTER TO                                  0             Rising edge at “Exe‐
               BYTE                                                      cute”
NoOfBytes      UDINT            0              16#FFFFFFFF 0             Rising edge at “Exe‐
                                                                         cute”

1072 /    ctrlX PLC Engineering
1344      TCP

Functional Description
The function block IL_TCPRecvPacketAsync receives a defined number of
bytes via a connection established with ⮫ Chapter IL_TCPConnectionAsync
on page 1062.
Transmission begins at a rising edge at "Enable".
The function block has to be called cyclically until "Done" or "Error" is TRUE.

The "Active" output is set during data transmission.
● If the amount of data is smaller than the buffer size, it is completely trans‐
   ferred. For the actual amount, refer to "NoOfRecBytes". ACTIVE remains
   TRUE until NoOfRecBytes < NoOfBytes.
● If the amount of data is equal to the buffer size, it is transferred and
   NoOfRecBytes = NoOfBytes. ACTIVE is set to FALSE and DONE to TRUE.
● If the amount of data is higher than the buffer size, only NoOfRecBytes is
   transferred. ACTIVE is set to FALSE and DONE to TRUE.
   Upon next function block call, the remaining bytes are transferred and
   might be followed by data of the next package to be transferred.
   Note! There can be a buffer overflow on the complete transmission path!
IL_TCPRecvPacketAsync detects an interrupted connection. This is displayed
by the relevant error code.

Signal-time diagram

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 926: Error codes generated by IL_TCPRecvPacketAsync
ErrorID              Additional1 Additional2 Description
OTHER_ERROR         16#0A0F.010 16#0C23.00 General error
                          1          01
INPUT_RANGE_ERROR 16#0A0F.010 16#0C23.00 Input "ValueAdr" is not set
                          1          06
INPUT_RANGE_ERROR 16#0A0F.010 16#0C23.00 Input "NoOfBytes" is 0
                          1          0F
INPUT_INVALID_ERROR 16#0A0F.010 16#0C23.02 Socket handle invalid.
                          1          02
COMMUNICA‐          16#0A0F.010 16#0C23.02 Connection was closed.
TION_ERROR                1          0E

                                                                     TCP       1344

ErrorID                       Additional1 Additional2 Description
COMMUNICA‐                   16#0A0F.010 16#0C23.02 Remote host closed the connection.
TION_ERROR                         1          11
   Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
   codes of the CXA_Table on page 1131.

### 35.2.3 Synchronous functions

Introduction and overview
The synchronous TCP functions are implemented as blocking calls. Thus, they
do not return until the operation is completed or an error occurred. These

functions are only to be used in free running tasks.
IL_TCPInitial establishes a connection and returns a socket handle. If the
socket handle is valid, the connection was established. After the connection
has been establishment, data can be sent and received via IL_TCPSend and
IL_TCPRecv.
IL_TCPClose closes an existing connection and enables the socket handle.
TCP is a character stream-based protocol that guarantees the order and con‐
sistency of transmitted data. Received data is merged again internally to form
a marking current. If a package-based communication is required, the user is
responsible for identifying the package header.

IL_TCPInitial
   Brief description
   The IL_TCPInitial function establishes either a TCP server or a TCP client
   depending on the "bServer" parameter.

   Interface description

Table 927: Interface variables of the IL_TCPInitial function
              Name             Type              Description
VAR_INPUT     bServer          BOOL              TRUE: TCP server is created
                                                 FALSE: TCP client is created.
              strAddress       STRING            If "bServer" is set, this input is not used and the
                                                 own IP address is used. If "bServer" is FALSE, this
                                                 input contains the IP address of the device to be
                                                 connected
              uiPort           UINT              The TCP port at which incoming connections are
                                                 expected or to which they are to be connected
              pudiSocket       POINTER TO        Contains the socket handle of the new connection
                               UDINT
              pudiEr‐          POINTER TO        Contains the error code
              rorNum           UDINT

1074 /    ctrlX PLC Engineering
1344      TCP

Name          Type              Description
RETURN                           UDINT             0 if a connection was successfully established; oth‐
                         erwise INVALID_SOCKET

Functional description
The IL_TCPInitial function establishes either a TCP server or a TCP client
depending on the "bServer" parameter.
In server mode, the function opens a socket at the TCP port given in "uiPort".
If another TCP client connects to this port, the connection is established. The
socket handle belonging to the connection is stored in "pdiSocket" and the
function returns with the return value 0.
In client mode, the function connects to the IP address provided in "strAd‐
dress" at the TCP target port provided in "uiPort". If a connection was estab‐
lished successfully, the socket handle is archived in "pdiSocket" and the func‐
tion returns with the return value 0. If no connection can be established
within 2 seconds, the function returns with the return value SOCKET_INVALID
and the "pudiErrorNum" contains a corresponding error code.
If an error occurs, the function returns with SOCKET_INVALID and stores the
error code in "pudiErrorNum".

Troubleshooting
The function uses the error table CXA_TABLE.
The function returns the following error codes in "pudiErrorNum":
Table 928: Error codes of the IL_TCPInitial
ErrorID                             pudiErrorNum    Description
OTHER_ERROR                         16#0C231001     Socket could not be created
OTHER_ERROR                         16#0C231002     Error when setting I/O mode
OTHER_ERROR                         16#0C231003     Could not connect socket to port
OTHER_ERROR                         16#0C231004     Socket could not go into list mode.
OTHER_ERROR                         16#0C231005     Could not accept incoming connection.
OTHER_ERROR                         16#0C231006     Error when connecting to another device.
INPUT_INVALID_ERROR                 16#0C230208     Target address invalid
COMMUNICATION_ERROR                 16#0C230209     Remote host denied connection establishment
COMMUNICATION_ERROR                 16#0C23020C     No route to target device
                          Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                          codes of the CXA_Table on page 1131.

IL_TCPSend
Brief description
The IL_TCPSend function sends data via a connection created with IL_TCPIni‐
tial.
This function does not return until either all data was transmitted or an error
occurs.

                                                                  TCP       1344

Interface description

Table 929: Interface variables of the IL_TCPSend function
              Name        Type                Description
VAR_INPUT     udiSocket   UDINT               IL_TCPInitial socket handle
              pbyValueAdr POINTER TO          Initial address of data to be sent.
                          BYTE
              pudiEr‐     POINTER TO          Contains the error code
              rorNum      UDINT
              udiNoOf‐    UDINT               Number of characters to be sent
              Bytes
RETURN                    UDINT               Number of bytes actually sent 0 indicates that the
                                              connection was closed or an error occurred.

Functional description
The IL_TCPSend function sends data via a connection created with IL_TCPIni‐
tial. This function does not return until either all data was transmitted or an
error occurred.
The buffer to be sent is created in "pbyValueAdr". The number of characters to
be sent is transferred in "udiNoOfBytes".
After successful transmission, this function returns the number of characters
transmitted. If 0 is returned, the connection was closed before data could
be sent. In case of error, the error code is stored to "pudiErrorNum" and the
function returns with a return value of 0.

Troubleshooting
The function uses the error table CXA_TABLE.
The function returns the following error codes in "pudiErrorNum":
Table 930: Error codes of the IL_TCPSend
ErrorID                       pudiErrorNum Description
INPUT_RANGE_ERROR             16#0C230006 Input "ValueAdr" is not set
INPUT_RANGE_ERROR             16#0C23000F Input "NoOfBytes" is 0
INPUT_INVALID_ERROR           16#0C230202 Invalid socket handle
COMMUNICATION_ERROR           16#0C23020E Connection was closed
COMMUNICATION_ERROR           16#0C230211 Socket was closed
                     Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                     codes of the CXA_Table on page 1131.

1076 /    ctrlX PLC Engineering
1344      TCP

IL_TCPRecv
Brief description
The IL_TCPRecv function receives data via a connection created with IL_TCPI‐
nitial. This function does not return until either data was received or an error
occurred.

Interface description

Table 931: Interface variables of the IL_TCPRecv function
                   Name        Type              Description
VAR_INPUT          udiSocket   UDINT             IL_TCPInitial socket handle
                   pbyValueAdr POINTER TO        Initial address of the received data buffer
                               BYTE
                   pudiEr‐     POINTER TO        Contains the error code
                   rorNum      UDINT
                   udiNoOf‐    UDINT             Size of the received data buffer
                   Bytes
RETURN                         UDINT             Number of bytes received. 0 indicates that the con‐
                                                 nection was closed or an error occurred

Functional description
The IL_TCPRecv function receives data via a connection created with IL_TCPI‐
nitial. This function does not return until either data was received or an error
occurred.
The reception buffer is created in "pbyValueAdr". The size of the reception
buffer is transmitted in "udiNoOfBytes".
The IL_TCPRecv function receives characters up to the maximum size of the
reception buffer connected. Fewer characters can also be received. If the com‐
plete buffer is always to be filled, the function ⮫ on page is to be used.
After successful transmission, this function returns the number of characters
received. If 0 is returned, the connection was closed before data could be
received. In case of error, the error code is stored to "pudiErrorNum" and the
function returns with a return value of 0.
If no data is received within a second, the function returns with the return
value 0 and stores the error code 16#0000020A in "pudiErrorNum".

Troubleshooting
The function uses the error table CXA_TABLE.
The function returns the following error codes in "pudiErrorNum":
Table 932: Error codes of the IL_TCPRecv
ErrorID                          pudiErrorNum Description
INPUT_RANGE_ERROR                16#0C230006 Input "ValueAdr" is not set
INPUT_RANGE_ERROR                16#0C230006 Input "ValueAdr" is not set

                                                                 TCP        1344

ErrorID                       pudiErrorNum Description
INPUT_INVALID_ERROR           16#0C230202 Invalid socket handle
COMMUNICATION_ERROR           16#0C23020A Timeout. No response from the addressed device (3
                      seconds)
COMMUNICATION_ERROR           16#0C23020E Connection was closed
COMMUNICATION_ERROR           16#0C230211 Socket was closed
Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
codes of the CXA_Table on page 1131.

IL_TCPRecvPacket

Brief description
The IL_TCPRecvPacket function receives data via a connection created with
IL_TCPInitial. This function does not return until either data was received or
an error occurred.

Interface description

Table 933: Interface variables of the IL_TCPRecvPacket function
              Name        Type                Description
VAR_INPUT     udiSocket   UDINT               IL_TCPInitial socket handle
              pbyValueAdr POINTER TO          Initial address of the received data buffer
                          BYTE
              pudiEr‐     POINTER TO          Contains the error code
              rorNum      UDINT
              udiNoOf‐    UDINT               Size of the received data buffer
              Bytes
RETURN                    UDINT               Number of bytes received. 0 indicates that either the
VALUE                                         connection was closed or an error occurred

Functional description
The IL_TCPRecvPacket function receives data via a connection created with
IL_TCPInitial. This function does not return until either data was received or
an error occurred.
The reception buffer is created in "pbyValueAdr". The size of the reception
buffer is transmitted in "udiNoOfBytes".
The IL_TCPRecvPacket function receives characters until the connected recep‐
tion buffer is full.
It returns when the reception buffer is full or a timeout occurred. After suc‐
cessful transmission, this function returns the number of characters received.
If 0 is returned, the connection was closed before data could be received.
In case of error, the error code is stored to "pudiErrorNum" and the function
returns with a return value of 0.

1078 /    ctrlX PLC Engineering
1344      TCP

If no data is received within a second, the function returns with the return
value 0 and stores the error code 16#0000020A in "pudiErrorNum".

Troubleshooting
The function uses the error table CXA_TABLE.
The function returns the following error codes in "pudiErrorNum":
Table 934: Error codes of the IL_TCPRecvPacket
ErrorID                          pudiErrorNum Description
INPUT_RANGE_ERROR                16#0C230006 Input "ValueAdr" is not set
INPUT_RANGE_ERROR                16#0C23000F Input "NoOfBytes" is 0
INPUT_INVALID_ERROR              16#0C230202 Invalid socket handle
COMMUNICATION_ERROR              16#0C23020A Timeout. No response from the addressed device (3
                                              seconds)
COMMUNICATION_ERROR              16#0C230211 Socket was closed
                        Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                        codes of the CXA_Table on page 1131.

IL_TCPClose
Brief description
The function IL_TCPClose closes a connection created with IL_TCPInitial. This
function returns immediately.

Interface description

Table 935: Interface variables of the IL_TCPClose function
                   Name        Type               Description
VAR_INPUT          udiSocket   UDINT              IL_TCPInitial socket handle
                   pudiEr‐     POINTER TO         Contains the error code
                   rorNum      UDINT
RETURN                         BOOL               TRUE: Socket was closed successfully.
                                                  FALSE: Error occurred when the socket was closed.

Functional description
The function IL_TCPClose closes a connection created with IL_TCPInitial. This
function returns immediately.
If an error occurs, the error code is stored to the variable specified in pudiEr‐
rorNum.

Troubleshooting
The function uses the error table CXA_TABLE.
The function returns the following error codes in "pudiErrorNum":

                                                                 UDP         1344

Table 936: Error codes of the IL_TCPClose
ErrorID                        pudiErrorNum Description
INPUT_INVALID_ERROR            16#0C230202 Invalid socket handle
COMMUNICATION_ERROR            16#0C230211 Socket was closed
                     Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                     codes of the CXA_Table on page 1131.

## 35.3 UDP

### 35.3.1 Introduction and overview

UDP is a connection-free IP protocol. In contrast to the TCP protocol, there
is no connection establishment prior to the actual data exchange. Communica‐
tion is package-based. Received data packages are stored in the buffer, but
not merged. Every reception call takes exactly one package from the queue.
Received UDP data packages are not acknowledged. It is therefore not pos‐
sible to identify lost packages. UDP is therefore suitable for cyclic data trans‐
mission, in which data of possibly lost packages is updated by later packages.
The following flow chart shows a typical mono-directional UDP client server
configuration. The server opens a UDP socket at a given port while the UDP
port of the client is unknown. In this configuration, the client can only send
but not receive.

The following flow chart shows a typical bidirectional UDP server-server con‐
figuration. In this configuration, both communication partners can send and
receive data packages, as the respective target port is known.

1080 /    ctrlX PLC Engineering
1344      UDP

UDP client example
The following example shows a simple UDP client, which cyclically sends a
data package once per second to a defined UDP server IP and port pair.
Typ-Definition einer UDP-Paket Datenstruktur:
TYPE UDP_PACKET :
STRUCT
  Sequence: UINT;
  State: INT;
  InfoTxt: STRING[20];
END_STRUCT
END_TYPE

Einfaches UDP-Clientprogramm (Deklaration)
(* This simple Example implements an UDP client. It sends an UDP packet once a second. *)
(* the packet can contain all process data and even strings.                           *)
(* A sequence number is implemented to allow for a missing data packets check          *)

PROGRAM PLC_PRG
VAR CONSTANT
  (* communication settings *)
  strUDPServer: STRING := '192.168.1.254'; (* put in your remote UDP server IP here *)
  uiPort: UINT := 2323; (* remote UDP server port *)
END_VAR

VAR
 (* used function blocks *)
  fbUDPSocket: IL_UDPSocketAsync;
  fbUDPSend: IL_UDPSendtoAsync;

 (* variables *)
  udiSocket: UDINT; (* socket handle *)
  iCount: INT; (* send loop counter *)

 (* UDP packet data to send *)
  stUDPPacket: UDP_PACKET := (Sequence:=0, State:=1, InfoTxt:='Device Ready');
END_VAR

Einfaches UDP-Clientprogramm (Implementation)
(* check for UDP socket *)IFfbUDPSocket.Done = FALSETHEN(* no UDP socket yet => create one
*)fbUDPSocket(Enable:=TRUE, Server:=FALSE, Socket=>udiSocket);

  IFfbUDPSocket.Error = TRUETHEN(* an error occurred => reset *)fbUDPSocket(Enable:=FALSE, Socket=>udiSocket);
  END_IFELSEIFiCount <= 0THEN(* every 100 loops send UDP packet (10ms task * 100 loops = 1s) *)IFfbUDPSend.Active
= FALSETHEN(* not already about to send => increase sequence number of UDP packet *)stUDPPacket.Sequence :=
stUDPPacket.Sequence + 1;
    END_IF(* send the packet *)fbUDPSend(Enable:=TRUE, Socket:=udiSocket,
ValueAdr:=ADR(stUDPPacket), NoOfBytes:=SIZEOF(stUDPPacket),

                                                                        UDP           1344

Address:=strUDPServer, Port:=uiPort);

   IFfbUDPSend.Done = TRUETHEN(* packet send => restart counter *)fbUDPSend(Enable:=FALSE);
iCount := 100;
   ELSIFfbUDPSend.Error = TRUETHEN(* an error occurred => reset everything *)fbUDPSend(Enable:=FALSE);
fbUDPSocket(Enable:=FALSE);
   END_IFELSE(* decrease loop counter *)iCount := iCount - 1;
 END_IFEND_IF

UDP server, synchronous transfer
A UDP server is implemented in the following example. The UDP server
receives data from a client and sends data to this client.
The connection is then closed and the socket is available.
The program requires the libraries "CXA_SocketComm" and "cmperrors".

−      The function block IL_UDPInitial may not be called cyclically. The function
       block returns from the call, once the connection is established.
−      IL_UDPInitial generates a socket upon each call. Consider the limitation of
       the number of sockets.
−      If the error "ERR_SOCK_WOULDBLOCK" occurs while sending or receiving
       data, the "Send" buffer is either full or the "Receive" buffer is still empty.
       The error "ERR_SOCK_WOULDBLOCK" can thus be ignored and the call
       repeated.

Deklaration des Programms
PROGRAM UDPSync_Server_Prog
VAR
  arRecvData: ARRAY[1..10] OF BYTE;
  arSendData: ARRAY[1..10] OF BYTE;

  uiState:           UINT := 0;
  i:                 INT;
  udiResult:         UDINT;
  bResult:           BOOL;
  udiSocket:         UDINT;
  udiErrorNum:       UDINT;
  uiClient_Port:     UINT;
  strClient_Address: STRING;
  udiResult_Latched: UDINT;
  udiErrorNum_Latched: UDINT;
END_VAR

VAR CONSTANT
  STATE_INIT:    UINT := 0;
  STATE_SERVER: UINT := 1;
  STATE_RECEIVE: UINT := 2;
  STATE_SEND:    UINT := 3;
  STATE_CLOSE:   UINT := 4;
  STATE_ERROR:   UINT := 5;
  STATE_FINISH: UINT := 6;
END_VAR

Implementation
//The following program implements an UDP Server
//the UDP Server receives data from a Client
//then the Server sends data back to the Client
//after that close connection and release socket

CASE uiState OF

//Initialize senddata
STATE_INIT:
    FOR i := 1 TO 10 BY 1 DO
arSendData[i] := arSendData[i] + 1;
    END_FOR
uiState := STATE_SERVER;

//UDP Server
STATE_SERVER:
  udiResult:= IL_UDPInitial(bServer:= TRUE, strAdress:= '', uiPort:= 6000, pudiSocket:= ADR(udiSocket),
    pudiErrorNum:= ADR(udiErrorNum));

  //if no error, go to next state, else go to the error state

1082 /    ctrlX PLC Engineering
1344      UDP

  IF udiResult = 0 AND udiErrorNum = 0 THEN
uiState := STATE_RECEIVE;
 ELSE
uiState := STATE_CLOSE;
  END_IF

 //Receive data from Client
STATE_RECEIVE:
  udiResult:= IL_UDPRecvfrom(udiSocket:= udiSocket, pbyValueAdr:= ADR(arRecvData),
      pstSendSockAddr:= ADR(strClient_Address), puiSendPort:= ADR(uiClient_Port),
      pudiErrorNum:= ADR(udiErrorNum), udiNoOfBytes:= SIZEOF(arRecvData));

  //go to the next state if the receive process is finished without error
  IF udiResult <> 0 AND udiErrorNum = Errors.ERR_OK THEN
uiState := STATE_SEND;
  END_IF

  //if error is 'wouldblock', try it again; else go to the error state
  IF udiErrorNum <> 0 THEN
    IF udiErrorNum = Errors.ERR_SOCK_WOULDBLOCK THEN
RETURN;
    ELSE
uiState := STATE_CLOSE;
    END_IF
  END_IF

//Send data to client
STATE_SEND:
    udiResult:= IL_UDPSendto(udiSocket:= udiSocket, pbyValueAdr:= ADR(arSendData),
      strAdress:= strClient_Address, uiPort:= uiClient_Port,
      pudiErrorNum:= ADR(udiErrorNum), udiNoOfBytes:= SIZEOF(arSendData));

    //go to the next state if the send process is finished without error
 IF udiResult <> 0 AND udiErrorNum = Errors.ERR_OK THEN
    uiState := STATE_CLOSE;
  END_IF

  //if error is wouldblock, try it again; else go to the error state
  IF udiErrorNum <> 0 THEN
    IF udiErrorNum = Errors.ERR_SOCK_WOULDBLOCK THEN
RETURN;
    ELSE
uiState := STATE_CLOSE;
    END_IF
  END_IF

//Release Socket
STATE_CLOSE:
   bResult := IL_UDPClose(udiSocket:= udiSocket, pudiErrorNum:= ADR(strClient_Address));

    //store error information
    IF udiErrorNum <> 0 THEN
udiErrorNum_Latched := udiErrorNum;
    END_IF
    uiState := STATE_FINISH;

   //store error information
STATE_ERROR:
    udiResult_Latched := udiResult;
    udiErrorNum_Latched := udiErrorNum;
    //go to the close state to break the connection and release the socket
    uiState := STATE_CLOSE;

//Finish, do nothing
STATE_FINISH:
;
END_CASE

UDP client, synchronous transfer
A UDP client is implemented in the following example. The UDP client sends
data to a server and then receives data from this server.
The connection is then closed and the socket is available.
The program requires the libraries "CXA_SocketComm" and "cmperrors".

                                                                        UDP              1344

−      The function block IL_UDPInitial may not be called cyclically. The function
       block returns from the call, once the connection is established.
−      IL_UDPInitial generates a socket upon each call. Consider the limitation of
       the number of sockets.
−      If the error "ERR_SOCK_WOULDBLOCK" occurs while sending or receiving
       data, the "Send" buffer is either full or the "Receive" buffer is still empty.
       The error "ERR_SOCK_WOULDBLOCK" can thus be ignored and the call
       repeated.
Deklaration des Programms
PROGRAM UDPSync_Client_Prog
VAR

  arRecvData: ARRAY[1..10] OF BYTE;
  arSendData: ARRAY[1..10] OF BYTE;

  uiState:           UINT := 0;
  i:                 INT;
  udiResult:         UDINT;
  bResult:           BOOL;
  udiSocket:         UDINT;
  udiErrorNum:       UDINT;
  uiRecv_Port:       UINT;
  strRecv_Address:   STRING;
  udiResult_Latched: UDINT;
  udiErrorNum_Latched: UDINT;
END_VAR

VAR CONSTANT
  STATE_INIT:    UINT := 0;
  STATE_CLIENT: UINT := 1;
  STATE_RECEIVE: UINT := 2;
  STATE_SEND:    UINT := 3;
  STATE_CLOSE:   UINT := 4;
  STATE_ERROR:   UINT := 5;
  STATE_FINISH: UINT := 6;
END_VAR

Implementation
//The following program implements a UDP Client
//the UDP Client sends data to a Server
//then it receives data from the Server
//after that close the connection and release socket

CASE uiState OF

//Initialize senddata
STATE_INIT:
    FOR i := 1 TO 10 BY 1 DO
arSendData[i] := arSendData[i] + 1;
    END_FOR
    uiState := STATE_CLIENT;

//UDP Client
STATE_CLIENT:
  udiResult := IL_UDPInitial(bServer:= FALSE, strAdress := '192.168.42.11', uiPort:= 6000,
     pudiSocket:= ADR(udiSocket), pudiErrorNum:= ADR(udiErrorNum));

 //if no error, go to next state, else go to the error state
  IF udiResult = 0 AND udiErrorNum = Errors.ERR_OK THEN
uiState := STATE_SEND;
    ELSE
uiState := STATE_ERROR;
  END_IF

//Send data to Server
STATE_SEND:
    udiResult:= IL_UDPSendto(udiSocket:= udiSocket, pbyValueAdr:= ADR(arSendData),
      strAdress:= '192.168.42.11', uiPort:= 6000,
      pudiErrorNum:= ADR(udiErrorNum) , udiNoOfBytes:= SIZEOF(arSendData));

 //go to the next state if the send process is finisched without error
    IF udiResult <> 0 AND udiErrorNum = Errors.ERR_OK THEN
uiState := STATE_RECEIVE;
  END_IF

 //if error is wouldblock, try it again; else go to the error state
  IF udiErrorNum <> 0 THEN
    IF udiErrorNum = Errors.ERR_SOCK_WOULDBLOCK THEN

1084 /    ctrlX PLC Engineering
1344      UDP

RETURN;
    ELSE
uiState := STATE_ERROR;
    END_IF
  END_IF

//Receive data from Server
STATE_RECEIVE:
    udiResult:= IL_UDPRecvfrom(udiSocket:= udiSocket, pbyValueAdr:= ADR(arRecvData),
          pstSendSockAddr:= ADR(strRecv_Address), puiSendPort:= ADR(uiRecv_Port),
          pudiErrorNum:= ADR(udiErrorNum), udiNoOfBytes:= SIZEOF(arRecvData));

 //go to the next state if the receive process is finisched without error
  IF udiResult <> 0 AND udiErrorNum = Errors.ERR_OK THEN
uiState := STATE_CLOSE;
  END_IF

 //if error is wouldblock, try it again; else go to the error state
  IF udiErrorNum <> 0 THEN
    IF udiErrorNum = Errors.ERR_SOCK_WOULDBLOCK THEN
RETURN;
    ELSE
uiState := STATE_ERROR;
    END_IF
  END_IF

//Release socket
STATE_CLOSE:
   bResult := IL_UDPClose(udiSocket:= udiSocket, pudiErrorNum:= ADR(udiErrorNum));

 //store error information
    IF udiErrorNum <> 0 THEN
udiErrorNum_Latched := udiErrorNum;
    END_IF
    uiState := STATE_FINISH;

 //store error information
STATE_ERROR:
    udiResult_Latched := udiResult;
    udiErrorNum_Latched := udiErrorNum;
 //go to the close state to break the connection and release the socket
    uiState := STATE_CLOSE;

//Finish, do nothing
STATE_FINISH:
;
END_CASE

### 35.3.2 Asynchronous function blocks

Introduction and overview
The UDP asynchronous function blocks are used in cyclic tasks and have to
be called cyclically. Normally, multiple calls are required to complete an oper‐
ation.
A function block starts with a rising edge at "Enable" and operates until either
"Done" or "Error" is TRUE or "Enable" is reset. To start a new operation, reset
"Enable" and set it again.
  A new UDP socket can be set up and closed via the ⮫ Chapter IL_UDPSocketA‐
  sync on page 1085 function block.
  If "Server" is set to FALSE when the socket is created, the socket cannot
  receive any data.
  After the socket was established, data can be exchanged with ⮫ Chapter
  IL_UDPSendtoAsync on page 1086 and ⮫ Chapter IL_UDPRecvfromAsync
  on page 1088.
  UDP is a package-based protocol that guarantees neither the order nor the
  consistency of the data packages transmitted.
  Packages can be lost during transmission.
  Received data in the received order is handled in a queue.
  Each call by IL_UDPRecvfromAsync or IL_UDPRecvfrom returns exactly one
  package from the queue.

                                                                 UDP        1344

IL_UDPSocketAsync
Brief description
The function block IL_UDPSocketAsync manages either a UDP server or a UDP
client depending on the "Server" input.

Interface description

Table 937: Interface variables of the IL_UDPSocketAsync function block
              Name           Type    Description
VAR_INPUT     Enable         BOOL    Starts at a rising edge
                                     Binary outputs are reset at a falling edge
           Server      BOOL          TRUE: UDP server is created
                                     FALSE: UDP client is created
           Address     STRING        If "Server" is set, this input is not used and the own
                                     IP address is used
                                     If "Server" is FALSE, this input contains the IP
                                     address of the device to be connected
           Port        UINT          The UDP port on which incoming data packages are
                                     expected or to which data packages are to be sent
VAR_OUTPUT InOperation BOOL          TRUE indicates that the function block is busy with
                                     its actual task
           Shutdown    BOOL          TRUE indicates that the function block is currently in
                                     a defined final state
           Error       BOOL          TRUE indicates an error
           ErrorID     ⮫ ERROR_CODE Error class
           ErrorIdent  ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
                       T             on page 1086 )
           Socket      UDINT         Contains the socket handle of the new socket

Table 938: Min./max. and default values of the IL_UDPSocketAsync function block inputs
Name           Type           Min. value      Max. value    Default value   Effective
Enable         BOOL                                         FALSE           Continuous
Server         BOOL                                         FALSE           Rising edge at Enable
Address        STRING                                       ''              Rising edge at Enable
Port           UINT           0               65535         0               Rising edge at Enable

Functional description
The function block IL_UDPSocketAsync manages either a UDP server or a UDP
client depending on the "Server" input. Processing starts at a rising edge at
"Enable". The function block has to be called cyclically until "Done" or "Error"
are TRUE.

1086 /    ctrlX PLC Engineering
1344      UDP

In Server mode, the function block opens a socket at the UDP port speci‐
fied in "Port". The socket handle belonging to the socket is displayed at the
"Socket" output and the "Done" output is set. While the socket is created, the
"Active" output is set.
In "Client" mode, a socket is created, but not connected to a port. Accord‐
ingly, the port number is unknown and no data can be received. After a suc‐
cessful socket creation, the socket handle is displayed at the "Socket" output
and the "Done" output is set. While the socket is created, the "Active" output
is set.
In "Client" mode, UDP packages can only be sent, but not received.

In case of error, the "Error" output is set. SOCKET_INVALID is displayed at the
"Socket" output. The error class and the exact error code can be read at the
"ErrorID" and "ErrorIdent" outputs.
If "Enable" is set to FALSE before "Done" is TRUE, no socket is created and
all internal resources are enabled. If "Enable" is set to FALSE after the socket
has been created, the socket is closed. Possible errors while closing are han‐
dled internally and not issued at the error outputs. After "Enable" was set to
FALSE, the "Socket" output is set to SOCKET_INVALID.
The "Active" output can be used as timeout indicator during connection setup.
Typical timeouts for connection setup range from 2 to 10 seconds.

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 939: Error codes of the IL_UDPSocketAsync
ErrorID              Additional1  Additional2 Description
OTHER_ERROR         16#0A0F.0101 16#0C23.100 Socket could not be created
                                       1
OTHER_ERROR         16#0A0F.0101 16#0C23.100 Error when setting the I/O mode
                                       2
OTHER_ERROR         16#0A0F.0101 16#0C23.100 Could not connect socket to port
                                       3
INPUT_INVALID_ERROR 16#0A0F.0101 16#0C23.020 Destination address invalid
                                       8
COMMUNICA‐          16#0A0F.0101 16#0C23.020 No route to target device
TION_ERROR                             C
                     Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                     codes of the CXA_Table on page 1131.

IL_UDPSendtoAsync
Brief description
The function block IL_UDPSendtoAsync sends data packages via a socket cre‐
ated with⮫ Chapter IL_UDPSocketAsync on page 1085.

                                                                 UDP        1344

Interface description

Table 940: Interface variables of the IL_UDPSendtoAsync function block
              Name           Type              Description
VAR_INPUT     Execute        BOOL              Starts at a rising edge
              Socket         UDINT             IL_UDPSocketAsync socket handle
              ValueAdr       POINTER TO        Initial address of data to be sent
                             BYTE
           Address           STRING       Target IP address of the receiver (e.g '192.168.1.2')
           Port              UINT         UDP reception port of remote host
           NoOfBytes         UDINT        Number of characters to be sent
VAR_OUTPUT Done              BOOL         TRUE indicates that the data package was success‐
                                          fully sent
              Active         BOOL         TRUE indicates that the function block sends data
              Error          BOOL         TRUE indicates an error
              ErrorID        ⮫ ERROR_CODE Error class
              ErrorIdent     ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
                             T             on page 1088 )
              NoOfSend‐      UDINT         Number of bytes sent. 0 indicates that an error
              Bytes                        occurred or that the socket was closed

Table 941: Min./max. and default values of the IL_UDPSendtoAsync function block inputs
Name           Type            Min. value      Max. value  Default value Applied
Execute        BOOL                                        FALSE         Continuous
Socket         UDINT           0               16#FFFFFFFF SOCKET_INVA Rising edge at “Exe‐
                                                           LID           cute”
ValueAdr       POINTER TO                                  0             Rising edge at “Exe‐
               BYTE                                                      cute”
Address        STRING                                      ''            Rising edge at “Exe‐
                                                                         cute”
Port           UINT            1               65535       0             Rising edge at “Exe‐
                                                                         cute”
NoOfBytes      UDINT           0               16#FFFFFFFF 0             Rising edge at “Exe‐
                                                                         cute”

Functional Description
The function block IL_UDPSendtoAsync sends data packages via a socket cre‐
ated with⮫ Chapter IL_UDPSocketAsync on page 1085. Transmission begins at
a rising edge at "Execute". The function block has to be called cyclically until
"Done" or "Error" is TRUE.

1088 /    ctrlX PLC Engineering
1344      UDP

The buffer to be sent is applied to the "ValueAdr" input. The number of char‐
acters to be sent is applied at the "NoOfBytes" input.
For some controls, the maximum size of UDP data packages is limited to 1430
bytes.
If "Execute" is reset before "Done" is TRUE, the transmission is interrupted. No
data is sent and the "NoOfSentBytes" output is 0.
The "Active" output is set during transmission of the data package. "Active"
can be used as a timeout indicator. Typical transmission timeouts range from
1 to 2 seconds. During transmission ("Active" is TRUE), the number of bytes
sent can be read at the "NoOfSentBytes" output. Generally, the entire package
is sent in one call.
The IP address of the remote host and the target port has to be specified in
the "Address" and "Port" inputs.

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 942: IL_UDPSendtoAsync error codes
ErrorID              Additional1  Additional2 Description
INPUT_RANGE_ERROR   16#0A0F.0101 16#0C23.000 ValueAdr is not set
                                       6
INPUT_RANGE_ERROR 16#0A0F.0101 16#0C23.000 NoOfBytes is 0
                                       F
INPUT_INVALID_ERROR 16#0A0F.0101 16#0C23.020 Socket handle invalid
                                       2
COMMUNICA‐          16#0A0F.0101 16#0C23.020 Target address invalid
TION_ERROR                             8
COMMUNICA‐          16#0A0F.0101 16#0C23.020 No network path to target device found
TION_ERROR                             C
                     Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                     codes of the CXA_Table on page 1131.

IL_UDPRecvfromAsync
Brief description
The function block IL_UDPRecvfromAsync sends data packages via a socket
created with ⮫ Chapter IL_UDPSocketAsync on page 1085.

Interface description

                                                                UDP         1344

Table 943: Interface variables of the IL_UDPRecvfromAsync function block
              Name            Type              Description
VAR_INPUT     Execute         BOOL              Starts at a rising edge
              Socket          UDINT             IL_UDPSocketAsync or IL_UDPInitialAsync socket
                                                handle
              ValueAdr        POINTER TO        Initial address of the received data buffer
                              BYTE
           NoOfBytes          UDINT        Size of the received data buffer
VAR_OUTPUT Done               BOOL         TRUE indicates that the data package was received
                                           successfully

Active          BOOL         TRUE indicates that the function block is waiting for
                    incoming data packages
Error           BOOL         TRUE indicates an error
ErrorID         ⮫ ERROR_CODE Error class
ErrorIdent      ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
       T             on page 1090 )
SocketAddr      SOCKINFO      IP address and port number of the transmitter
NoOfRec‐        UDINT         Number of bytes copied to the reception data buffer
Bytes                         0 indicates that either the socket was closed or an
                     error occurred

Table 944: Min./max. and default values of the IL_UDPRecvfromAsync function block inputs
Name           Type             Min. value      Max. value  Default value Applied
Execute        BOOL                                         FALSE         Continuous
Socket         UDINT            0               16#FFFFFFFF SOCKET_INVA Rising edge at “Exe‐
                                                            LID           cute”
ValueAdr       POINTER TO                                   0             Rising edge at “Exe‐
               BYTE                                                       cute”
NoOfBytes      UDINT            0               16#FFFFFFFF 0             Rising edge at “Exe‐
                                                                          cute”

Functional Description
The function block IL_UDPRecvAsync sends data packages via a socket created
with ⮫ Chapter IL_UDPSocketAsync on page 1085.
Transmission begins at a rising edge at "Execute".
The function block has to be called cyclically until "Done" or "Error" is TRUE.
If "Execute" is reset before "Done" is TRUE, the transmission is canceled. In
case of such an abort, no data is accepted. "NoOfRecBytes" is hence 0.
The "Active" output is set during data transmission. "Active" can be used as a
timeout indicator.
Typical reception timeouts range from 1 to 2 seconds.

1090 /    ctrlX PLC Engineering
1344      UDP

Time diagram

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 945: Error codes of the IL_UDPRecvfromAsync
ErrorID              Additional1  Additional2 Description
INPUT_RANGE_ERROR   16#0A0F.0101 16#0C23.000 “ValueAdr” is not set
                                       6
INPUT_RANGE_ERROR 16#0A0F.0101 16#0C23.000 “NoOfBytes” is 0
                                       F
INPUT_INVALID_ERROR 16#0A0F.0101 16#0C23.020 Socket handle invalid
                                       2
                     Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                     codes of the CXA_Table on page 1131.

### 35.3.3 Synchronous functions

Introduction and overview
The synchronous UDP functions are implemented as blocking calls. Thus, they
do not return until the operation is completed or an error occurred. These
functions are only to be used in free running tasks.
IL_UDPInitial is used to connect a new UDP socket and returns a socket
handle.
After the successful creation of the UDP socket, data can be sent and received
with IL_UDPSendto and IL_UDPRecvfrom.
If "bServer" is set to FALSE when the socket is created, the socket cannot
receive any data
IL_UDPClose closes a UDP socket and enables the socket handle.
UDP is a package-based protocol that guarantees neither the order nor the
consistency of the data packages transmitted. Packages can be lost during
transmission.
Received data in the received order is managed in a queue.
Each call by IL_UDPRecvfromAsync or IL_UDPRecvfrom returns exactly one
package from the queue.

                                                                  UDP        1344

IL_UDPInitial
Brief description
The IL_UDPInitial function establishes either a UDP server or a UDP client
depending on the "bServer" parameter.

Interface description

Table 946: Interface variables of the IL_UDPInitial Interface function
              Name            Type               Description
VAR_INPUT     bServer         BOOL               TRUE: TCP server is created.
                                                 FALSE: UDP client is created.
              strAddress      STRING             If "bServer" is set, this input is not used and the
                                                 own IP address is used. If "bServer" is FALSE, this
                                                 input contains the IP address of the device to be
                                                 connected
              uiPort          UINT               The UDP port at which incoming data packages are
                                                 expected or to which data packages are to be sent
              pudiSocket      POINTER TO         Contains the socket handle of the new socket
                              UDINT
              pudiEr‐         POINTER TO         Contains the error code
              rorNum          UDINT
RETURN                        UDINT              0 if the socket was successfully created; otherwise
                                                 INVALID_SOCKET

Functional description
The IL_UDPInitial function establishes either a UDP server or a UDP client
depending on the "bServer" parameter.
In server mode, the function opens a socket at the UDP port given in "uiPort".
The socket handle belonging to the socket is displayed in "pudiSocket" and
the function returns with the return value 0.
In client mode, a socket is created but not connected to a port. Accordingly,
the port number is unknown and no data can be received. After a successful
socket creation, the socket handle is displayed in "pudiSocket" and the func‐
tion returns with the return value 0.
In client mode, UDP packages can only be sent but not received.

If an error occurs, the function returns with SOCKET_INVALID and stores the
error code in "pudiErrorNum".

Troubleshooting
The function uses the error table CXA_TABLE.
The function returns the following error codes in "pudiErrorNum":

1092 /    ctrlX PLC Engineering
1344      UDP

Table 947: Error codes of the IL_UDPInitial
ErrorID                           pudiErrorNum    Description
OTHER_ERROR                       16#0C231001     Socket could not be created
OTHER_ERROR                       16#0C231002     Error when setting I/O mode
OTHER_ERROR                       16#0C231003     Could not connect socket to port
INPUT_INVALID_ERROR               16#0C230208     Target address invalid
COMMUNICATION_ERROR               16#0C23020C     No network path to target device found
                        Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                        codes of the CXA_Table on page 1131.

IL_UDPSendto
     Brief description
     The IL_UDPSendto function sends a data package via a socket created with
     IL_UDPInitial. This function does not return until either all data was trans‐
     mitted or an error occurred.

     Interface description

Table 948: Interface variables of the IL_UDPSendto function
                   Name        Type              Description
VAR_INPUT          udiSocket   UDINT             IL_UDPInitial socket handle
                   pbyValueAdr POINTER TO        Initial address of data to be sent
                               BYTE
                   strAddress  STRING            Target IP address of the receiver (e.g '192.168.1.2')
                   uiPort      UINT              UDP reception port of remote host
                   pudiEr‐     POINTER TO        Contains the error code
                   rorNum      UDINT
                   udiNoOf‐    UDINT             Number of characters to be sent
                   Bytes
RETURN                         UDINT             Number of bytes actually sent. 0 indicates that
                                                 either the connection was closed or an error
                                                 occurred.

     Functional description
     The IL_UDPSendto function sends a data package via a socket created with
     IL_UDPInitial. This function does not return until either all data was trans‐
     mitted or an error occurred.
     The buffer to be sent is created in "pbyValueAdr". The number of characters to
     be sent is transferred in "udiNoOfBytes".

                                                                UDP         1344

After successful transmission, this function returns the number of characters
transmitted. If 0 is returned, the connection was closed before the data
packet could be sent. In case of error, the error code is stored to "pudiEr‐
rorNum" and the function returns with a return value of 0.

Troubleshooting
The function uses the error table CXA_TABLE.
The function returns the following error codes in "pudiErrorNum":
Table 949: Error codes of the IL_UDPSendto
ErrorID                        pudiErrorNum    Description
INPUT_RANGE_ERROR              16#0C230006     Input "ValueAdr" is not set

INPUT_RANGE_ERROR              16#0C23000F     Input "NoOfBytes" is 0
INPUT_INVALID_ERROR            16#0C230202     Invalid socket handle
COMMUNICATION_ERROR            16#0C230208     Target address invalid
COMMUNICATION_ERROR            16#0C23020C     No network path to target device found
Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
codes of the CXA_Table on page 1131.

IL_UDPRecvfrom
Brief description
The function IL_UDPRecvfrom receives data packages via a socket created with
IL_UDPInitial. This function does not return until either a data package was
received or an error occurred.

Interface description

Table 950: Interface variables of the IL_UDPRecvfrom function
              Name        Type                Description
VAR_INPUT     udiSocket   UDINT               IL_UDPInitial socket handle
              pbyValueAdr POINTER TO          Initial address of the received data buffer
                          BYTE
              pstrSend‐   POINTER TO          IP address of the transmitter
              SockAddr    STRING
              puiSendPort POINTER TO          Port number of the transmitter
                          UINT
              pudiEr‐     POINTER TO          Contains the error code
              rorNum      UDINT
              udiNoOf‐    UDINT               Size of the received data buffer
              Bytes
RETURN                    UDINT               Number of bytes received. 0 indicates that the either
                                              the socket was closed or an error occurred

1094 /    ctrlX PLC Engineering
1344      UDP

Functional description
The function IL_UDPRecvfrom receives data packages via a socket created with
IL_UDPInitial. This function does not return until either a data package was
received or an error occurred.
The reception buffer is created in "pbyValueAdr". The size of the reception
buffer is transmitted in "udiNoOfBytes".
After successful transmission, this function returns the number of characters
received. If 0 is returned, the socket has been closed before a data package
could be received. In case of error, the error code is stored to "pudiErrorNum"
and the function returns with a return value of 0.
If no data is received within a second, the function returns with the return
value 0 and stores the error code 16#0000020A in "pudiErrorNum".

Troubleshooting
The function uses the error table CXA_TABLE.
The function returns the following error codes in "pudiErrorNum":
Table 951: Error codes of the IL_UDPRecvfrom
ErrorID                           pudiErrorNum    Description
INPUT_RANGE_ERROR                 16#0C230006     Input "ValueAdr" is not set
INPUT_RANGE_ERROR                 16#0C23000F     Input "NoOfBytes" is 0
INPUT_INVALID_ERROR               16#0C230202     Invalid socket handle
                        Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                        codes of the CXA_Table on page 1131.

IL_UDPClose
Brief description
The IL_UDPClose function closes a socket created with IL_UDPInitial. This
function returns immediately.

Interface description

Table 952: Interface variables of the IL_UDPClose function
                   Name        Type              Description
VAR_INPUT          udiSocket   UDINT             IL_UDPInitial socket handle
                   pudiEr‐     POINTER TO        Contains the error code
                   rorNum      UDINT
RETURN                         BOOL              TRUE: Socket was closed successfully
                                                 FALSE: Error occurred when the socket was closed

Functional description
The IL_UDPClose function closes a socket created with IL_UDPInitial. This
function returns immediately.

                                                                ICMP        1344

Troubleshooting
The function uses the error table CXA_TABLE.
The function returns the following error codes in "pudiErrorNum":
Table 953: Error codes of the IL_UDPClose
ErrorID                        pudiErrorNum Description
INPUT_INVALID_ERROR            16#0C230202 Invalid socket handle
COMMUNICATION_ERROR            16#0C230211 Socket was closed
                     Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                     codes of the CXA_Table on page 1131.

## 35.4 ICMP

### 35.4.1 Introduction and overview

The Internet Control Message Protocol (ICMP) exchanges information and
error messages in networks via internet protocol (IP). It also provides a mech‐
anism for simple testing of IP devices. This ping sends a short package to a
remote host. The remote host responds with the same content. If the receiver
receives the package from the remote host, the ping was successful.

### 35.4.2 Asynchronous function blocks

IL_PingAsync
Brief description
The function block IL_PingAsync performs an ICMP ping to the specified IP
address and waits for the response. The ping runtime is displayed at the
"EchoTime" output.

Interface description

Table 954: Interface variables of the IL_PingAsync function block
           Name              Type         Description
VAR_INPUT Execute            BOOL         Rising edge starts the ping
           Address           STRING       IP address of the device to be checked
           Timeout           TIME         Maximum ping runtime
VAR_OUTPUT Done              BOOL         TRUE: Ping was performed successfully.
           Active            BOOL         TRUE: Ping is currently performed.
           Error             BOOL         An error occurred.
           ErrorID           ⮫ ERROR_CODE Error class
              ErrorIdent     ⮫ ERROR_STRUC For detailed error information (refer to ⮫ on page )
                             T
              EchoTime       TIME          Measured ping runtime

1096 /    ctrlX PLC Engineering
1344      ICMP

Table 955: Min./max. and default values of the inputs of the IL_PingAsync function block
Name               Type              Min. value        Max. value   Default value Applied
Execute            BOOL                                                FALSE      Continuous
Address            STRING                                                ""       Rising edge at “Exe‐
                                                                                  cute”
Timeout            TIME                  0s             N. def.         3s        Rising edge at “Exe‐
                                                                                  cute”

Functional description
This function block serves to check the availability of a device in the Ethernet.
At a rising edge at "Execute", the IL_PingAsync function block sends a short
ICMP ping package to the Ethernet device specified in "Address".
Providing this device is reachable and supports the ICMP protocol, this device
returns a ping with the same package content to the transmitter.
The runtime is measured by the function block and issued at the "EchoTime"
output.
If the device does not respond within the time specified at the "Timeout”
input, an error message is generated at the "Error" outputs. "Active" is set
when the function block is waiting for response. Once the response is
received, "Done" is set and "EchoTime" contains the runtime.
The "EchoTime" output has the resolution of the calling task. The minimum
"EchoTime" of a cyclic 2 ms task is thus 2 ms.

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 956: Error codes generated by IL_PingAsync
ErrorID             Additional1  Additional2 Description
INPUT_INVALID_ERROR 16#0A0F0101 16#0C230208 IP address is invalid
COMMUNICA‐          16#0A0F0101 16#0C23020A Timeout. No response from the addressed
TION_ERROR                                   device (3 seconds)
COMMUNICA‐          16#0A0F0101 16#0C230211 Socket was closed
TION_ERROR
                          Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                          codes of the CXA_Table on page 1131.

### 35.4.3 Synchronous functions

IL_Ping
Brief description
The IL_Ping function sends an ICMP ping to the specified IP address and
waits for the response. The function returns the runtime of the ping.

Interface description

                                                                  FTP         1344

Table 957: Interface variables of the IL_Ping function
              Name           Type             Description
VAR_INPUT     strAddress     STRING           IP address of the device to be checked
              pudiEr‐        POINTER TO       Contains the error code
              rorNum         UDINT
              tTimeout       TIME             Maximum ping runtime
RETURN                       TIME             Measured ping runtime

 Functional Description
 This function checks the availability of a device in the Ethernet.

 Upon call, the IL_Ping function sends a short ICMP ping package to the
 Ethernet device specified in "Address". Providing this device is reachable and
 supports the ICMP protocol, this device returns a ping with the same package
 content to the transmitter. The runtime is measured by the function and
 stored in the return value. If the device does not respond within the time
 given at the "Timeout" input, an error message is written to "pudiErrorNum".
 The function operates synchronously. Thus, it returns when either the device
 responded, there was a timeout or another error occurred.

 Troubleshooting
The function uses the error table CXA_TABLE.
The function returns the following error codes in "pudiErrorNum":
Table 958: Error codes generated by IL_Ping
ErrorID                        pudiErrorNum Description
COMMUNICATION_ERROR            16#0C23020A Timeout. No response from the addressed device
                                            (3 seconds)
COMMUNICATION_ERROR            16#0C23020B Remote host not found
COMMUNICATION_ERROR            16#0C23020C No network path to target device found
                     Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
                     codes of the CXA_Table on page 1131.

## 35.5 FTP

### 35.5.1 Introduction and overview

 The File Transfer Protocol (FTP) transfers files between two network devices
 based on the TCP protocol. An FTP client connects to an FTP server running
 on the target computer. Once the connection is established, data can be read
 and written.

### 35.5.2 Asynchronous function blocks

Introduction and overview
FTP (File Transfer Protocol) implements the transfer of individual files via IP.
It is based on the TCP protocol.
To transfer a file, an FTP client has to log into an FTP server before. Subse‐
quently, the file can be transferred either from the server to the client (get)
or from the client to the server (put). Usually, the FTP server waits for an
incoming client connection at the TCP port 21.
Data is transmitted in passive mode. This bypasses possible problems due to
firewalls and NAT (Network Address Translation).

1098 /    ctrlX PLC Engineering
1344      FTP

      If the FTP server does not support the passive mode, active mode is used.
      Data is always transmitted in binary code. As a result, the line-end identifier is
      not compiled in texts between Windows- and Unix-based systems.

IL_FTPGetAsync
      Brief description
      The function block IL_FTPGetAsync retrieves a file from an FTP server and
      stores it to a data area.

      Interface description

Table 959: Interface variables of the IL_FTPGetAsync function block
                   Name         Type               Description
VAR_INPUT          Execute      BOOL               Function block processing enabled (once, edge-con‐
                                                   trolled)
                   Address      STRING             Name or IP address of FTP server
                   Login        STRING             Login on FTP server; empty means anonymous
                                                   access
                   Password     STRING             Password for login on FTP server
                   RemoteFile   STRING             File name including path on FTP server
                   ValueAdr     POINTER TO         Initial address of the memory area to store data to
                                BYTE
           NoOfBytes            UDINT        Size of the memory area specified in "ValueAdr"
VAR_OUTPUT Done                 BOOL         Processing completed without error
           Active               BOOL         Processing active
           Error                BOOL         Processing completed with error
           ErrorID              ⮫ ERROR_CODE Error class
                   ErrorIdent   ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
                                T             on page 1099 )
                   NoOfRec‐     UDINT         Number of actually transferred bytes
                   Bytes

Table 960: Min./max. and default values of the inputs of the IL_FTPGetAsync function block
Name               Type            Min. value     Max. value     Default value Applied
Execute            BOOL                                          FALSE         Continuous
Address            STRING                                        ''            Rising edge at “Exe‐
                                                                               cute”
Login              STRING                                        ''            Rising edge at “Exe‐
                                                                               cute”
Password           STRING                                        ''            Rising edge at “Exe‐
                                                                               cute”

                                                                   FTP        1344

Name           Type              Min. value   Max. value     Default value Applied
RemoteFile     STRING                                        ''            Rising edge at “Exe‐
                                                      cute”
ValueAdr       POINTER TO                                    0             Rising edge at “Exe‐
BYTE                                                        cute”
NoOfBytes      UDINT             0            65535          0             Rising edge at “Exe‐
                                                      cute”

Functional Description
The function block IL_FTPGetAsync retrieves a file from an FTP server and
stores it to a data area in the RAM of the control.

At a rising edge at "Execute", all inputs are applied and checked for their
validity.
Subsequently, the connection is set up to the FTP server specified in
"Address". The port used is always TCP port 21 registered for FTP.
After the connection was set up successfully, "Login" and "Password" are
transferred. If the "Login" input is empty, it is tried to login via the "Anony‐
mous" user.
If login was successful, the file transfer is started.
The FTP server transfers the file specified in "RemoteFile" to the storage area
specified in "ValueAdr". If the file length exceeds the value specified in "NoOf‐
Bytes", the process is canceled. In this case, the storage area at "ValueAdr"
does not contain the complete file. A corresponding error message is gener‐
ated. During transfer, the progress made can be read at the "NoOfRecBytes"
output.
Data is always transferred in binary mode. Passive FTP is preferably used for
data transfer at which the FTP client establishes a second connection to the
FTP server. If this mode is not supported, active FTP is used at which the FTP
server establishes a connection to the FTP client for the data transfer.
The function block requires several calls to terminate the operation.
The transfer is completed successfully when the "Done" output is set. "Active"
is set during transfer. If an error occurs, the "Error" output is set. The outputs
"ErrorID" and "ErrorIdent" contain more detailed error information.
Call the function block after a rising edge at "Execute" until either "Done" or
"Error" is set.

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 961: Error codes generated by IL_FTPGetAsync
ErrorID                      Additional1 Additional2 Description
INPUT_RANGE_ERROR            16#0A0F010 16#0C23000 Input "ValueAdr" is not set
                                  1           6
INPUT_RANGE_ERROR            16#0A0F010 16#0C23000 Input "NoOfBytes" is 0
                                  1           F
OTHER_ERROR                  16#0A0F010 16#0C23100 Socket could not be created
                                  1           1
OTHER_ERROR                  16#0A0F010 16#0C23100 Error when setting I/O mode
                                  1           2
OTHER_ERROR                  16#0A0F010 16#0C23100 Could not connect socket to port
                                  1           3

1100 /    ctrlX PLC Engineering
1344      FTP

ErrorID             Additional1 Additional2 Description
OTHER_ERROR         16#0A0F010 16#0C23100 Socket could not be set to Listen mode.
1           4
OTHER_ERROR         16#0A0F010 16#0C23100 Could not accept incoming connection.
1           5
OTHER_ERROR         16#0A0F010 16#0C23100 Error when connecting to another device.
1           6
INPUT_INVALID_ERROR 16#0A0F010 16#0C23020 Target address invalid
1           8
COMMUNICA‐          16#0A0F010 16#0C23020 Remote host denied connection establish‐
TION_ERROR               1           9      ment
COMMUNICA‐          16#0A0F010 16#0C23020 No network path to target device found
TION_ERROR               1           C
COMMUNICA‐          16#0A0F010 16#0C23200 Input "RemoteFile" is invalid
TION_ERROR               1           1
COMMUNICA‐          16#0A0F010 16#0C23200 Target buffer too small for file to be trans‐
TION_ERROR               1           2      ferred
COMMUNICA‐          16#0A0F010 16#0C23207 FTP server not ready
TION_ERROR               1           8
COMMUNICA‐          16#0A0F010 16#0C23214 Account required for login
TION_ERROR               1           C
COMMUNICA‐          16#0A0F010 16#0C2321A Service not ready
TION_ERROR               1           5
COMMUNICA‐          16#0A0F010 16#0C2321A Cannot open data connection
TION_ERROR               1           9
COMMUNICA‐          16#0A0F010 16#0C2321A Connection closed and file transfer aborted
TION_ERROR               1           A
COMMUNICA‐          16#0A0F010 16#0C2321C File not available
TION_ERROR               1           2
COMMUNICA‐          16#0A0F010 16#0C2321C Error during file processing on FTP server
TION_ERROR               1           3
COMMUNICA‐          16#0A0F010 16#0C2321C Insufficient memory on FTP server
TION_ERROR               1           4
COMMUNICA‐          16#0A0F010 16#0C2321F Error in command syntax
TION_ERROR               1           4
COMMUNICA‐          16#0A0F010 16#0C2321F Incorrect command parameters
TION_ERROR               1           5
COMMUNICA‐          16#0A0F010 16#0C2321F Command not implemented
TION_ERROR               1           6
COMMUNICA‐          16#0A0F010 16#0C2321F Incorrect command order
TION_ERROR               1           7
COMMUNICA‐          16#0A0F010 16#0C2321F Command with this parameter not imple‐
TION_ERROR               1           8      mented
COMMUNICA‐          16#0A0F010 16#0C23221 Incorrect login or password
TION_ERROR               1           2
COMMUNICA‐          16#0A0F010 16#0C23222 File not available
TION_ERROR               1           6
COMMUNICA‐          16#0A0F010 16#0C23222 Unknown page type
TION_ERROR               1           7
COMMUNICA‐          16#0A0F010 16#0C23222 Insufficient memory
TION_ERROR               1           8

                                                                  FTP       1344

ErrorID                      Additional1 Additional2 Description
COMMUNICA‐                   16#0A0F010 16#0C23222 File name not allowed
TION_ERROR                        1           9
COMMUNICA‐                   16#0A0F010 16#0C23FFF Unexpected response from FTP server
TION_ERROR                        1           E
COMMUNICA‐                   16#0A0F010 16#0C23FFF Unknown response from FTP server
TION_ERROR                        1           F
Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
codes of the CXA_Table on page 1131.

IL_FTPPutAsync

Brief description
The function block IL_FTPPutAsync stores a data area as file to an FTP server.

Interface description

Table 962: Interface variables of the IL_FTPPutAsync function block
              Name             Type             Description
VAR_INPUT     Execute          BOOL             Function block processing enabled (once, edge-con‐
                                                trolled)
              Address          STRING           Name or IP address of FTP server
              Login            STRING           Login on FTP server; empty means anonymous
                                                access
              Password         STRING           Password for login on FTP server
              RemoteFile       STRING           File name including path on FTP server
              ValueAdr         POINTER TO       Initial address of data to be sent
                               BYTE
           NoOfBytes           UDINT        Number of characters to be transferred
VAR_OUTPUT Done                BOOL         Processing completed without error
           Active              BOOL         Processing active
           Error               BOOL         Processing completed with error
           ErrorID             ⮫ ERROR_CODE Error class
              ErrorIdent       ⮫ ERROR_STRUC For detailed error information (refer to ⮫ on page )
                               T
              NoOfSend‐        UDINT         Number of actually transferred bytes
              Bytes

Table 963: Min./max. and default values of the inputs of the IL_FTPPutAsync function block
Name           Type             Min. value     Max. value    Default value Applied
Execute        BOOL                                          FALSE         Continuous

1102 /    ctrlX PLC Engineering
1344      FTP

Name               Type         Min. value      Max. value    Default value Applied
Address            STRING                                     ''            Rising edge at “Exe‐
                                                     cute”
Login              STRING                                     ''            Rising edge at “Exe‐
                                                     cute”
Password           STRING                                     ''            Rising edge at “Exe‐
                                                     cute”
RemoteFile         STRING                                     ''            Rising edge at “Exe‐
                                                     cute”
ValueAdr           POINTER TO                                 0             Rising edge at “Exe‐
BYTE                                                     cute”
NoOfBytes          UDINT        0               65535         0             Rising edge at “Exe‐
                                                     cute”

Functional Description

The function block IL_FTPPutAsync transfers data from a data area in the
control RAM to an FTP server and stores it as file.
At a rising edge at "Execute", all inputs are applied and checked for their
validity. Subsequently, the connection is set up to the FTP server specified in
"Address".
The port used is always TCP port 21 registered for FTP.
After the connection was set up successfully, "Login" and "Password" are
transferred. If the "Login" input is empty, it is tried to login via the "Anony‐
mous" user.
If login was successful, the file transfer is started. The number of bytes
specified in "NoOfBytes" is transferred from the storage area specified in "Val‐
ueAdr" to the FTP server where they are stored as file with the name specified
in "RemoteFile". The progress made during transfer can be retrieved at the
"NoOfSendBytes" output.
Data is always transferred in binary mode. Passive FTP is preferably used for
data transfer at which the FTP client establishes a second connection to the
FTP server. If this mode is not supported, active FTP is used at which the FTP
server establishes a connection to the FTP client for the data transfer.
The function block requires several calls to terminate the operation. The
transfer is completed successfully when the "Done" output is set. "Active" is
set during transfer. If an error occurs, the "Error" output is set. The outputs
"ErrorID" and "ErrorIdent" contain more detailed error information.
Call the function block after a rising edge at "Execute" until either "Done" or
"Error" is set.

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 964: Error codes generated by IL_FTPPutAsync
ErrorID                     Additional1 Additional2 Description
INPUT_RANGE_ERROR           16#0A0F010 16#0C23000 Input "ValueAdr" is not set
                                 1           6
INPUT_RANGE_ERROR           16#0A0F010 16#0C23000 Input "NoOfBytes" is 0
                                 1           F
OTHER_ERROR                 16#0A0F010 16#0C23100 Socket could not be created
                                 1           1

                                                     FTP       1344

ErrorID             Additional1 Additional2 Description
OTHER_ERROR         16#0A0F010 16#0C23100 Error when setting I/O mode
1           2
OTHER_ERROR         16#0A0F010 16#0C23100 Could not connect socket to port
1           3
OTHER_ERROR         16#0A0F010 16#0C23100 Socket could not be set to Listen mode.
1           4
OTHER_ERROR         16#0A0F010 16#0C23100 Could not accept incoming connection.
1           5
OTHER_ERROR         16#0A0F010 16#0C23100 Error when connecting to another device.
1           6

INPUT_INVALID_ERROR 16#0A0F010 16#0C23020 Target address invalid
1           8
COMMUNICA‐          16#0A0F010 16#0C23020 Remote host denied connection establish‐
TION_ERROR               1           9      ment
COMMUNICA‐          16#0A0F010 16#0C23020 No network path to target device found
TION_ERROR               1           C
COMMUNICA‐          16#0A0F010 16#0C23200 Input "RemoteFile" is invalid
TION_ERROR               1           1
COMMUNICA‐          16#0A0F010 16#0C23200 Target buffer too small for file to be trans‐
TION_ERROR               1           2      ferred
COMMUNICA‐          16#0A0F010 16#0C23207 FTP server not ready
TION_ERROR               1           8
COMMUNICA‐          16#0A0F010 16#0C23214 Account required for login
TION_ERROR               1           C
COMMUNICA‐          16#0A0F010 16#0C2321A Service not ready
TION_ERROR               1           5
COMMUNICA‐          16#0A0F010 16#0C2321A Cannot open data connection
TION_ERROR               1           9
COMMUNICA‐          16#0A0F010 16#0C2321A Connection closed and file transfer aborted
TION_ERROR               1           A
COMMUNICA‐          16#0A0F010 16#0C2321C File not available
TION_ERROR               1           2
COMMUNICA‐          16#0A0F010 16#0C2321C Error during file processing on FTP server
TION_ERROR               1           3
COMMUNICA‐          16#0A0F010 16#0C2321C Insufficient memory on FTP server
TION_ERROR               1           4
COMMUNICA‐          16#0A0F010 16#0C2321F Error in command syntax
TION_ERROR               1           4
COMMUNICA‐          16#0A0F010 16#0C2321F Incorrect command parameters
TION_ERROR               1           5
COMMUNICA‐          16#0A0F010 16#0C2321F Command not implemented
TION_ERROR               1           6
COMMUNICA‐          16#0A0F010 16#0C2321F Incorrect command order
TION_ERROR               1           7
COMMUNICA‐          16#0A0F010 16#0C2321F Command with this parameter not imple‐
TION_ERROR               1           8      mented
COMMUNICA‐          16#0A0F010 16#0C23221 Incorrect login or password
TION_ERROR               1           2
COMMUNICA‐          16#0A0F010 16#0C23222 File not available
TION_ERROR               1           6

1104 /    ctrlX PLC Engineering
1344      FTP

ErrorID                         Additional1 Additional2 Description
COMMUNICA‐                      16#0A0F010 16#0C23222 Unknown page type
TION_ERROR                           1           7
COMMUNICA‐                      16#0A0F010 16#0C23222 Insufficient memory
TION_ERROR                           1           8
COMMUNICA‐                      16#0A0F010 16#0C23222 File name not allowed
TION_ERROR                           1           9
COMMUNICA‐                      16#0A0F010 16#0C23FFF Unexpected response from FTP server
TION_ERROR                           1           E
COMMUNICA‐                      16#0A0F010 16#0C23FFF Unknown response from FTP server
TION_ERROR                           1           F
      Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
      codes of the CXA_Table on page 1131.

IL_FTPGetFileAsync
      Brief description
      The function block IL_FTPGetFileAsync retrieves a file from an FTP server and
      stores it on the Flash card.

      Interface description

Table 965: Interface variables of the IL_FTPGetFileAsync function block
                   Name           Type         Description
VAR_INPUT          Execute        BOOL         Function block processing enabled (once, edge-con‐
                                               trolled)
                   Address        STRING       Name or IP address of FTP server
                   Login          STRING       Login on FTP server; empty means anonymous
                                               access
           Password               STRING       Password for login on FTP server
           RemoteFile             STRING       File name including path on FTP server
           LocalFile              STRING       File name including path on Flash card
VAR_OUTPUT Done                   BOOL         Processing completed without error
           Active                 BOOL         Processing active
           Error                  BOOL         Processing completed with error
           ErrorID                ⮫ ERROR_CODE Error class
                   ErrorIdent     ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
                                  T             on page 1105 )
                   NoOfRec‐       UDINT         Number of actually transferred bytes
                   Bytes

                                                                   FTP         1344

Table 966: Min./max. and default values of the inputs of the IL_FTPGetFileAsync function block
Name           Type              Min. value   Max. value      Default value Applied
Execute        BOOL                                           FALSE         Continuous
Address        STRING                                         ''            Rising edge at “Exe‐
                                                                            cute”
Login          STRING                                         ''            Rising edge at “Exe‐
                                                                            cute”
Password       STRING                                         ''            Rising edge at “Exe‐
                                                                            cute”
RemoteFile     STRING                                         ''            Rising edge at “Exe‐
                                                                            cute”

LocalFile      STRING                                         ''            Rising edge at “Exe‐
                                                       cute”

Functional Description
The function block IL_FTPGetAsync retrieves a file from an FTP server and
stores it on the Flash card of the control.
At a rising edge at "Execute", all inputs are applied and checked for their
validity. Subsequently, the connection is set up to the FTP server specified in
"Address". The port used is always TCP port 21 registered for FTP.
After the connection was established successfully, "Login" and "Password" are
transferred. If the "Login" input is empty, it is tried to login via the "Anony‐
mous" users.
If login was successful, the file transfer is started. The file specified in "Remo‐
teFile" is transferred from the FTP server to the Flash card and stored under
the file name specified in "LocalFile". During transfer, the progress made can
be read at the "NoOfRecBytes" output.
Data is always transferred in binary mode. Passive FTP is preferably used for
data transfer at which the FTP client establishes a second connection to the
FTP server. If this mode is not supported, active FTP is used at which the FTP
server establishes a connection to the FTP client for the data transfer.
The function block requires several calls to terminate the operation. The
transfer is completed successfully when the "Done" output is set. "Active" is
set during transfer. If an error occurs, the "Error" output is set. The outputs
"ErrorID" and "ErrorIdent" contain more detailed error information.
Call the function block after a rising edge at "Execute" until either "Done" or
"Error" is set.

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 967: Error codes generated by IL_FTPGetFileAsync
ErrorID                      Additional1 Additional2 Description
INPUT_RANGE_ERROR            16#0A0F010 16#0C23000 Input "ValueAdr" is not set
                                  1           6
INPUT_RANGE_ERROR            16#0A0F010 16#0C23000 Input "NoOfBytes" is 0
                                  1           F
RESSOURCE_ERROR              16#0A0F010 16#0C23001 No object available with this name
                                  1           0
OTHER_ERROR                  16#0A0F010 16#0C23100 Socket could not be created
                                  1           1

1106 /    ctrlX PLC Engineering
1344      FTP

ErrorID             Additional1 Additional2 Description
OTHER_ERROR         16#0A0F010 16#0C23100 Error when setting I/O mode
1           2
OTHER_ERROR         16#0A0F010 16#0C23100 Could not connect socket to port
1           3
OTHER_ERROR         16#0A0F010 16#0C23100 Socket could not be set to Listen mode.
1           4
OTHER_ERROR         16#0A0F010 16#0C23100 Could not accept incoming connection.
1           5
OTHER_ERROR         16#0A0F010 16#0C23100 Error when connecting to another device.
1           6
INPUT_INVALID_ERROR 16#0A0F010 16#0C23020 Target address invalid
1           8
COMMUNICA‐          16#0A0F010 16#0C23020 Remote host denied connection establish‐
TION_ERROR               1           9      ment
COMMUNICA‐          16#0A0F010 16#0C23020 No network path to target device found
TION_ERROR               1           C
COMMUNICA‐          16#0A0F010 16#0C23200 Input "RemoteFile" is invalid
TION_ERROR               1           1
COMMUNICA‐          16#0A0F010 16#0C23200 Target buffer too small for file to be trans‐
TION_ERROR               1           2      ferred
COMMUNICA‐          16#0A0F010 16#0C23207 FTP server not ready
TION_ERROR               1           8
COMMUNICA‐          16#0A0F010 16#0C23214 Account required for login
TION_ERROR               1           C
COMMUNICA‐          16#0A0F010 16#0C2321A Service not ready
TION_ERROR               1           5
COMMUNICA‐          16#0A0F010 16#0C2321A Cannot open data connection
TION_ERROR               1           9
COMMUNICA‐          16#0A0F010 16#0C2321A Connection closed and file transfer aborted
TION_ERROR               1           A
COMMUNICA‐          16#0A0F010 16#0C2321C File not available
TION_ERROR               1           2
COMMUNICA‐          16#0A0F010 16#0C2321C Error during file processing on FTP server
TION_ERROR               1           3
COMMUNICA‐          16#0A0F010 16#0C2321C Insufficient memory on FTP server
TION_ERROR               1           4
COMMUNICA‐          16#0A0F010 16#0C2321F Error in command syntax
TION_ERROR               1           4
COMMUNICA‐          16#0A0F010 16#0C2321F Incorrect command parameters
TION_ERROR               1           5
COMMUNICA‐          16#0A0F010 16#0C2321F Command not implemented
TION_ERROR               1           6
COMMUNICA‐          16#0A0F010 16#0C2321F Incorrect command order
TION_ERROR               1           7
COMMUNICA‐          16#0A0F010 16#0C2321F Command with this parameter not imple‐
TION_ERROR               1           8      mented
COMMUNICA‐          16#0A0F010 16#0C23221 Incorrect login or password
TION_ERROR               1           2
COMMUNICA‐          16#0A0F010 16#0C23222 File not available
TION_ERROR               1           6

                                                                FTP       1344

ErrorID                      Additional1 Additional2 Description
COMMUNICA‐                   16#0A0F010 16#0C23222 Unknown page type
TION_ERROR                        1           7
COMMUNICA‐                   16#0A0F010 16#0C23222 Insufficient memory
TION_ERROR                        1           8
COMMUNICA‐                   16#0A0F010 16#0C23222 File name not allowed
TION_ERROR                        1           9
COMMUNICA‐                   16#0A0F010 16#0C23FFF Unexpected response from FTP server
TION_ERROR                        1           E
COMMUNICA‐                   16#0A0F010 16#0C23FFF Unknown response from FTP server
TION_ERROR                        1           F

Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
codes of the CXA_Table on page 1131.

IL_FTPPutFileAsync
Brief description
The function block IL_FTPPutFileAsync copies a file from a Flash card of the
control to an FTP server.

Interface description

Table 968: Interface variables of the IL_FTPPutFileAsync function block
              Name             Type         Description
VAR_INPUT     Execute          BOOL         Function block processing enabled (once, edge-con‐
                                            trolled)
              Address          STRING       Name or IP address of FTP server
              Login            STRING       Login on FTP server; empty means anonymous
                                            access
           Password            STRING       Password for login on FTP server
           RemoteFile          STRING       File name including path on FTP server
           LocalFile           STRING       File name including path on Flash card
VAR_OUTPUT Done                BOOL         Processing completed without error
           Active              BOOL         Processing active
           Error               BOOL         Processing completed with error
           ErrorID             ⮫ ERROR_CODE Error class
              ErrorIdent       ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
                               T             on page 1108 )
              NoOfSend‐        UDINT         Number of actually transferred bytes
              Bytes

1108 /    ctrlX PLC Engineering
1344      FTP

Table 969: Min./max. and default values of the inputs of the IL_FTPPutFileAsync function block
Name               Type          Min. value      Max. value     Default value Applied
Execute            BOOL                                         FALSE         Continuous
Address            STRING                                       ''            Rising edge at “Exe‐
                                                                              cute”
Login              STRING                                       ''            Rising edge at “Exe‐
                                                                              cute”
Password           STRING                                       ''            Rising edge at “Exe‐
                                                                              cute”
RemoteFile         STRING                                       ''            Rising edge at “Exe‐
                                                                              cute”
LocalFile          STRING                                       ''            Rising edge at “Exe‐
                                                                              cute”

Functional Description
The function block IL_FTPPutFileAsync copies a file from a Flash card of the
control to an FTP server.
At a rising edge at "Execute", all inputs are applied and checked for their
validity. Subsequently, the connection is set up to the FTP server specified in
"Address".
The port used is always TCP port 21 registered for FTP.
After the connection was established successfully, "Login" and "Password" are
transferred. If the "Login" input is empty, it is tried to login via the "Anony‐
mous" users.
If login was successful, the file transfer is started. The file specified in "Local‐
File" is transferred from the Flash card of the control and stored on the
FTP server under the file name specified in "RemoteFile". The progress made
during transfer can be retrieved at the "NoOfSendBytes" output.
Data is always transferred in binary mode. Passive FTP is preferably used for
data transfer at which the FTP client establishes a second connection to the
FTP server. If this mode is not supported, active FTP is used at which the FTP
server establishes a connection to the FTP client for the data transfer.
The function block requires several calls to terminate the operation. The
transfer is completed successfully when the "Done" output is set. "Active" is
set during transfer.
If an error occurs, the "Error" output is set. The outputs "ErrorID" and "ErrorI‐
dent" contain more detailed error information.
Call the function block after a rising edge at "Execute" until either "Done" or
"Error" is set.

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 970: Error codes generated by IL_FTPPutFileAsync
ErrorID                     Additional1 Additional2 Description
INPUT_RANGE_ERROR           16#0A0F010 16#0C23000 Input "ValueAdr" is not set
                                 1           6
INPUT_RANGE_ERROR           16#0A0F010 16#0C23000 Input "NoOfBytes" is 0
                                 1           F
RESSOURCE_ERROR             16#0A0F010 16#0C23001 No object available with this name
                                 1           0

                                                     FTP       1344

ErrorID             Additional1 Additional2 Description
OTHER_ERROR         16#0A0F010 16#0C23100 Socket could not be created
1           1
OTHER_ERROR         16#0A0F010 16#0C23100 Error when setting I/O mode
1           2
OTHER_ERROR         16#0A0F010 16#0C23100 Could not connect socket to port
1           3
OTHER_ERROR         16#0A0F010 16#0C23100 Socket could not be set to Listen mode.
1           4
OTHER_ERROR         16#0A0F010 16#0C23100 Could not accept incoming connection.
1           5

OTHER_ERROR         16#0A0F010 16#0C23100 Error when connecting to another device.
1           6
INPUT_INVALID_ERROR 16#0A0F010 16#0C23020 Target address invalid
1           8
COMMUNICA‐          16#0A0F010 16#0C23020 Remote host denied connection establish‐
TION_ERROR               1           9      ment
COMMUNICA‐          16#0A0F010 16#0C23020 No network path to target device found
TION_ERROR               1           C
COMMUNICA‐          16#0A0F010 16#0C23200 Input "RemoteFile" is invalid
TION_ERROR               1           1
COMMUNICA‐          16#0A0F010 16#0C23200 Target buffer too small for file to be trans‐
TION_ERROR               1           2      ferred
COMMUNICA‐          16#0A0F010 16#0C23207 FTP server not ready
TION_ERROR               1           8
COMMUNICA‐          16#0A0F010 16#0C23214 Account required for login
TION_ERROR               1           C
COMMUNICA‐          16#0A0F010 16#0C2321A Service not ready
TION_ERROR               1           5
COMMUNICA‐          16#0A0F010 16#0C2321A Cannot open data connection
TION_ERROR               1           9
COMMUNICA‐          16#0A0F010 16#0C2321A Connection closed and file transfer aborted
TION_ERROR               1           A
COMMUNICA‐          16#0A0F010 16#0C2321C File not available
TION_ERROR               1           2
COMMUNICA‐          16#0A0F010 16#0C2321C Error during file processing on FTP server
TION_ERROR               1           3
COMMUNICA‐          16#0A0F010 16#0C2321C Insufficient memory on FTP server
TION_ERROR               1           4
COMMUNICA‐          16#0A0F010 16#0C2321F Error in command syntax
TION_ERROR               1           4
COMMUNICA‐          16#0A0F010 16#0C2321F Incorrect command parameters
TION_ERROR               1           5
COMMUNICA‐          16#0A0F010 16#0C2321F Command not implemented
TION_ERROR               1           6
COMMUNICA‐          16#0A0F010 16#0C2321F Incorrect command order
TION_ERROR               1           7
COMMUNICA‐          16#0A0F010 16#0C2321F Command with this parameter not imple‐
TION_ERROR               1           8      mented
COMMUNICA‐          16#0A0F010 16#0C23221 Incorrect login or password
TION_ERROR               1           2

1110 /    ctrlX PLC Engineering
1344      TFTP

ErrorID                   Additional1 Additional2 Description
COMMUNICA‐                16#0A0F010 16#0C23222 File not available
TION_ERROR                     1           6
COMMUNICA‐                16#0A0F010 16#0C23222 Unknown page type
TION_ERROR                     1           7
COMMUNICA‐                16#0A0F010 16#0C23222 Insufficient memory
TION_ERROR                     1           8
COMMUNICA‐                16#0A0F010 16#0C23222 File name not allowed
TION_ERROR                     1           9
COMMUNICA‐                16#0A0F010 16#0C23FFF Unexpected response from FTP server
TION_ERROR                     1           E
COMMUNICA‐                16#0A0F010 16#0C23FFF Unknown response from FTP server
TION_ERROR                     1           F
Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
codes of the CXA_Table on page 1131.

## 35.6 TFTP

### 35.6.1 Introduction and overview

Many peripheral devices use the TFTP protocol (Trivial File Transfer Protocol)
to transfer firmware or the configuration. This protocol can be implemented
using little resources and is thus used by devices with little memory size.
Upon firmware boot, an TFTP server is started in all Rexroth IndraDrives
and is therefore available as remote host. This TFTP server is used for firm‐
ware updates. Windows-based computers normally do not provide an installed
TFTP server.
Usually, the TFTP server runs on the UDP port 69. This port has to be reach‐
able from the control. Any possible firewalls present in the network have to
be configured accordingly.

### 35.6.2 Asynchronous function blocks

Introduction and overview
Many peripheral devices use the TFTP protocol (Trivial File Transfer Protocol)
to transfer firmware or the configuration. This protocol can be implemented
using little resources and is thus used by devices with little memory size.
The function blocks IL_TFTPutFileAsync and IL_TFTPGetFileAsync allow using
the TFTP protocol to transfer data from the PLC.
Files can be transferred between the Flash card of the control and the target
device.
Both function blocks operate asynchronously. Thus, they do not complete the
operation at first call, but have to be called several times until the operation
is completed or an error is reported.

IL_TFTPGetFileAsync
Brief description
The function block IL_TFTPGetFileAsync transfers a file from a distant device
to a Compact Flash card of the control using the TFTP protocol.

                                                               TFTP         1344

Interface description

Table 971: Interface variables of the IL_TFTPGetFileAsync function block
              Name           Type         Description
VAR_INPUT     Execute        BOOL         Function block processing enabled (once, edge-con‐
                                          trolled)
           Address           STRING       Name or IP address of the target device
           RemoteFile        STRING       File name including path on target device
           LocalFile         STRING       File name including path on Flash card
VAR_OUTPUT Done              BOOL         Processing completed without error
           Active            BOOL         Processing active
           Error             BOOL         Processing completed with error
           ErrorID           ⮫ ERROR_CODE Error class
              ErrorIdent     ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
                             T             on page 1112 )
              NoOfRec‐       UDINT         Number of actually transferred bytes
              Bytes

Table 972: Min./max. and default values of the inputs of the IL_TFTPGetFileAsync function block
Name           Type           Min. value      Max. value   Default value Applied
Execute        BOOL                                        FALSE         Continuous
Address        STRING                                      ''            Rising edge at “Exe‐
                                                                         cute”
RemoteFile     STRING                                      ''            Rising edge at “Exe‐
                                                                         cute”
LocalFile      STRING                                      ''            Rising edge at “Exe‐
                                                                         cute”

Functional Description

The function block IL_TFTPGetFileAsync transfers the file specified in "Remo‐
teFile" from a distant device using the TFTP protocol and stores it on the
Compact Flash card of the control under the file name "LocalFile".
Prerequisites
The target device has to be reachable from the control via internet protocol
(IPv4). This is the case if the device is reachable from the control via ping
(see IL_PingAsync). However, it is not required to get this explicitly checked
by the PLC program. The target device has to support read-only access via
TFTP protocol.
Address

1112 /    ctrlX PLC Engineering
1344      TFTP

The "Address" input contains the IP address of the target device. It has to
consists of four decimal numbers between 0 and 255 separated by points as
common for the notation in IPv4.

Example IP address
"192.168.1.42"

RemoteFile
The "RemoteFile" input specifies the file name on the target device. Thus,
a specific file can be called by the target device. Not every target device
supports the specification of a file name on the target device. In this case, the
"RemoteFile" input is ignored.
LocalFile
The "LocalFile" input indicates the file name on the local Compact Flash card
of the control. It can also contain a complete path. The default directory is
the USER partition of the control.

Time response
The IL_TFTPGetFileAsync function block operates asynchronously. After the
start due to a rising edge at the "Execute" input, it reads the inputs "Address",
"RemoteFile" and "LocalFile".
The function block has to be called cyclically until the successful transfer is
signaled via the "Done" output or the "Error" output displays an error. During
this period, the "Active" output is set.

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 973: Error codes generated by IL_TFTPGetFileAsync
ErrorID                    Additional1 Additional2 Description
INPUT_INVALID_ERROR       16#0A0F0101 16#0C230208 Target address invalid
COMMUNICA‐                16#0A0F0101 16#0C23020C No network path to target device found
TION_ERROR
OTHER_ERROR               16#0A0F0101 16#0C231001 Socket could not be created
OTHER_ERROR               16#0A0F0101 16#0C231002 Error when setting I/O mode
OTHER_ERROR               16#0A0F0101 16#0C231003 Could not connect socket to port
COMMUNICA‐                16#0A0F0101 16#0C231006 Error while establishing a connection
TION_ERROR
INPUT_INVALID_ERROR       16#0A0F0101 16#0C23100B Input "RemoteFile" is invalid
INPUT_INVALID_ERROR       16#0A0F0101 16#0C23100C Input "LocalFile" input is invalid
INPUT_INVALID_ERROR       16#0A0F0101 16#0C23100 "LocalFile" not found
                                           D
ACCESS_ERROR              16#0A0F0101 16#0C23100E "LocalFile" could not be written
ACCESS_ERROR              16#0A0F0101 16#0C23100F "RemoteFile" not found
ACCESS_ERROR              16#0A0F0101 16#0C231010 Access violation
COMMUNICA‐                16#0A0F0101 16#0C231012 Prohibited TFTP operation
TION_ERROR
COMMUNICA‐                16#0A0F0101 16#0C231013 Unknown transfer ID
TION_ERROR
ACCESS_ERROR              16#0A0F0101 16#0C231015 Unknown user

                                                                      TFTP         1344

ErrorID                       Additional1 Additional2 Description
COMMUNICA‐                   16#0A0F0101 16#0C231016 Unexpected communication error
TION_ERROR
COMMUNICA‐                   16#0A0F0101 16#0C231018 Timeout during transmission
TION_ERROR
ACCESS_ERROR                 16#0A0F0101 16#0C23xxxx Local file error, see CXA_FileAsync
      Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
      codes of the CXA_Table on page 1131.

IL_TFTPPutFileAsync

      Brief description
      The function block IL_TFTPPutFileAsync transfers a file from the Compact
      Flash card of the control to a distant device using the TFTP protocol.

      Interface description

Table 974: Interface variables of the IL_TFTPPutFileAsync function block
               Name            Type         Description
VAR_INPUT      Execute         BOOL         Function block processing enabled (once, edge-con‐
                                            trolled)
           Address             STRING       Name or IP address of the target device
           RemoteFile          STRING       File name including path on target device
           LocalFile           STRING       File name including path on Flash card
VAR_OUTPUT Done                BOOL         Processing completed without error
           Active              BOOL         Processing active
           Error               BOOL         Processing completed with error
           ErrorID             ⮫ ERROR_CODE Error class
               ErrorIdent      ⮫ ERROR_STRUC Detailed error information (see ⮫ Troubleshooting
                               T             on page 1114 )
               NoOfSend‐       UDINT         Number of actually transferred bytes
               Bytes

Table 975: Min./max. and default values of the inputs of the IL_TFTPPutFileAsync function block
Name           Type              Min. value    Max. value   Default value Applied
Execute        BOOL                                         FALSE         Continuous
Address        STRING                                       ''            Rising edge at “Exe‐
                                                                          cute”
RemoteFile     STRING                                       ''            Rising edge at “Exe‐
                                                                          cute”

1114 /    ctrlX PLC Engineering
1344      TFTP

Name               Type         Min. value      Max. value     Default value Applied
LocalFile          STRING                                      ''            Rising edge at “Exe‐
                                                      cute”

Functional Description

The function block IL_TFTPPutFileAsync transfers the file specified in "Local‐
File" from the Compact Flash card of the control to a distant device using the
TFTP protocol and stores it under the file name "RemoteFile".
Prerequisites
The target device has to be reachable from the control via internet protocol
(IPv4). This is the case if the device is reachable from the control via ping
(⮫ Chapter IL_PingAsync on page 1095). However, it is not required to get this
explicitly checked by the PLC program. The target device has to support write
access via TFTP protocol.
Address
The "Address" input contains the IP address of the target device. It has to
consists of four decimal numbers between 0 and 255 separated by points as
common for the notation in IPv4.

Example address
"192.168.1.42"

The "RemoteFile" input specifies the file name on the target device. Thus,
a specific file can be called by the target device. Not every target device
supports the specification of a file name on the target device. In this case, the
"RemoteFile" input is ignored.
RemoteFile
LocalFile
The "LocalFile" input indicates the file name on the local Compact Flash card
of the control. It can also contain a complete path. The default directory is
the USER partition of the control.

Time response
The IL_TFTPPutFileAsync function block operates asynchronously. After the
start due to a rising edge at the "Execute" input, it reads the inputs "Address",
"RemoteFile" and "LocalFile".
The function block has to be called cyclically until the successful transfer is
signaled via the "Done" output or the "Error" output displays an error. During
this period, the "Active" output is set.

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2:
Table 976: Error codes generated by IL_TFTPPutFileAsync
ErrorID                      Additional1 Additional2 Description
INPUT_INVALID_ERROR         16#0A0F0101 16#0C230208 Target address invalid
COMMUNICA‐                  16#0A0F0101 16#0C23020C No network path to target device found
TION_ERROR
OTHER_ERROR                 16#0A0F0101 16#0C231001 Socket could not be created
OTHER_ERROR                 16#0A0F0101 16#0C231002 Error when setting I/O mode
OTHER_ERROR                 16#0A0F0101 16#0C231003 Could not connect socket to port

                                                  Cyclic communication       1344

ErrorID                      Additional1 Additional2 Description
COMMUNICA‐                  16#0A0F0101 16#0C231006 Error while establishing a connection
TION_ERROR
INPUT_INVALID_ERROR         16#0A0F0101 16#0C23100B Input "RemoteFile" is invalid
INPUT_INVALID_ERROR         16#0A0F0101 16#0C23100C Input "LocalFile" input is invalid
INPUT_INVALID_ERROR         16#0A0F0101 16#0C23100 "LocalFile" not found
                           D
ACCESS_ERROR                16#0A0F0101 16#0C23100E "LocalFile" could not be written
ACCESS_ERROR                16#0A0F0101 16#0C23100F "RemoteFile" not found
ACCESS_ERROR                16#0A0F0101 16#0C231010 Access violation

COMMUNICA‐                  16#0A0F0101 16#0C231012 Prohibited TFTP operation
TION_ERROR
COMMUNICA‐                  16#0A0F0101 16#0C231013 Unknown transfer ID
TION_ERROR
ACCESS_ERROR                16#0A0F0101 16#0C231015 Unknown user
COMMUNICA‐                  16#0A0F0101 16#0C231016 Unexpected communication error
TION_ERROR
COMMUNICA‐                  16#0A0F0101 16#0C231018 Timeout during transmission
TION_ERROR
ACCESS_ERROR                16#0A0F0101 16#0C23xxxx Local file error, see CXA_FileAsync
  Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
  codes of the CXA_Table on page 1131.

## 35.7 Cyclic communication

### 35.7.1 Introduction and overview

  The function blocks under CyclicCommunication allow to exchange data cycli‐
  cally. They are based on the TCP and UDP communication function blocks of
  the CXA_SocketComm.
  Data to be exchanged can be specified in its user-defined data structures.
  Apart from the cyclic communication, data can also be exchanged on request.

### 35.7.2 Asynchronous function blocks

Introduction and overview
The function blocks under CyclicCommunication allow a cyclic data exchange.
They are based on the TCP- and UDP communication function blocks of the
CXA_SocketComm.
Data to be exchanged can be specified in its user-defined data structures.
Apart from the cyclic communication, data can also be exchanged on request.
The field of application for the cyclic communication is the cyclic data
exchange between two controls or another communication partner. Event-con‐
trolled communication is required when querying data such as a camera. Both
communication methods are supported via UDP and TCP protocol.

IL_TCPCyclic
  Brief description
  The IL_TCPCyclic function block sends and receives data via a TCP-based
  connection.
  The cyclic bidirectional operation and the event-controlled transmission mode
  are supported.

1116 /    ctrlX PLC Engineering
1344      Cyclic communication

To establish a connection, one communication partner has to be the server,
that means that it listens to incoming connections. The other communication
partner is the client, that means that it tries to establish a TCP connection to
the server. Received packages can be read at every function block call. The
function block is enabled at a rising edge at "Enable" and has to be called
cyclically. "InOperation” indicates an established connection.

Interface description

Table 977: Interface description of the IL_TCPCyclic function block
                   Name            Type Description
VAR_INPUT          Enable          BOOL Starts at a rising edge
                   Mode            IL_CONN_MODE
                                        Specifies the connection mode
                   IpAddress       STRING(15)
                                        IP address of the communication partner as
                                        aaa.bbb.ccc.ddd
           Port           UINT          Communication port (default: Port 50000). The
                                        port should be in the range from 50000 to
                                        65535. Communication partners have identical
                                        port numbers
           Send           BOOL          Rising edge sends data;
                                        only available for the
                                        modes "Cyclic_Event_Server",
                                        "Cyclic_Event_Client", "Cyclic_Event_Server_Pro‐
                                        tocol", "Cyclic_Event_Client_Protocol".
           SendDataAdr    POINTER TO    Pointer to the data to be sent. A data maximum
                          BYTE          of 1400 bytes can be sent.
           RecvDataAdr    POINTER TO    Pointer to the data to be received. A data max‐
                          BYTE          imum of 1400 bytes can be received.
           SizeOfSendData UDINT         Length of data to be sent
           SizeOfRecvData UDINT         Length of the data to be received
           Timeout        TIME          Optional; communication timeout (default: 1500
                                        ms)
VAR_OUTPUT InOperation    BOOL          TRUE indicates that the function block is ready
                                        to send or receive data.
           Error          BOOL          TRUE indicates an error.
           ErrorID        ⮫ ERROR_CODE Error class
           ErrorIdent     ⮫ ERROR_STRUC Detailed error information
                          T

                                               Cyclic communication       1344

Name              Type          Description
Status            IL_CONN_STATU Status information on the function block state
           S
ResponseTime      TIME          Time required from sending to a successful
                         reception.
DoneSend          BOOL          TRUE indicates that data was successfully sent
                         for one cycle
DoneRecv          BOOL          TRUE indicates that data was successfully
                         received for one cycle

Table 978: Min./max. and default values of the inputs of the IL_TCPCyclic function block

Name            Type        Min. value         Max. value     Default value    Applied
Enable          BOOL                                          FALSE            Continuous
Mode            IL_CONN_MOD Cyclic_Server      Cyclic_Event_C Cyclic_Server    Rising edge at
E                              lient_Protocol                  "Enable"
IpAddress       STRING(15)  '0.0.0.0'          '25525525525                    Rising edge at
                          5'                              "Enable"
Port            UINT            0              65535          50000            Rising edge at
                                                          "Enable"
Send            BOOL                                           FALSE           Continuously, only
                                                          available for the
                                                          modes
                                                          "Cyclic_Event_Serv
                                                          er",
                                                          "Cyclic_Event_Clien
                                                          t",
                                                          "Cyclic_Event_Serv
                                                          er_Protocol",
                                                          "Cyclic_Event_Clien
                                                          t_Protocol"
SendDataAdr     POINTER TO      >0                                             Continuous
BYTE
RecvDataAdr     POINTER TO      >0                                             Continuous
BYTE
SizeOfSend‐     UDINT           1              1400                            Continuous
Data
SizeOfRecv‐     UDINT           1              1400                            Continuous
Data
Timeout         TIME                                           T#1500MS        Continuous

Connection mode
The "Mode" input indicates how the connection is established between two
communication partners. This input also determines whether the data is
cyclic- or event-controlled and whether the length of the received data is
considered.
Possible values are described in the enumeration type IL_CONN_MODE.
The transmission data length is not considered for the modes "Server_Client",
"Cyclic_Client", "Cyclic_Event_Server" and "Cyclic_Event_Clientr".
If the number of bytes sent from the remote host is higher than the buffer
"RecvDataAdr", only "SizeOfRecvData" bytes are copied to the reception buffer
"RecvDataAdr".
The remaining and newly received bytes are copied upon next cycle.

1118 /    ctrlX PLC Engineering
1344      Cyclic communication

The length of the transmission data is considered for the modes
"Cyclic_Server_Protocol", "Cyclic_Client_Protocol", "Cyclic_Event_Server_Pro‐
tocol" and "Cyclic_Event_Client_Protocol".
If the number of bytes sent by the remote host is higher than the configured
buffer size, an error is output.

Functional Description
The IL_TCPCyclic function block sends and receives data via a TCP/IP-based
connection. The order of the characters are sent is always maintained. If an
error occurs during transmission, the package in question is automatically
resent. Therefore, data cannot be lost. A connection loss is reported in an
error code at next read or write access. It is distinguished between an "active"
and a "passive" connection:
● The "passive" connection mode specifies a port and then it is waited for
   queries on this port (so-called “Listening”). This method is used by servers
   (web server, mail server, etc.).
● For an "active" connection, an IP-address of the remote host and a port is
   required. This port has to be "open", that means that a client program has
   to have an established connection on the target device on this port.
After the connection has been established, data can be transmitted in both
directions. The function block IL_TCPCyclic establishes a cyclic server/client
Ethernet-based network communication between the controls.
Server and client communicate acyclically. Usually, the transferred data (1x
there+ 1x back; that is with acknowledgement) is available for further proc‐
essing within two PLC cycles in the respective PLC program.
Example: The transfer cycle is less than 20 ms for a PLC cycle time of 10 ms.
However, data is not available before the second PLC cycle
Supported functions:
● Cyclic communication
● Use as active (client) and passive (server) connection
● Max. telegram length: 1400 bytes
● Event-controlled transmission
● Timeout check
● Check for double telegram failure when receiving or sending
● Check for connection abort
The cyclic communication procedure is as follows:
● The server opens a socket on the port and waits for queries
● The client establishes a connection to the port of the server
● Cyclic_Client: The client starts to exchange data.
  The client sends a telegram to the server, starts the time monitoring
  (TimeOut) and waits for the response
  Cyclic_Client_Protocol: The client starts to exchange data.
  A header with magic number 4711 and data length are send to the server
  first. The client sends the data, starts the time monitoring (TimeOut) and
  waits for the response.

                                                Cyclic communication        1344

● Cyclic_Server: The server receives the data from the client.
  The server responds with a telegram, starts the time monitoring and waits
  for the response.
  Cyclic_Server_Protocol: The server receives the data from the client.
  The header sent by the client is expected first. The magic number 4711 is
  checked. Subsequently, the server receives the data sent by the client. The
  data length of the received data is checked against the data length con‐
  tained in the header. Subsequently, the server responds with a telegram,
  starts the time monitoring and waits for the response.
● Cyclic change: Server – Client
● A response is expected for each transmitted telegram

The event-controlled communication sequence is as follows:
● The server opens a socket on the port and waits for queries
● The client establishes a connection to the port of the server
● Cyclic_Event_Client: If a rising edge is entered at the "Send" input of the
  Client, the Client sends a telegram to the server and waits for a response.
  Cyclic_Event_Client_Protocol: If a rising edge is entered at the "Send" input
  of the Client, a header with magic number 4711 and the data length is
  send to the server first. The Client sends the data and waits for a server
  response
● Cyclic_Event_Server: The server receives the data from the client.
  In case of a rising edge is entered at the "Send" input, the server responds
  with a telegram and waits for a response by the client.
  Cyclic_Event_Server_Protocol: The server receives the data from the client.
  The header sent by the client is expected first. The magic number 4711
  is checked. Subsequently, the server receives the data sent by the client.
  The data length of the received data is checked against the data length
  contained in the header. In case of a rising edge is entered at the "Send"
  input, the server responds with a telegram and waits for a response by the
  client.

Diagnostics
The "Status" output indicates the connection state between two communica‐
tion partners.
Possible values are described in the enumeration type IL_CONN_STATUS.

Troubleshooting
The function block uses the error table CXA_TABLE.
Table 979: Error codes generated by IL_TCPCyclic
ErrorID             Additional1         Additional2 Description
INPUT_RANGE_ERROR   16#0A0F010          16#0C23.00 Address in RecvDataAdr cannot be 0 or lower.
                         1                  06
INPUT_RANGE_ERROR 16#0A0F010            16#0C23.00 The size of SizeOfRecvData has to be at least
                         1                  0F      1.
INPUT_INVALID_ERROR 16#0A0F010          16#0C23.02 The socket handle is invalid.
                         1                  02
COMMUNICA‐          16#0A0F010          16#0C23.02 The port is already assigned.
TION_ERROR               1                  07
INPUT_INVALID_ERROR 16#0A0F010          16#0C23.02 Target address invalid
                         1                  08
COMMUNICA‐          16#0A0F010          16#0C23.02 Remote host denied connection establish‐
TION_ERROR               1                  09      ment

1120 /    ctrlX PLC Engineering
1344      Cyclic communication

ErrorID             Additional1          Additional2 Description
COMMUNICA‐          16#0A0F010           16#0C23.02 Timeout occurred.
TION_ERROR               1                   0A
COMMUNICA‐          16#0A0F010           16#0C23.02 Remote host not found.
TION_ERROR               1                   0B
COMMUNICA‐          16#0A0F010           16#0C23.02 No network path to target device found
TION_ERROR               1                   0C
COMMUNICA‐          16#0A0F010           16#0C23.02 The connection was closed.
TION_ERROR               1                   0E
COMMUNICA‐          16#0A0F010           16#0C23.02 Connection interrupted by software
TION_ERROR               1                   0F
COMMUNICA‐          16#0A0F010           16#0C23.02 Remote host closed the connection.
TION_ERROR               1                   11
OTHER_ERROR         16#0A0F010           16#0C23.10 Socket could not be created
    1                   01
OTHER_ERROR         16#0A0F010           16#0C23.10 Error when setting I/O mode
    1                   02
OTHER_ERROR         16#0A0F010           16#0C23.10 Could not connect socket to port
    1                   03
OTHER_ERROR         16#0A0F010           16#0C23.10 Socket could not be set to Listen mode.
    1                   04
OTHER_ERROR         16#0A0F010           16#0C23.10 Could not accept incoming connection.
    1                   05
OTHER_ERROR         16#0A0F010           16#0C23.10 Error when connecting to another device.
    1                   06
INPUT_INVALID_ERROR 16#0A0F010           16#0C23.10 The port number is not in a valid range.
    1                   07
INPUT_RANGE_ERROR 16#0A0F010             16#0C23.10 SizeOfSendData must not exceed 1400. A
    1                   08      maximum of 1400 bytes can be transmitted.
COMMUNICA‐          16#0A0F010           16#0C23.10 Unknown connection mode at the Mode
TION_ERROR               1                   09      input.
COMMUNICA‐          16#0A0F010           16#0C23.10 Invalid protocol
TION_ERROR               1                   19
COMMUNICA‐          16#0A0F010           16#0C23.10 Data transmission error, sent data does not
TION_ERROR               1                   1A      correspond to the received data
Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
codes of the CXA_Table on page 1131.

IL_UDPCyclic
Brief description
The IL_UDPCyclic function block sends and receives data via a UDP-based
connection.
The cyclic bidirectional operation and the event-controlled transmission mode
are supported.

                                           Cyclic communication        1344

Interface description

Table 980: Interface variables of the IL_UDPCyclic function block
              Name              Type    Description
VAR_INPUT     Enable            BOOL    Starts at a rising edge
              Mode              IL_CONN_MODE
                                        Specifies the connection mode
              IpAddress         STRING(15)
                                        IP address of the communication partner as
                                        aaa.bbb.ccc.ddd
           Port           UINT          Communication port (default: Port 50000). The
                                        port should be in the range from 50000 to
                                        65535. The communication partners have an
                                        identical port
           Send           BOOL          Rising edge sends data;
                                        Only available for the "Cyclic_Event_Server" and
                                        "Cyclic_Event_Client" modes.
           SendDataAdr    POINTER TO    Pointer to the data to be sent. A data maximum
                          BYTE          of 1400 bytes can be sent.
           RecvDataAdr    POINTER TO    Pointer to the data to be received. A data max‐
                          BYTE          imum of 1400 bytes can be received.
           SizeOfSendData UDINT         Length of data to be sent
           SizeOfRecvData UDINT         Length of the data to be received
           Timeout        TIME          Optional; communication timeout (default: 1500
                                        ms)
VAR_OUTPUT InOperation    BOOL          TRUE indicates that the function block is ready
                                        to send or receive data.
           Error          BOOL          TRUE indicates an error.
           ErrorID        ⮫ ERROR_CODE Error class
           ErrorIdent     ⮫ ERROR_STRUC Detailed error information
                          T
           Status         IL_CONN_STATU Status information on the function block state
                          S
           ResponseTime   TIME          Time required from sending to a successful
                                        reception.
           DoneSend       BOOL          TRUE indicates that data was successfully sent
                                        for one cycle
           DoneRecv       BOOL          TRUE indicates that data was successfully
                                        received for one cycle

1122 /    ctrlX PLC Engineering
1344      Cyclic communication

Table 981: Min./max. and default values of the inputs of the IL_UDPCyclic function block
Name               Type        Min. value         Max. value     Default value    Applied
Enable             BOOL                                          FALSE            Continuous
Mode               IL_CONN_MOD Cyclic_Server      Cyclic_Event_C Cyclic_Server    Rising edge at
                   E                              lient                           "Enable"
IpAddress          STRING(15)  '0.0.0.0'          '25525525525                    Rising edge at
                                                  5'                              "Enable"
Port               UINT           0               65535          50000            Rising edge at
                                                                                  "Enable"
Send               BOOL                                           FALSE           Continuous, only
                                                                                  for the
                                                                                  "Cyclic_Event_Serv
                                                                                  er" and
                                                                                  "Cyclic_Event_Clien
                                                                                  t” modes
SendDataAdr        POINTER TO     >0                                              Continuous
                   BYTE
RecvDataAdr        POINTER TO     >0                                              Continuous
                   BYTE
SizeOfSend‐        UDINT          1               1400                            Continuous
Data
SizeOfRecv‐        UDINT          1               1400                            Continuous
Data
Timeout            TIME                                           T#1500MS        Continuous

Connection mode
The Mode input indicates how the connection is established between two
communication partners. This input also specifies whether data is cyclically
transferred or event-controlled.
Possible values are described in the enumeration type IL_CONN_MODE.

Functional description
The IL_UDPCyclic function block sends and receives data via a UDP-based
connection.
The cyclic bidirectional operation and the event-controlled transmission mode
are supported.
UDP is a connection-free IP protocol. In contrast to the TCP protocol, there
is no connection establishment prior to the actual data exchange. Communica‐
tion is package-based. Received data packages are stored in the buffer, but
not merged. Every reception call takes exactly one package from the queue.
Received UDP data packages are not acknowledged. It is therefore not pos‐
sible to identify lost packages. UDP is therefore suitable for cyclic data trans‐
mission, in which data of possibly lost packages is updated by later packages.
To communicate, a server has to provide an open port to a client. Received
packages can be received and read in one function block call. The function
block is enabled at a rising edge at "Enable" and has to be called cyclically.
The server opens a UDP socket at a given port while the client's UDP port is
not known. In this configuration, the client can only send but not receive. The
server-server variant allows a bidirectional UDP server-server communication.
In this configuration, both communication partners can send and receive data
packages if the respective target port is specified.

                                                 Cyclic communication        1344

Server and client communicate acyclically for the PLC program. Normally,
the transferred data (1x there+ 1x back; that is with acknowledgement) is
available for further processing within two PLC cycles in the respective PLC
program. Example: The transfer cycle is less than 20 ms for a PLC cycle time
of 10 ms. However, data is not available before the second PLC cycle
Supported functions:
● Cyclic communication
● Use as active (client) and passive (server) connection
● Telegram length: 1400 bytes
● Event-controlled transmission
● Timeout check

● Double telegram failure: Checking when receiving or sending
● Connection abort check
The cyclic behavior was achieved by the following measurements:
● The server opens a socket on the port and waits for queries.
● The client connects to the socket on the port on the server
● The client starts the data exchange. It sends a telegram to the server, starts
  the time monitoring (TimeOut) and waits for the response.
● The server receives data from the client, starts the time monitoring and
  waits for the response.
● The client receives data from the server, starts the time monitoring and
  waits for the response.
● Cyclic change: Server – Client as described above
● A response is expected for each sent telegram

Diagnostics
The "Status" output indicates the connection state between two communica‐
tion partners.
Possible values are described in the enumeration type IL_CONN_STATUS.
The IL_UDPCyclic function blocks can also output more detailed information:
● To display more details, enter <FunctionBlock InstanceName>.StatusDetail;
  in the PLC program and this flag can be set via forcing. This outputs the
  following states additionally: "Receiving", "Received", "Transmitting" and
  "Transmitted"
● If "<FunctionBlock InstanceName>.ConnBreak;" is set in the PLC program,
  simple telegram failures can be displayed.
● If "<FunctionBlock InstanceName>.uiConnBreak;" is set in the PLC pro‐
  gram, the number of simple telegram failures can be displayed.

Troubleshooting
The function block uses the error table CXA_TABLE.
Table 982: Error codes generated by IL_UDPCyclic
ErrorID             Additional1         Additional2 Description
INPUT_RANGE_ERROR   16#0A0F010          16#0C23.00 Address in RecvDataAdr cannot be 0 or lower.
                         1                  06
INPUT_RANGE_ERROR 16#0A0F010            16#0C23.00 The size of SizeOfRecvData has to be at least
                         1                  0F      1.
INPUT_INVALID_ERROR 16#0A0F010          16#0C23.02 The socket handle is invalid.
                         1                  02
COMMUNICA‐          16#0A0F010          16#0C23.02 The port is already assigned.
TION_ERROR               1                  07

1124 /    ctrlX PLC Engineering
1344      Cyclic communication

ErrorID             Additional1      Additional2 Description
INPUT_INVALID_ERROR 16#0A0F010       16#0C23.02 Target address invalid
      1               08
COMMUNICA‐          16#0A0F010       16#0C23.02 Remote host denied connection establish‐
TION_ERROR               1               09      ment
COMMUNICA‐          16#0A0F010       16#0C23.02 Timeout occurred.
TION_ERROR               1               0A
COMMUNICA‐          16#0A0F010       16#0C23.02 Remote host not found.
TION_ERROR               1               0B
COMMUNICA‐          16#0A0F010       16#0C23.02 No network path to target device found
TION_ERROR               1               0C
COMMUNICA‐          16#0A0F010       16#0C23.02 The connection was closed.
TION_ERROR               1               0E
COMMUNICA‐          16#0A0F010       16#0C23.02 Connection interrupted by software
TION_ERROR               1               0F
COMMUNICA‐          16#0A0F010       16#0C23.02 Remote host closed the connection.
TION_ERROR               1               11
OTHER_ERROR         16#0A0F010       16#0C23.10 Socket could not be created
      1               01
OTHER_ERROR         16#0A0F010       16#0C23.10 Error when setting I/O mode
      1               02
OTHER_ERROR         16#0A0F010       16#0C23.10 Could not connect socket to port
      1               03
OTHER_ERROR         16#0A0F010       16#0C23.10 Socket could not be set to Listen mode.
      1               04
OTHER_ERROR         16#0A0F010       16#0C23.10 Could not accept incoming connection.
      1               05
OTHER_ERROR         16#0A0F010       16#0C23.10 Error when connecting to another device.
      1               06
INPUT_RANGE_ERROR 16#0A0F010         16#0C23.10 SizeOfRecvData and SizeOfRecvData may be
      1               08      1400 max. A maximum of 1400 bytes can be
                              received.
COMMUNICA‐                16#0A0F010 16#0C23.10 Unknown connection mode at the Mode
TION_ERROR                     1         09      input.
COMMUNICA‐                16#0A0F010 16#0C23.10 Data transmission error, sent data does not
TION_ERROR                     1         1A      correspond to the received data
  Other error codes are listed in ⮫ Chapter 35.9.1 CXA_SocketComm - Error
  codes of the CXA_Table on page 1131.

IL_CONN_MODE
The "IL_CONN_MODE " enumeration type indicates how the connection is
established between two communication partners.
It also specifies whether data is cyclically transferred or in an event-controlled
manner with or without a protocol.

Table 983: Connection mode of the function blocks IL_TCPCyclic and IL_UDPCyclic
ENUM               Description
Cyclic_Server      Server; cyclic operation, waits for the first telegram from the client
Cyclic_Client      Client; cyclic operation, starts the data exchange
Cyclic_Event_Serve As Cyclic_Server; data can be sent event-controlled via an edge at "Send"
r

                                           Cyclic communication       1344

ENUM                Description
Cyclic_Event_Client As Cyclic_Client; data can be sent event-controlled via an edge at "Send"
Cyclic_Server_Pro‐ Server; cyclic operation, waits for the first telegram from the client. Magic
tocol               number and transmission data length have to be considered (only available
for IL_TCPCyclic)
Cyclic_Client_Pro‐ Client; cyclic operation, starts the data exchange. Magic number and transmis‐
tocol               sion data length have to be considered (only available for IL_TCPCyclic)
Cyclic_Event_Serve As Cyclic_Server_Protocol; data can be sent event-controlled via an edge at
r_Protocol          "Send”. Magic number and transmission data length have to be considered
(only available for IL_TCPCyclic)
Cyclic_Event_Serve As Cyclic_Client_Protocol; data can be sent event-controlled via an edge at

r_Protocol          "Send”. Magic number and transmission data length have to be considered
(only available for IL_TCPCyclic)

−   The communication of the function blocks is bidirectional.
−   During reception, the number of bytes specified under "SizeOfRecv‐
Data" is expected (applies to Mode = Cyclic_Server, Mode
= Cyclic_Client, Mode = Cyclic_Server_Protocol or Mode =
Cyclic_Client_Protocol).
−   If Mode = Cyclic_Event_*, it is possible to receive less data.
−   If different control variants or third-party controls communicate with
each other, consider the "natural alignment" and "packed alignment"; that
means that is it continuously written in WORD size on the memory range
and can thus contain gaps (so-called filling bytes).
Recommendation:
Start with the big data types such as DWORD - WORD - BYTE - BOOL.
STRING is comparable to BYTE
−   For the modes "Cyclic_Server_Protocol", "Cyclic_Client_Protocol",
"Cyclic_Event_Server_Protocol" and "Cyclic_Event_Client_Protocol":
Header and transmission data are sent/received individually.
At Send:
The header with the two elements "MagicNumber (4711, WORD)" and
"DataSize (UINT) = "SizeOfSendData" of the remote host" is sent first.
Subsequently, data is send.
At Receive:
The header is expected.
The two header elements are checked.
If the MagicNumber (WORD) is unequal to 4711 or if the "DataSize (UINT)"
is greater than the input value "SizeOfRecvData", an error is output.
If no error occurs, the data is received.

IL_CONN_STATUS
The enumeration type IL_CONN_STATUS indicates the current connection
status between the two communication partners.

Table 984: Diagnostic status of the function blocks IL_TCPCyclic and IL_UDPCyclic
ENUM              Description
NotConnected      The function block is disabled. There is no connection
WaitingForConnec‐ A connection is established or an incoming connection is expected
tion

1126 /    ctrlX PLC Engineering
1344      Cyclic communication

ENUM                Description
Running             There is an active communication between server and client
 (default state in operation; includes the individual states "Receiving",
 "Received", "Transmitting", "Transmitted")
Receiving           Data is received
Received            Data reception completed
Transmitting        Data is transmitted
Transmitted         Data sending completed successfully.
ConnectionTest      Ping connection test performed
Waiting             Waiting state
ReadyToSend         Data can be sent

TimeOutRx          The configured (default = 1500 ms) timeout value was reached
TimeOutTx          The configured (default = 1500 ms) timeout value was reached
NotReadyToSend     Data cannot be sent
DataLengthError    Data package too big. Thus, "SendData" or "RecvData" is bigger than 1400
bytes
ConnectionError    Error in connection. For detailed information, refer to the "CXA_Socket‐
Comm.lib" in this documentation
ChecksumError      Incorrect data was transferred. The sent data does not match the received
data
DataTransmittin‐   Error when sending data. For detailed information, refer to the "CXA_Socket‐
gError             Comm.lib" in this documentation
DataReceivingError Error when receiving data. For detailed information, refer to the "CXA_Socket‐
Comm.lib" in this documentation

### 35.7.3 Error codes

ETHERNET_TABLE, ERROR_TABLE 16#0150

ETHERNET_TABLE, General
ETHERNET_TABLE - ERROR_TABLE, table number 16#0150

  The table contains error numbers output by:
  ● Functions and function blocks of the CXA_SocketComm.lib library
    The CXA_SocketComm library contains the functions and function blocks to
    establish a connection to and data transfer via TCP (Transmission Control
    Protocol) and UDP (User Datagram Protocol).
    The CXA_SocketComm.lib library uses SysSockets library functions, Run‐
    time error codes (CmpErrors.library).
  ● Function block IL_UdpKeys, RIL_HMI_Utilities.library
    The function block IL_UdpKeys allows the user to reliably transfer key‐
    strokes of an HMI device to the control. Connection via UDP.
  ● IL_ModbusTCPClient function block, CXA_ModbusTCP.library
    A Modbus TCP master is implemented in the IL_ModbusTCPClient function
    block. It is used to establish a connection to the ModbusTCP server.

  The table is ordered in ascending order according to increasing numbering of
  ERROR_STRUCT/Additional1.

                   Cyclic communication       1344

ETHERNET_TABLE, General, 16#00000001-16#00000212
Additional1 Additional2 ErrorID           Cause/solution
16#0000000 16#0000000 STATE_MACHINE_ERRO Invalid state of the state machine
1           0           R
16#0000000 16#0000000 INPUT_RANGE_ERROR No address at the "ValueAdr" input
4           0
16#0000000 16#0000000 INPUT_RANGE_ERROR Input "NoOfByte" is 0
5           0
16#0000001 16#0000000 INPUT_INVALID_ERROR Wrong IP syntax
0           0

16#0000001 16#0000000 COMMUNICA‐          Unknown IP address or no connection
1           0           TION_ERROR
16#0000001 16#0000000 DEVICE_ERROR        Invalid internal buffer size
2           0
16#0000004 x            OTHER_ERROR       Socket could not be created
0
16#0000004 x            OTHER_ERROR       Error when setting I/O mode
1
16#0000004 x            OTHER_ERROR       Could not connect socket to port
2
16#0000004 x            OTHER_ERROR       Socket could not go into list mode.
3
16#0000004 x            OTHER_ERROR       The incoming connection could not be
4                                         accepted
16#0000004 x            OTHER_ERROR       Error when connecting to another device.
5
16#0000004 16#0000020 OTHER_ERROR         The remote host rejected the connection
5           9                             setup. The remote host does not expect any
incoming connections at this port.
16#0000004 16#0000020 OTHER_ERROR         Timeout when establishing a connection to
5           A                             another device. The device does not respond
16#0000004 16#0000020 OTHER_ERROR         Timeout when establishing a connection to
5           B                             another device. The device was not found
16#0000004 16#0000020 OTHER_ERROR         Connection cannot be established. No net‐
5           C                             work path to the target device
16#0000020 16#0000000 INPUT_INVALID_ERROR The socket handle is invalid
2           0
16#0000020 16#0000000 INPUT_INVALID_ERROR The port number is not in a valid range.
4           0
16#0000020 16#0000000 COMMUNICA‐          The port is already assigned
7           0           TION_ERROR
16#0000020 16#0000000 INPUT_INVALID_ERROR Target address invalid
8           0
16#0000020 16#0000000 COMMUNICA‐          Remote host denied connection establish‐
9           0           TION_ERROR        ment
16#0000020 16#0000000 COMMUNICA‐          Timeout occurred.
A           0           TION_ERROR
16#0000020 16#0000000 COMMUNICA‐          Remote host not found.
B           0           TION_ERROR
16#0000020 16#0000000 COMMUNICA‐          No network path to target device found
C           0           TION_ERROR

1128 /    ctrlX PLC Engineering
1344      Cyclic communication

Additional1 Additional2 ErrorID                   Cause/solution
16#0000020 16#0000000 COMMUNICA‐                  The connection was closed.
E           0           TION_ERROR
16#0000020 16#0000000 COMMUNICA‐                  Connection interrupted by software
F           0           TION_ERROR
16#0000021 16#0000000 COMMUNICA‐                  Data package too big, address in SendDa‐
0           0           TION_ERROR                taAdr cannot be 0 or lower.
16#0000021 16#0000000 COMMUNICA‐                  The size of SizeOfSendData has to be at least
0           1           TION_ERROR                1.
16#0000021 16#0000000 COMMUNICA‐                  SizeOfSendData must not exceed 1400. A
0           2           TION_ERROR                maximum of 1400 bytes can be transmitted.
16#0000021 16#0000000 COMMUNICA‐                  Data package too big, address in RecvDa‐
0           3           TION_ERROR                taAdr cannot be 0 or lower.
16#0000021 16#0000000 COMMUNICA‐                  Size of SizeOfRecvData has to be at least 1
0           4           TION_ERROR
16#0000021 16#0000000 COMMUNICA‐                  SizeOfRecvData must not exceed 1400. A
0           5           TION_ERROR                maximum of 1400 bytes can be received.
16#0000021 16#0000000 COMMUNICA‐                  SizeOfRecvData is smaller than the amount
0           6           TION_ERROR                of the received data
16#0000021 16#0000000 COMMUNICA‐                  Remote host closed the connection
1           0           TION_ERROR
16#0000021 16#0000000 COMMUNICA‐                  Invalid protocol
2           0           TION_ERROR

             ETHERNET_TABLE, IL_TcpCyclic, IL_UdpCyclic, 16#00001001-16#00001002
Additional1 Additional2 ErrorID                   Cause/solution
16#0000100 16#0000000 COMMUNICA‐                  Data transmission error, sent data does not
1           0           TION_ERROR                correspond to the received data
16#0000100 16#0000000 COMMUNICA‐                  Unknown connection mode at the Mode input
2           0           TION_ERROR

             ETHERNET_TABLE, IL_FTPGetAsync, IL_FTPPutAsync, IL_FTPGetFileAsync, IL_FTP_Put‐
             FileAsync, 16#00002001-16#00002004
Additional1 Additional2 ErrorID                   Cause/solution
16#0000200 16#0000000 COMMUNICA‐                  Input "RemoteFile" is invalid
1           0           TION_ERROR
16#0000200 16#0000000 COMMUNICA‐                  Target buffer too small for file to be trans‐
2           0           TION_ERROR                ferred
16#0000200 16#0000007 COMMUNICA‐                  FTP server not ready
3           8           TION_ERROR
16#0000200 16#0000014 COMMUNICA‐                  Account required for login
3           C           TION_ERROR
16#0000200 16#000001A COMMUNICA‐                  Service not ready
3           5           TION_ERROR
16#0000200 16#000001A COMMUNICA‐                  Cannot open data connection
3           9           TION_ERROR
16#0000200 16#000001A COMMUNICA‐                  Connection closed and file transfer aborted
3           A           TION_ERROR
16#0000200 16#000001C COMMUNICA‐                  File not available
3           2           TION_ERROR

Cyclic communication          1344

Additional1 Additional2 ErrorID                Cause/solution
16#0000200 16#000001C COMMUNICA‐               Error during file processing on FTP server
3           3           TION_ERROR
16#0000200 16#000001C COMMUNICA‐               Insufficient memory on FTP server
3           4           TION_ERROR
16#0000200 16#000001F COMMUNICA‐               Error in command syntax
3           4           TION_ERROR
16#0000200 16#000001F COMMUNICA‐               Incorrect command parameter
3           5           TION_ERROR
16#0000200 16#000001F COMMUNICA‐               Command not implemented
3           6           TION_ERROR

16#0000200 16#000001F COMMUNICA‐               Incorrect command order
3           7           TION_ERROR
16#0000200 16#000001F COMMUNICA‐               Command with this parameter not imple‐
3           8           TION_ERROR             mented
16#0000200 16#0000021 COMMUNICA‐               Incorrect login or password
3           2           TION_ERROR
16#0000200 16#0000022 COMMUNICA‐               File not available
3           6           TION_ERROR
16#0000200 16#0000022 COMMUNICA‐               Unknown page type
3           7           TION_ERROR
16#0000200 16#0000022 COMMUNICA‐               Not sufficient memory space
3           8           TION_ERROR
16#0000200 16#0000022 COMMUNICA‐               File name not allowed
3           9           TION_ERROR
16#0000200 16#0000FFF COMMUNICA‐               Unexpected response from FTP server
3           E           TION_ERROR
16#0000200 16#0000FFF COMMUNICA‐               Unknown response from FTP server
3           F           TION_ERROR
16#0000200 16#0000000 ACCESS_ERROR             LocalFile could not be created
4           0
16#0000200 16#0000000 ACCESS_ERROR             LocalFile could not be read
4           1
16#0000200 16#0000000 ACCESS_ERROR             LocalFile could not be written
4           2
16#0000200 16#0000000 ACCESS_ERROR             LocalFile could not be closed
4           3

ETHERNET_TABLE, IL_TFTPGetFileAsync, IL_TFTPPutFileAsync,
16#00002101-16#00002108
Additional1 Additional2 ErrorID                Cause/solution
16#0000210 16#0000000 COMMUNICA‐               Input "RemoteFile" is invalid
1           0           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐               Input "LocalFile" is invalid
2           0           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐               LocalFile not found
3           0           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐               LocalFile cannot be written
4           0           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐               Error while establishing a connection
5           0           TION_ERROR

1130 /    ctrlX PLC Engineering
1344      Byte Order in IP-Based Communication

Additional1 Additional2 ErrorID                       Cause/solution
16#0000210 16#0000000 COMMUNICA‐                      Timeout during transmission
6           0           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐                      Unexpected communication error
7           0           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐                      RemoteFile not found
7           1           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐                      Access violation
7           2           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐                      Insufficient memory on FTP server
7           3           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐                      Prohibited TFTP operation
7           4           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐                      Unknown transfer ID
7           5           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐                      File already exists
7           6           TION_ERROR
16#0000210 16#0000000 COMMUNICA‐                      Unknown user
7           7           TION_ERROR
16#0000210 16#0000000 ACCESS_ERROR                    LocalFile could not be created
8           0
16#0000210 16#0000000 ACCESS_ERROR                    LocalFile could not be read
8           1
16#0000210 16#0000000 ACCESS_ERROR                    LocalFile could not be written
8           2
16#0000210 16#0000000 ACCESS_ERROR                    LocalFile could not be closed
8           3

## 35.8 Byte Order in IP-Based Communication

### 35.8.1 Introduction and overview

The byte order describes the memory organization for simple numerical
values, primarily the archiving of integers. The smallest addressable unit is
a byte. A number is stored in several bytes, whose memory addresses follow
each other directly.
● With big endianfirst byte order (literally "big end first"), the byte with the
    highest value bits (that are the most significant points) is stored first, i.e.,
    at the smallest memory address.
● With little endian first byte order (literally "small end first"), the byte with
    the lowest value bits (that are the least significant points) is stored at the
    smallest memory address.
The byte order for IP-based communication is based on the big-endian
method. As controllers store data to the memory either in big-endian or in
little-endian format, conversion functions adapted to the system are required.
The functions are provided by the SysSocket library.
The following functions are available:
● SysSockHtons: Control to network 16 bits
● SysSockNtohs: Network to control 16 bits
● SysSockHtonl: Control to network 32 bits
● SysSockNtohl: Network to control 32 bits
The following data types have to be converted for transmission via TCP or
UDP:

                                                        Error codes       1344

Data type                     Control to network    Network to control
WORD, INT, UINT               SysSockHtons()        SysSockNtohs()
DWORD, DINT, UDINT, TIME      SysSockHtonl()        SysSockNtohl()
The data types BYTE, CHAR and STRING do not have to be converted.
The byte order for the data types REAL and LREAL is not specified. The cor‐
rect setting can only be determined by trying.

## 35.9 Error codes

### 35.9.1 CXA_SocketComm - Error codes of the CXA_Table

Addtional1 is 16#0A0F0101 for all errors of the CXA_SocketComm.
Table 985: Error codes of the CXA_Table for the CXA_SocketComm
ErrorID              Additional1 Additional2 Description
OTHER_ERROR         16#0A0F010 16#0C23000 Socket handle invalid or closed
                          1           1
INPUT_RANGE_ERROR 16#0A0F010 16#0C23000 Input "ValueAdr" is not set
                          1           6
INPUT_RANGE_ERROR 16#0A0F010 16#0C23000 Input "NoOfBytes" is 0
                          1           F
RESSOURCE_ERROR     16#0A0F010 16#0C23001 No object available with this name
                          1           0
INPUT_INVALID_ERROR 16#0A0F010 16#0C23020 Invalid socket handle
                          1           2
RESSOURCE_ERROR     16#0A0F010 16#0C23020 The address is already used
                          1           7
INPUT_INVALID_ERROR 16#0A0F010 16#0C23020 Target address invalid
                          1           8
COMMUNICA‐          16#0A0F010 16#0C23020 Remote host denied connection establish‐
TION_ERROR                1           9      ment
COMMUNICA‐          16#0A0F010 16#0C23020 Timeout. No response from the addressed
TION_ERROR          1                 A      device (3 seconds)
COMMUNICA‐          16#0A0F010 16#0C23020 Remote host not found
TION_ERROR          1                 B
COMMUNICA‐          16#0A0F010 16#0C23020 No network path to target device found
TION_ERROR                1           C
COMMUNICA‐          16#0A0F010 16#0C23020 Connection was closed
TION_ERROR                1           E
COMMUNICA‐          16#0A0F010 16#0C23020 Connection interrupted by software
TION_ERROR                1           F
COMMUNICA‐          16#0A0F010 16#0C23021 Socket was closed
TION_ERROR          1                 1
OTHER_ERROR         16#0A0F010 16#0C23100 Error in the state machine of the function
                          1           0      block
OTHER_ERROR         16#0A0F010 16#0C23100 Socket could not be created
                          1           1
OTHER_ERROR         16#0A0F010 16#0C23100 Error when setting I/O mode
                          1           2
OTHER_ERROR         16#0A0F010 16#0C23100 Could not connect socket to port
                          1           3
OTHER_ERROR         16#0A0F010 16#0C23100 Socket could not be set to Listen mode.
                          1           4

1132 /    ctrlX PLC Engineering
1344      Error codes

ErrorID            Additional1 Additional2 Description
OTHER_ERROR        16#0A0F010 16#0C23100 Could not accept incoming connection.
1           5
OTHER_ERROR        16#0A0F010 16#0C23100 Error when connecting to another device.
1           6
INPUT_RANGE_ERROR 16#0A0F010 16#0C23100 Invalid port
1           7
INPUT_RANGE_ERROR 16#0A0F010 16#0C23100 SizeOfRecvData must not exceed 1400. A
1           8      maximum of 1400 bytes can be received.
COMMUNICA‐         16#0A0F010 16#0C23100 Unknown connection mode at the Mode
TION_ERROR              1           9      input.
STATE_MACHINE_ERRO 16#0A0F010 16#0C23100 Error in state machine
R                       1           A
COMMUNICA‐         16#0A0F010 16#0C23100 Input "RemoteFile" is invalid
TION_ERROR              1           B
COMMUNICA‐         16#0A0F010 16#0C23100 Input "LocalFile" input is invalid
TION_ERROR              1           C
COMMUNICA‐         16#0A0F010 16#0C23100 "LocalFile" not found
TION_ERROR              1           D
COMMUNICA‐         16#0A0F010 16#0C23100 "LocalFile" could not be written
TION_ERROR              1           E
COMMUNICA‐         16#0A0F010 16#0C23100 "RemoteFile" not found
TION_ERROR              1           F
COMMUNICA‐         16#0A0F010 16#0C23101 Access violation on the remote host
TION_ERROR              1           0
COMMUNICA‐         16#0A0F010 16#0C23101 Prohibited TFTP operation
TION_ERROR              1           2
COMMUNICA‐         16#0A0F010 16#0C23101 Unknown transfer ID
TION_ERROR              1           3
COMMUNICA‐         16#0A0F010 16#0C23101 Unknown user
TION_ERROR              1           5
COMMUNICA‐         16#0A0F010 16#0C23101 Unexpected communication error
TION_ERROR              1           6
COMMUNICA‐         16#0A0F010 16#0C23101 Timeout during data transmission
TION_ERROR              1           8
COMMUNICA‐         16#0A0F010 16#0C23101
TION_ERROR              1           A
COMMUNICA‐         16#0A0F010 16#0C23200 Input "RemoteFile" is invalid
TION_ERROR              1           1
COMMUNICA‐         16#0A0F010 16#0C23200 Target buffer too small for file to be trans‐
TION_ERROR              1           2      ferred
COMMUNICA‐         16#0A0F010 16#0C23207 FTP server not ready
TION_ERROR              1           8
COMMUNICA‐         16#0A0F010 16#0C23214 Account required for login
TION_ERROR              1           C
COMMUNICA‐         16#0A0F010 16#0C2321A Service not ready
TION_ERROR              1           5
COMMUNICA‐         16#0A0F010 16#0C2321A Cannot open data connection
TION_ERROR              1           9
COMMUNICA‐         16#0A0F010 16#0C2321A Connection closed and file transfer aborted
TION_ERROR              1           A

                                            Introduction and overview       1344

ErrorID                      Additional1 Additional2 Description
COMMUNICA‐                   16#0A0F010 16#0C2321C File not available
TION_ERROR                        1           2
COMMUNICA‐                   16#0A0F010 16#0C2321C Error during file processing on FTP server
TION_ERROR                        1           3
COMMUNICA‐                   16#0A0F010 16#0C2321C Insufficient memory on FTP server
TION_ERROR                        1           4
COMMUNICA‐                   16#0A0F010 16#0C2321F Error in command syntax
TION_ERROR                        1           4
COMMUNICA‐                   16#0A0F010 16#0C2321F Incorrect command parameters
TION_ERROR                        1           5

COMMUNICA‐                   16#0A0F010 16#0C2321F Command not implemented
TION_ERROR                        1           6
COMMUNICA‐                   16#0A0F010 16#0C2321F Incorrect command order
TION_ERROR                        1           7
COMMUNICA‐                   16#0A0F010 16#0C2321F Command with this parameter not imple‐
TION_ERROR                        1           8      mented
COMMUNICA‐                   16#0A0F010 16#0C23221 Incorrect login or password
TION_ERROR                        1           2
COMMUNICA‐                   16#0A0F010 16#0C23222 File not available
TION_ERROR                        1           6
COMMUNICA‐                   16#0A0F010 16#0C23222 Unknown page type
TION_ERROR                        1           7
COMMUNICA‐                   16#0A0F010 16#0C23222 Insufficient memory
TION_ERROR                        1           8
COMMUNICA‐                   16#0A0F010 16#0C23222 File name not allowed
TION_ERROR                        1           9
COMMUNICA‐                   16#0A0F010 16#0C23FFF Unexpected response from FTP server
TION_ERROR                        1           E
COMMUNICA‐                   16#0A0F010 16#0C23FFF Unknown response from FTP server
TION_ERROR                        1           F
