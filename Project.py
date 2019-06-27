#import necessary modules
import csv
import random
class mall:
    def __init__(self,id,gender,age,income,score):
        self.id=id
        self.gender=gender
        self.age=age
        self.income=income
        self.score=score
        self.clusterno=0
with open('./Mall_Customers.csv','rt')as f:
  data = csv.reader(f)
  d=list(data)
  s= len(d)
  obj=[]
  for i in range(1,s):  
      obj.append(mall(d[i][0],d[i][1],d[i][2],d[i][3],d[i][4]))
for j in obj:
    #1 if male 0 if female
    if j.gender=="Male":
        j.gender=1
    elif j.gender=="Female":
        j.gender=0
    print (j.id,j.gender,j.age,j.income,j.score)
samples=[]
def random_values(obj):
    global samples
    samples=random.choices(obj,k=2)
    print ("Centroid 1 :- ",samples[0].id,samples[0].gender,samples[0].age,samples[0].income,samples[0].score,"Centroid 2:- ",samples[1].id,samples[1].gender,samples[1].age,samples[1].income,samples[1].score)

random_values(obj)
    
dist1=[]
for x in obj:
    dist1.append(abs(int(samples[0].gender)-int(x.gender))+abs(int(samples[0].age)-int(x.age))+abs(int(samples[0].income)-int(x.income))+abs(int(samples[0].score)-int(x.score)))

dist2=[]
for y in obj:
    dist2.append(abs(int(samples[1].gender)-int(y.gender))+abs(int(samples[1].age)-int(y.age))+abs(int(samples[1].income)-int(y.income))+abs(int(samples[1].score)-int(y.score)))
for i in range(len(dist1)):
    if dist1[i]<=dist2[i]:
               obj[i].clusterno=1
    elif dist1[i]>dist2[i]:
               obj[i].clusterno=2
print("CLUSTER 1:")
for x in obj:
    if x.clusterno==1:
        print (x.id,x.gender,x.age,x.income,x.score)
print("CLUSTER 2:")
for y in obj:
    if y.clusterno==2:
        print (y.id,y.gender,y.age,y.income,y.score)

gsum=0
gsum1=0
arsum=0
arsum1=0
isum=0
isum1=0
scsum=0
scsum1=0
j=0
i=0
for  y in obj:
    if y.clusterno==1:
        gsum+=int(y.gender)
        arsum+=int(y.age)
        isum+=int(y.income)
        scsum+=int(y.score)
        i+=1
    elif y.clusterno==2:
        gsum1+=int(y.gender)
        arsum1+=int(y.age)
        isum1+=int(y.income)
        scsum1+=int(y.score)
        j+=1
gsum=gsum/i
gsum1=gsum1/j
arsum=arsum/i
arsum1=arsum1/j
isum=isum/i
isum1=isum1/j
scsum=scsum/i
scsum1=scsum1/j
print ("mean of cluster 1:",gsum,arsum,isum,scsum)
print ("mean of cluster 2:",gsum1,arsum1,isum1,scsum1)   

               
