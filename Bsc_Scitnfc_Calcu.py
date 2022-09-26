
##Avarage:
lst=[]
a=int((input("No. of Element you want:")))
for i in range(a):
     user=int(input("Enter value:"))
     lst.append(user)
print(sum(lst)/a)

##Factorial:
a=int(input("Enter value:"))
b=1
for i in range(1,a+1):
     b=b*i
     print(b)

##Dataset:
a={"channel":{"id":875453,"name":"NODEMCU","latitude":"0.0","longitude":"0.0","field1":"Humidity","field2":"Temperature","created_at":"2019-09-30T06:57:17Z","updated_at":"2022-03-21T11:21:39Z","last_entry_id":665},"feeds":[{"created_at":"2022-03-21T11:57:39Z","entry_id":661,"field1":"24.00000","field2":'null'},{"created_at":"2022-03-21T11:57:57Z","entry_id":662,"field1":"24.00000","field2":'null'},{"created_at":"2022-03-21T11:58:16Z","entry_id":663,"field1":"25.00000","field2":'null'},{"created_at":"2022-03-21T11:58:35Z","entry_id":664,"field1":"25.00000","field2":'null'},{"created_at":"2022-03-21T11:59:36Z","entry_id":665,"field1":"25.00000","field2":'null'}]}
c=a['channel']
d=a['feeds']
print("Data channel:")
print("Data from created_at:",c['created_at'],'Data from fiels1:',c['field1'])
print("Data feeds:")
for i in range(len(d)):
    print("Data from created_at:",d[i]['created_at'],'Data from fiels1:',d[i]['field1'])
##lucky draw:
#while 1:
    user = int(input("Enter your lucky number:"))
    if user == 44:
        print("Congratulations you won lottery......")
    else:
        print("Better luck next time")
