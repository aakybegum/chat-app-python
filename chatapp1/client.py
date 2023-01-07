from socket import *
from threading import *
from tkinter import *

client = socket(AF_INET, SOCK_STREAM)

HOST = '192.168.1.108'
PORT = 5039
client.connect((HOST, PORT))

pencere = Tk()
pencere.title('ChatRoom')
pencere.iconbitmap("C:\speech-bubble.ico")

messages = Text(pencere, width=50)
messages.grid(row=0, column=0, padx=10, pady=10)

yourMessage = Entry(pencere, width=50)
yourMessage.insert(0, 'Name')
yourMessage.grid(row=1, column=0, padx=10, pady=10)
yourMessage.focus()
yourMessage.selection_range(0, END)

menu = Menu(pencere)
pencere.config(menu=menu)

dosya = Menu(menu)
dosya = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=dosya)
dosya.add_command(label="Open")
dosya.add_command(label="Exit", command=pencere.quit)
dosya = Menu(menu, tearoff=0)


def sendMessage(event=None):
    clientMessage = yourMessage.get()
    messages.insert(END, '\n' + 'You: ' + clientMessage)
    client.send(clientMessage.encode('utf-8'))
    yourMessage.delete(0, END)


yourMessage.bind("<Return>", sendMessage)


def recvMessage():
    while True:
        serverMessage = client.recv(1024).decode('utf-8')
        messages.insert(END, '\n' + serverMessage)


recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()

messages = Text(pencere, width=50, bg="misty rose")
messages.grid(row=0, column=0, padx=10, pady=10)

login_btn = PhotoImage(file="C:\p-send.png")

img_label = Label(image=login_btn)

my_button = Button(pencere, image=login_btn, command=sendMessage,
                   borderwidth=0, width=300, height=40)
my_button.grid(pady=10)

my_label = Label(pencere, text="")
my_label.grid(pady=1)

pencere.mainloop()
