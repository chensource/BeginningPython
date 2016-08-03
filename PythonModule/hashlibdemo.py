import hashlib

md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
print(md5.hexdigest())

#模拟用户登录
db= {}
def get_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

def calc_md5(username,password):
    return get_md5(username+password+'centanet')

def register(username,password):
    db[username] = calc_md5(username, password)

def login(username,password):
    pwd = db.get(username)
    if not pwd:
        print('user is not defind')
    else:
        if calc_md5(username, password) == pwd:
            print('login success')
        else:
            print('login fail. may be password is error')
register('chens', '12345678')

login('chens', '12345678')
login('chens1', '12345')
login('chens', '1234')
