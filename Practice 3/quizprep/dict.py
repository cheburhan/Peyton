num = list (map (int, input().split()))
dic = {}
for i in num:
    dic[i] = dic.get (i, 0) + 1
print (dic)