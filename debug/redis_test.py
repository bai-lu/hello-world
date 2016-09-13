from redis import Redis
db=Redis(host='192.168.15.132', port=6379, db=0)
print(db.dbsize())
for key in db.keys():
    title=db.hkeys(key)[0]
    content=db.hgetall(key)[title]
    print(key.decode('utf-8'))
    print(title.decode('utf-8'))
    print(content.decode('utf-8'))
# db.save()
db.flushdb()
