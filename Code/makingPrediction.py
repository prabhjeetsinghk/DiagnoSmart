import tensorflow as tf
import tensorflow_hub as hub
import joblib
import pandas as pd

class MakePrediction:
    def __init__(self, knn_model):
        self.knn_model = joblib.load('knn_model.joblib')
    

    def predict(self, text):
        nei = self.knn_model.kneighbors(text,return_distance=False)[0][0]
        symptomsDF =pd.read_csv('/workspaces/DiagnoSmart/Code/CleanedSymptoms.csv')
        diseaseDescriptionDF = pd.read_csv('Code/CleanedDescripition.csv')

        disease_name = symptomsDF['Disease'].iloc[nei]
        description = diseaseDescriptionDF['Description'].loc[disease_name]

        print('**********************************')
        print('Predicted Disease : ',disease_name.title())
        print('Disease Definition:',description)
        print('**********************************')


