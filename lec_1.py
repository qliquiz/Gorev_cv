import numpy as np
import matplotlib.pyplot as plt
import socket


host = '84.237.21.36'
port = 5152

def recvall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return
        data.extend(packet)
    return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))

    # for i in range(10):
    sock.send(b'get')
    bts = recvall(sock, 40002)

    """ im1 = np.frombuffer(bts[2:40002], dtype='uint8').reshape(bts[0], bts[1])
    im2 = np.frombuffer(bts[40004:], dtype='uint8').reshape(bts[40002], bts[40003])

    pos1 = np.unravel_index(np.argmax(im1), im1.shape)
    pos2 = np.unravel_index(np.argmax(im2), im2.shape)

    res = np.abs(np.array(pos1) - np.array(pos2))

    sock.send(f'{res[0]} {res[1]}'.encode())
    print(sock.recv(20)) """

    im = np.frombuffer(bts[2:40002], dtype='uint8').reshape(bts[0], bts[1])

    # pos1 = np.unravel_index(np.argmax(im), im.shape)
    # im[np.unravel_index(np.argmax(im), im.shape)] = im[np.unravel_index(np.argmin(im), im.shape)]
    # pos2 = np.unravel_index(np.argmax(im), im.shape)

    for i in range(2001):
        for j in range(2001):
            pos1 = max(pos1, im[i])
            pos1 = max(pos1, im[i])

    res = round((np.sqrt((pos2[0] - pos1[0])**2 - (pos2[1] - pos1[1])**2)), 1)

    sock.send(f'{res}'.encode())
    print(sock.recv(20))

    sock.send(b'beat')
    beat = sock.recv(20)
    print(beat)

    """ plt.subplot(121)
    plt.title(f'{pos1}')
    plt.imshow(im1, cmap='hot')
    plt.subplot(122)
    plt.title(f'{pos2}')
    plt.imshow(im2, cmap='hot')
    plt.show() """

    # plt.subplot(121)
    # plt.imshow(im, cmap='hot')
    # plt.show()