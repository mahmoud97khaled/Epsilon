from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FloatField , SubmitField , StringField , SelectField,TimeField
from wtforms.validators import DataRequired , Regexp
import pandas as pd
import numpy as np
import seaborn as sns
import datetime
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import pickle
from sklearn.ensemble import RandomForestRegressor
from decimal import Decimal


app = Flask (__name__,template_folder='template')
app.config ['SECRET_KEY'] = "SEEEECREET"


class NamerForm (FlaskForm):
    stroke = SelectField("Stroke Type",choices=[('Freestyle', 'Freestyle'), ('Backstroke', 'BackStroke'), ('Breaststroke', 'Breaststroke'), ('Butterfly', 'Butterfly')],validators = [DataRequired()] )    
    distance = SelectField("Distance",choices=[('400', '400 m '),('200', '200 m '),('100', '100 m '), ('50', '50m')],validators = [DataRequired()] )
    Number = StringField("Put the target time in that format 00:00.00",validators = [DataRequired(), Regexp('^[0-5][0-9]:[0-5][0-9].[0-9]{2}$')] )
    Gender = SelectField("Gender",choices=[('0', 'Male'), ('1', 'Female')],validators = [DataRequired()] )    
    Course = SelectField("Course",choices=[('0', 'Long'), ('1', 'Short')],validators = [DataRequired()] )    
    Age = FloatField("Age",validators = [DataRequired()] )  

    Get_result = SubmitField ('Get result')
    
def convert(convert):
    lss = convert.split(':')
    mins = float(lss[0])*60
    sec = float(lss[1])
    convert = float(mins) + sec
    return convert
    

def reverse(seconds):
    minutes = int(seconds // 60)
    seconds %= 60
    return (f'0{minutes}:{round(seconds,2)}')

def gender (x):
    if x == 'Male':
        return 0
    else :
        return 1

@app.route ('/', methods = ['GET', 'POST'])
def Data ():
    Number = None
    stroke = None
    distance = None
    Age = None
    Gender = None
    Course = None
    pred1 = None
    predc1 = None
    pred2 = None
    predc2 = None
    pred3 = None
    predc3 = None
    pred4 = None
    predc4 = None
    pred5 = None
    predc5 = None
    pred6 = None
    predc6 = None
    pred7 = None
    predc7 = None
    pred8 = None
    predc8 = None
    pred9 = None
    predc9 = None
    pred10 = None
    predc10 = None
    pred11 = None
    predc11 = None
    pred12 = None
    predc12 = None
    pred13 = None
    predc13 = None
    pred14 = None
    predc14 = None

    form = NamerForm()
    filename = 'model_100m.sav'
    filename_2 = 'model_200m.sav'
    filename_3 = 'model_400m.sav'

    # load the model from disk	
    loaded_model = pickle.load(open(filename, 'rb'))
    loaded_model_2 = pickle.load(open(filename_2, 'rb'))
    loaded_model_3 = pickle.load(open(filename_3, 'rb'))
    dic = {'Butterfly':2,'Breaststroke':1,'Backstroke':0,'Freestyle':3}
#	required = [[dic['Freestyle'],0,58,350000]]


    if form .validate_on_submit():
        Number = form.Number.data
        Age = form.Age.data
        Course = form.Course.data
        Gender = form.Gender.data
        stroke = form.stroke.data
        form.stroke.data =  ''
        distance = form.distance.data
        form.distance.data =  ''
        if distance == '100':
            required = [[int(Age),int(Course),int(distance),gender(Gender),dic[stroke],convert(Number)]]
            num = loaded_model.predict(required)
            pred1 = round(float(num[0]),2)
            predc1 = reverse(pred1)
            pred2 = abs(round(convert(Number)- (pred1),2))
            predc2 = reverse(pred2)
                    

        elif distance == '200':
                
            required_2 = [[int(Age),int(Course),int(distance),gender(Gender),dic[stroke],convert(Number)]]
            num_2 = loaded_model_2.predict(required_2)
            pred6= round(float(convert(Number)- (num_2[0][0] +num_2[0][1]+num_2[0][2])),2)
            predc6 = reverse(pred6)
            pred3 = round(num_2[0][0],2)
            predc3 = reverse(pred3)
            pred4= round(num_2[0][1],2)
            predc4 = reverse(pred4)
            pred5= round(num_2[0][2],2)
            predc5 = reverse(pred5)
        elif distance == '400':
            required_3 = [[int(Age),int(Course),int(distance),gender(Gender),dic[stroke],convert(Number)]]
            num_3 = loaded_model_3.predict(required_3)
            pred7 = round(num_3[0][0],2)
            predc7 = reverse(pred7)
            pred8= round(num_3[0][1],2)
            predc8 = reverse(pred8)
            pred9= round(num_3[0][2],2)
            predc9 = reverse(pred9)
            pred10 = round(num_3[0][3],2)
            predc10 = reverse(pred10)
            pred11= round(num_3[0][4],2)
            predc11 = reverse(pred11)
            pred12= round(num_3[0][5],2)
            predc12 = reverse(pred12)
            pred13= round(num_3[0][6],2)
            predc13 = reverse(pred13) 
            pred14= round(float(convert(Number)- (num_3[0][0] +num_3[0][1]+num_3[0][2]+num_3[0][3]+num_3[0][4]+num_3[0][5]+num_3[0][6])),2)
            predc14 = reverse(pred14)
        
        form.Number.data =  ''

    return render_template("home.html",Number = Number,stroke = stroke,Age = Age,Course = Course, Gender = Gender,pred1 = pred1,pred2 = pred2,predc1 = predc1,predc2 = predc2,pred3 = pred3,predc3 = predc3,predc4 = predc4,predc5 = predc5,pred4 = pred4,pred5 = pred5,pred6=pred6,predc6 = predc6,pred7 = pred7,pred8 = pred8,predc7 = predc7,predc8 = predc8,pred13 = pred13,predc9 = predc9,predc10 = predc10,predc11 = predc11,pred9 = pred9,pred10 = pred10,pred11=pred11,pred12=pred12,predc12 = predc12,predc13 = predc13,predc14 = predc14,pred14 = pred14,form =form, distance = distance)



if __name__ == "__main__":
    app.run()