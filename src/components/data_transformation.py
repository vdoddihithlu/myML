
import sys
import os
import pandas as pd


from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from src.exceptions import CustomException
from src.logger import logging
from src.components.parms import numeric_feature, categorical_features, target_feature

class DataTransformation:
    def __init__(self):
        # Initialization code here
        pass

    def define_preprocessing(self):
        try:
            logging.info("Define pipeline")
            
            numeric_transformation = Pipeline(steps=[
                ('Impute',SimpleImputer(strategy='mean'))
                ,('Scale',StandardScaler())
            ])

            
            categorical_transformation = Pipeline(steps=[
                ('Impute', SimpleImputer(strategy='most_frequent'))
                ,('onehot',OneHotEncoder())
            ])

            preprocessing = ColumnTransformer( transformers= [
                ('numeric',numeric_transformation,numeric_feature)
                ,('cat',categorical_transformation,categorical_features) ]
            )

            return preprocessing
        except Exception as e:
            raise CustomException(e,sys)
        

    def innitiate_preprocessing(self, train_path,test_path):
        try:
            logging.info("Read train and Test data")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("transform the data")
            preprocessing =  self.define_preprocessing() 
            train_ar = preprocessing.fit_transform(train_df)
            test_ar = preprocessing.transform(test_df)

            logging.info("recreate datafrome with transformed columns")
            categorical_features_transformed = preprocessing.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_features)
            features_transformed = list(numeric_feature) + list(categorical_features_transformed)
            df_train_transformed_inter = pd.DataFrame(train_ar, columns=features_transformed)
            df_test_transformed_inter = pd.DataFrame(test_ar, columns=features_transformed)

         #   df_untransformed = df.drop(columns=list(numeric_feature) + list(categorical_features)).reset_index(drop=True)
            df_train_transformed = pd.concat( [df_train_transformed_inter, train_df[target_feature].reset_index(drop=True)], axis=1)
            df_test_transformed = pd.concat( [df_test_transformed_inter, test_df[target_feature].reset_index(drop=True)], axis=1)

            logging.info("return trasnsformed data")
            return (df_train_transformed, df_test_transformed)


        except Exception as e:
            raise CustomException(e,sys)


