import hlextend
from base64 import b64decode, b64encode
import socket

def recvuntil(clientSocket, string):
    output = b'' 
    while True:
        output += clientSocket.recv(8092).rstrip()       
        if string in output:
            return output

def solve():
    host, port = '13.59.250.77', 8020
    # host, port = 'localhost', 8000
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSock.connect((host, port))

    #order
    output = recvuntil(clientSock, b'Your choice:')
    clientSock.sendall(b'2\n')
    output = recvuntil(clientSock, b'ID:')
    clientSock.sendall(b'6\n')
    output = recvuntil(clientSock, b'Your choice:')
    order = output.split(b'\n')[0][len('Your order:'):].strip()
    order = b64decode(order).decode('latin-1')

    sp = order.rfind('&sign=')
    sign = order[sp+6:]
    payment = order[:sp]
    append_msg = '&price=0'
    

    for i in range(8, 33):
        sha = hlextend.new('sha512')
        new_payment = sha.extend(append_msg, payment, i, sign)
        new_sign = sha.hexdigest()
        new_order = new_payment + b'&sign=' + new_sign.encode()
        new_order = b64encode(new_order)

        #confirm order
        clientSock.sendall(b'3\n')
        output = recvuntil(clientSock, b'Your order:')
        clientSock.sendall(new_order + b'\n')
        output = recvuntil(clientSock, b'Your choice:')
        if b'FUSec{' in output:
            flag = output.decode()[output.index(b'FUSec{'):output.index(b'}')+1]
            print(flag)
            break
    

def test():
    from hashlib import sha512
    known_msg = 'product=FLAG&price=99999&time=1633744784.98'
    secret_msg = '3H0XfrdRDl7ceGBM2kc0e'
    hashed_msg = '1119731cf1ff1adc30c90222a05cb96c5022613d01ad49c297b3e408dd542b3a'
    append_msg = '&price=0'

if __name__=="__main__":
    solve()