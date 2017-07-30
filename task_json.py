import json
foodyo=json.loads(open('foodyo_output.json').read())
def recurr(dic,n):
    if dic['selected']==1:
        print("-"*n,">",dic['name'])
        n=n+2
        l=dic['children']
        for v in l:
            recurr(v,n)
        
for i in foodyo['body']['Recommendations']:
    name=i['RestaurantName']
    print("-->",name)
    li=i['menu']
    for j in li:
        if j['type']=='sectionheader':
            lis=j['children']
            for k in lis:
                if k['type']=='item' and k['selected']==1:
                    print("----->",k['name'])
                    lists=k['children']
                    for m in lists:
                        recurr(m,7)
                
        
