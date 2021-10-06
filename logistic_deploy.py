#Let's start with importing necessary libraries
import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template

class predObj:

    def predict_log(self, dict_pred):
        with open("sandardScalar.sav", 'rb') as f:
            print('Inside Scalar')
            scalar = pickle.load(f)

        with open("modelForPrediction.sav", 'rb') as f:
            print('INside Model')
            model = pickle.load(f)
        data_df = pd.DataFrame(dict_pred,index=[1,])
        print("DF:",data_df)
        print(scalar,type(scalar))
        scaled_data = scalar.transform(data_df)
        predict = model.predict(scaled_data)
        print(predict)
        if predict[0] == 0 :
            result = 'bending1'
            print(result)
        elif predict[0] == 1:
            result = 'bending2'
            print(result)
        elif predict[0] == 2:
            result = 'cycling'
            print(result)
        elif predict[0] == 3:
            result = 'lying'
            print(result)
        elif predict[0] == 4:
            result = 'sitting'
            print(result)
        elif predict[0] == 5:
            result = 'standing'
            print(result)
        elif predict[0] == 6:
            result = 'walking'
            print(result)
        else :
            result ='Can not Detect the posture'
            print(result)
        return result



