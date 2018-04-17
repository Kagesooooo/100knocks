all_cnt = 0
ok_cnt = 0
with open('output/92.txt')as f:
    for sen in f:
        words = sen.split()
        if len(words) == 5:
            continue
        elif words[3] == words[4]:
            ok_cnt += 1
        else:
            pass
        all_cnt += 1
print(str(ok_cnt/all_cnt)+'%')
print(str(ok_cnt)+'/'+str(all_cnt))
