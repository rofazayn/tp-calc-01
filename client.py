import socket
import os
import time

client = str( os.getpid() )

def prepare_seq( steps, task ):
    prep_time = steps[task]
    print(f"[Client-{client}][] {task} in preparation for ({prep_time}s)...")
    time.sleep( prep_time )
    return task

STEPS = {
        "site_search": 2,
        "book_search": 3,
        "image_search": 2,
        "video_search": 1,
        "presentation_software_search": 2,
        }

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect(("localhost", 56789))

i = 0
while i < 2:
    msg1 = "test connection" + client
    Client.sendall( msg1.encode("ascii") )

    data = Client.recv(2048).decode()
    print(f"[Client-{client}][Task in] {data} to prepare received")
    msg = prepare_seq( STEPS, data)
    Client.sendall( msg.encode() )
    print(f"[Client-{client}][Task out] {data} ready sent")
    i = i + 1

Client.close()

