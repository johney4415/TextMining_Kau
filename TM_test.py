news = ["今天天氣好好，好想去打球，梅西", "梅西昨天進了兩球，西甲冠軍今年是巴薩", "今天想去巴薩打球，西甲"]
dic ={0:"今天",1:"天氣",2:"好好",3:"好想",4:"打球",5:"梅西",6:"昨天",7:"進了兩球",8:"西甲",9:"巴薩"}
diclist = ["今天","天氣","好好","好想","打球","梅西","昨天","進了兩球","西甲","巴薩"]

f = [[0]*5 for d in range(5)]
#f[0][0] = 1

print(id(f[0][0])==id(f[1][0]))
final = [[0]*len(dic)for d in range(len(dic))]

for k in range(len(news)):
    for i in range(len(dic)-1):
        for j in range((i+1), len(dic)):
            if dic[i] in news[k] and dic[j] in news[k]:
                #print(dic[i],dic[j],news[k])
                final[i][j] += 1

for i in range(len(dic) - 1):
    for j in range((i + 1), len(dic)):
        if final[i][j] > 0:
            print(dic[i], dic[j], final[i][j])









print(final)

