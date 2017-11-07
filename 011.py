with open('hightemp.txt','r', encoding='utf-8') as f:
    print(f.read().replace('\t',' ').strip())

# sed 's/<control+v><tab>/ /g' hightemp.txt
