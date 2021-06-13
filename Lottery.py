import datetime

aviya=209203991
idan=208057505
lihi=206902736
matan=205639800

#-------------Question between 1-9----------#
sec=datetime.now().second
total=sec+aviya%10

while total>10 :
    while total<0:
        total+=aviya%10
    total-=aviya%10

print("Question chosen: "+total)


