import plyvel

db = plyvel.DB('./db_test/', create_if_missing=True)

for key, value in db:
    if 'Oasis' == (key.decode()).split('\t')[0]:
        print(value.decode())
