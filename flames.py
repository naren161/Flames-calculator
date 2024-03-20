print("Hi welcome to the This Game ")
name1 = input("Enter your name1 :").lower()
name2 = input("Enter your name2 :").lower()
name1 = name1.replace(" ","")
name2 = name2.replace(" ","")
for i in name1:
  for j in name2:
    if(i==j):
      name1=name1.replace(i,"",1)
      name2=name2.replace(j,"",1)
      break

count=len(name1+name2)
print(count)
if count>0:
  flames=['f','l','a','m','e','s']
  while len(flames)>1:
    formula = count%len(flames)
    index = formula-1
    if index>=0:
      left = flames[:index]
      right = flames[index+1:]
      flames = right+left
    else:
      flames = flames[:len(flames)-1]
  print("YOUR RELATIONSHIP BETWEEN",name1,"and",name2,"is",flames[0] )
else:
  print("Enter different names")
