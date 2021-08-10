import hashlib

text = 'xiongyangyang17621847970'
text_sha256 = hashlib.sha256(text.encode('utf-8')).hexdigest()
print(f'text_sha256--{text_sha256}')


text_sha1 = hashlib.sha1(text.encode('utf-8')).hexdigest()
print(f'text_sha1--{text_sha1}')


text_md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
print(f'text_md5--{text_md5}')