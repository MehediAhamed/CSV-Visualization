from turtle import width
import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('data.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(float((row[0])))
        y.append(float((row[1])))
        print(x)
        
plt.bar(x, y, color = 'r', 
         width=0.80,label = "Data")

plt.xlabel('X AXIS')
plt.ylabel('Y AXIS')
plt.title('DATA VISUALIZATION', fontsize = 30)

plt.legend()
plt.show()
