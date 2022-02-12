import socket

host = 'localhost'
port = 56789

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

requests = [
        "image_search", "site_search", "presentation_software_search", "video_search", "book_search"
        ]
req_index = 0

while True:
    print("The server is accessible to port : {}".format(port))

    (sClient, addrClient) = server.accept()
    print("Client address: {}".format(addrClient))

    try :
        while True:
            if req_index == 5:
                req_index = 0

            data = sClient.recv(2048)
            if data == '' or data.decode() == "bye":
                break

            req = requests[ req_index ]

            sClient.send( req.encode() )
            print(f"[Server][Task out] {req} sent to preparation")
            data = sClient.recv(2048).decode()
            if data:
                print(f"[Server][Task in] {data} prepared")

            req_index = req_index + 1

        sClient.close()

    except socket.error:
        print("---- Socket Error ----")
s.close()


