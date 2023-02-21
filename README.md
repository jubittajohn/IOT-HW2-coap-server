# CoAP SERVER excecution
The file IOT_HW2-coap-server has the following data:
- Server.py - Program code for coap server
- DataFiles - This folder contains the 4 different datafiles that are to be transmitted to the client on request.

## Library used
- aiocoap in python

## Required installations
- install aiocoap library using the following command

    ```  pip3 install aiocoap```

## How to excute CoAP server
- Host name is predefined to '127.0.0.1'. So no changes are required to be made in CoAP server.
- Directly run the server and the http server is now ready to receive request from client

## What happens in CoAP server
-  The following will be output by the CoAP server when it receives a PUT request from the client:

    ``` PUT -  1MB  - CoAP```
-   The entire data is read at once from the file and is transferred using block transfer which is an inbuilt functionality in aiocoap.
- This is an asynchronous file transfer mechanism using confirmable(CON) messages.