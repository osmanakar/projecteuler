with open('basic_problems/1000_digit_number') as namefile:
    data=namefile.read()
    
data=data.replace("\n","")

answer=0
for i in range(0,987):
    temp=1
    for j in range(i,i+13):
        temp=temp*int(data[j])
    if temp>answer:
        answer=temp

print(answer)
