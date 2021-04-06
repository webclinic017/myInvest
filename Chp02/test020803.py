BUF_SIZE = 1024

with open('d:\sda1\src.png', 'rb') as sf, open('d:\sda1\dst.png', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
        df.write(data)
