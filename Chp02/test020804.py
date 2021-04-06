import hashlib

sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

with open('src.png', 'rb') as sf, open('dst.png', 'rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())

print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dst.png's hash : {}".format(sha_dst.hexdigest()))
