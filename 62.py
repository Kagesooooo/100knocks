import plyvel

db = plyvel.DB('./db_test/', create_if_missing=True)

cnt = 0
for _, value in db:
    if value == 'Japan'.encode():
        cnt += 1

print(cnt)
