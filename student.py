from csv import *
from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 

#gui
window=Tk()
window.title("Data Entry")
window.geometry("700x350")
main_lst=[]

def Save():
   with open("Student_Scores.csv","w",newline="") as file:
      lst=[Hours.get(),Scores.get()]
      main_lst.append(lst)
      Writer=writer(file)
      Writer.writerow(["Hours","Scores"])
      Writer.writerows(main_lst)
      messagebox.showinfo("Information","Saved succesfully")

def Clear():
   Hours.delete(0,END)
   Scores.delete(0,END)


# gui layouts
label1=Label(window,text="Hours: ",padx=20,pady=10)
label2=Label(window,text="Scores: ",padx=20,pady=10)

Hours=Entry(window,width=30,borderwidth=3)
Scores=Entry(window,width=30,borderwidth=3)


save=Button(window,text="Save",padx=20,pady=10,command=Save)
clear=Button(window,text="Clear",padx=18,pady=10,command=Clear)
Exit=Button(window,text="Exit",padx=20,pady=10,command=window.quit)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)

Hours.grid(row=0,column=1)
Scores.grid(row=1,column=1)
save.grid(row=4,column=0,columnspan=2)
clear.grid(row=5,column=0,columnspan=2)
Exit.grid(row=6,column=0,columnspan=2)

window.mainloop()

#dataset reading
df = pd.read_csv ('Student_Scores.csv')
print(df)

#simple linear regression to predict the data
X = df.iloc[:,:-1].values 
y = df.iloc[:,-1].values 
from sklearn.model_selection import train_test_split 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.30,random_state=0) 
from sklearn.linear_model import LinearRegression 
regressor = LinearRegression() 
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test) 
print(y_pred)

#Comparing Actual vs Predicted Value
df1 = pd.DataFrame({'Actual':y_test ,'Predicted_Score':y_pred}) 
print(df1)

#Visualizing Actual scores and predicted scores
plt.scatter(X_train,y_train,color ='blue')
plt.plot(X_train,regressor.predict(X_train),color="red")
plt.title('(Training set)') 
plt.xlabel('Hours') 
plt.ylabel('Scores') 
plt.show() 

#categorising students who failed and passed
cut_off = 40 
df['Result'] = df['Scores'] >= cut_off
df["Result"] = df["Result"].astype(str) 
df.Result = df.Result.replace({"True" :"Passed","False":"Failed"}) 
print(df) 
print(df[ "Result" ].value_counts())
Results = [ ' Passed ' , ' Failed ' ] 
data = [df[ "Result" ].value_counts().Passed, df[ "Result" ].value_counts().Failed] 
colors = ( "Green" , "red" ) 
wp = { 'linewidth': 1 , 'edgecolor' : 'green' } 
# Creating autocpt arguments
def func(pct , allvalues): 
    absolute = int ( pct / 100. * np.sum ( allvalues )) 
    return '{:.1f}%\n({:d}g)'.format(pct,absolute)
# Creating plot 
fig , ax = plt.subplots ( figsize =(15,10)) 
wedges,texts , autotexts = ax.pie(
data,
autopct= lambda pct : func(pct,data),
labels= Results,
shadow = True,  
colors = colors , 
startangle = 90 , 
wedgeprops = wp , 
textprops = dict( color = "black")
)
#Adding Legend 
ax.legend ( wedges,Results, 
title = "Results", 
loc ="center left", 
bbox_to_anchor = (1,0)) 
plt.setp (autotexts,size=8,weight="bold") 
ax.set_title("Students Results") 
# show plot 
plt.show()