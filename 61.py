import plyvel

db = plyvel.DB('./db_test/', create_if_missing=True)

print(db.get('The Silhouettes\t101060'.encode()))
