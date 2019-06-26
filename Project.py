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
print(dist1)

dist2=[]
for y in obj:
    dist2.append(abs(int(samples[1].gender)-int(y.gender))+abs(int(samples[1].age)-int(y.age))+abs(int(samples[1].income)-int(y.income))+abs(int(samples[1].score)-int(y.score)))
print(dist2)
for i in range(len(dist1)):
    if dist1[i]<=dist2[i]:
               obj[i].clusterno=1
    elif dist1[i]>dist2[i]:
               obj[i].clusterno=2
arsum=0
arsum1=0
j=0
i=0
for  y in obj:
    if y.clusterno==1:
        print ("cluster 1",y.age)
        arsum+=int(y.age)
        i+=1
    elif y.clusterno==2:
        print ("cluster 2",y.age)
        arsum1+=int(y.age)
        j+=1
arsum=arsum/i
arsum1=arsum1/j
print ("cluster 1",arsum)
print ("cluster 2",arsum1)   

               
