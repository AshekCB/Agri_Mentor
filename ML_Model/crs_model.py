#Importing needed Libraries
import pandas as pd#For Data Handling.
from sklearn.model_selection import train_test_split#For Data Seperation.
from sklearn.ensemble import RandomForestClassifier # Ensembling technique RandomForestClassifier.


#data Loading
df=pd.read_csv("D:\Flask Demo's\Crop Recommendation System [CRS]\Source Codes\Crop_recommendation.csv")

#Feature Extraction
#independent feature
x=df.drop('label',axis=1)
#dependent
y=df['label']

#Data Splitting
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
 #splitting
 #Training:70
 #Testing:30

#modeldefination
model=RandomForestClassifier(n_estimators=100,criterion="gini")#model defination

#model training
model.fit(x_train,y_train)


 #prediction method
def Crop_Recommendation_System(N,P,K,temperature,humidity,ph,rainfall):
  
  data={
      'N':N,
      'P':P,
      'K':K,
      'temperature':temperature,
      'humidity':humidity,
      'ph':ph,
      'rainfall':rainfall
  }
  test_data=pd.DataFrame(data,index=[0])
  result=model.predict(test_data)
  crop=str(result[0].title())
  return crop

'''
N - ratio of Nitrogen content in soil.
P - ratio of Phosphorous content in soil.
K - ratio of Potassium content in soil.
temperature - temperature in degree Celsius.
humidity - relative humidity in %.
ph - ph value of the soil.
rainfall - rainfall in mm.
'''
#test case 1

'''
#testing the prediction function
crop=Crop_Recommendation_System(2,21,35,25.0288,91.5372,6.293,179.8248)
print("The Recommended Crop for the given details are : ",crop)
#result --> Coconut
'''

'''
#test case 2
crop=Crop_Recommendation_System(93,94,53,25.8663,84.424,6.079,111.4535)
print("The Recommended Crop for the given details are : ",crop)
#result --> Banana
'''

#print(Crop_Recommendation_System(93,94,53,25.8663,84.424,6.079,111.4535))
