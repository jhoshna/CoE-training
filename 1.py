basic = int(input("enter the basic salary"))
if basic < 10000:
    hra = (67 / basic)*10
    da = (73 / basic)*100
elif basic < 20000:
    hra = (69 / basic)*100
    da = (76 / basic)*100
else:
    hra = (73/basic)*100
    da = (89/basic)*100
gs = hra + da + basic
print(gs)