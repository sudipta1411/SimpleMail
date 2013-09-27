import PopUp

import smtp_server

def main() :
    popup = PopUp.PopUp()
    popup.main()
    print smtp_server.Server.get()

if __name__ == '__main__':
    main()