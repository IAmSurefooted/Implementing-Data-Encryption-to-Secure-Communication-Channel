#!/usr/bin/python3
# Author:
# 	Suraj Singh Bisht
#

from src import ask_mode as ask, client_mode as client, server_mode as server

if __name__ == '__main__':
    tmp_obj = ask.ask_ip_dialog()
    if tmp_obj == 0:
        client.ClientDialogBox(
            className='Chatting [Client Window]').mainloop()
    else:
        server.ServerDialogBox(className='Chatting [Server Window]').mainloop()
