import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data_train = pd.read_csv(r"C:\Users\mourinho\Downloads\Project_1\Project 1\train.csv")
data_test = pd.read_csv(r"C:\Users\mourinho\Downloads\Project_1\Project 1\test.csv")

#droping columns that ain't meaningful to our model
data_train = data_train.drop(["BLOCKID"], axis=1)

Train_missing_values=[]
for col in data_train.columns:
    if data_train[col].isnull().sum() !=0:
         Train_missing_values.append(col)
print(Train_missing_values)


for col in data_train.columns:
    if col in (Train_missing_values):
        data_train[col].replace(np.nan, data_train[col].mean(),inplace=True)


data_test = data_test.drop(["BLOCKID"], axis =1)

Test_missing_values=[]
for col in data_test.columns:
    if data_test[col].isnull().sum() !=0:
         Test_missing_values.append(col)
print(Test_missing_values)

for col in data_test.columns:
    if col in (Test_missing_values):
        data_test[col].replace(np.nan, data_test[col].mean(),inplace=True)


data_train['bad_debt']=data_train['second_mortgage']+data_train['home_equity']-data_train['home_equity_second_mortgage']
data_test['bad_debt']=data_test['second_mortgage']+data_test['home_equity']-data_test['home_equity_second_mortgage']


data_train['pop_density'] = data_train['pop'] / data_train['ALand']
data_test['pop_density'] = data_test['pop'] / data_test['ALand']

data_train['median_age'] = (data_train['male_age_median'] *  data_train['male_pop'] + data_train['female_age_median'] *  data_train['female_pop'])  / data_train['pop']
data_test['median_age'] = (data_test['male_age_median'] *  data_test['male_pop'] + data_test['female_age_median'] *  data_test['female_pop'])  / data_test['pop']

data_train["median_age"] = data_train["median_age"].fillna(data_train["median_age"].mean())
data_test["median_age"] = data_test["median_age"].fillna(data_test["median_age"].mean())

type_dict={'type':{'City':1,
                   'Urban':2,
                   'Town':3,
                   'CDP':4,
                   'Village':5,
                   'Borough':6}
          }
data_train.replace(type_dict,inplace=True)
data_test.replace(type_dict,inplace=True)

cat_2_drop = ['UID', 'state', 'state_ab', 'city', 'place', 'primary', 'zip_code', 'area_code', 'lat', 'lng', 'COUNTYID', 'STATEID', 'SUMLEVEL']
data_train.drop(cat_2_drop, axis=1, inplace=True)
data_test.drop(cat_2_drop, axis =1, inplace=True)
data_train["income_mean"] = (data_train['hi_mean'] + data_train['family_mean'])/2
data_test["income_mean"] = (data_test['hi_mean'] + data_test['family_mean'])/2

#Removing redundant columns
Redundant_columns = [
    'male_pop',
    'female_pop',
    'rent_median',
    'universe_samples',
    'used_samples',
    'hi_median',
    'family_mean',
    'family_median',
    'hc_median',
    'hs_degree_male',
    'male_age_median',
    'female_age_median',
    'hs_degree_female',
    'male_age_samples',
    'female_age_samples']
data_train.drop(Redundant_columns, axis=1, inplace=True)
data_test.drop(Redundant_columns, axis=1, inplace=True)

y_test = data_test['hc_mortgage_mean']
data_train.drop(['remaining_income'], axis =1, inplace=True)
x_test = data_test.drop(columns=['hc_mortgage_mean'])
x_train = data_train.drop(columns=['hc_mortgage_mean'])
y_train = data_train['hc_mortgage_mean']

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error,accuracy_score


def adj_rsqrd(df, r2):


# adjusted r2 using formula adj_r2 = 1 - (1- r2) * (n-1) / (n - k - 1)
# k = number of predictors = data.shape[1] - 1
adj_rsqrd = 1 - (1 - r2) * (len(df) - 1) / (len(df) - (df.shape[1] - 1) - 1)
return round(adj_rsqrd, 3)

lr = LinearRegression()
lr.fit(x_train,y_train)

Accuracy_on_Train = lr.score(x_train, y_train)
print('The Accuracy Training:', Accuracy_on_Train)
y_predict = lr.predict(x_test)

# model evaluation for testing set

mae = mean_absolute_error(y_test, y_predict)
mse = mean_squared_error(y_test, y_predict)
r2 = r2_score(y_test, y_predict)

print("The model performance for test set")
print("--------------------------------------")
print('MAE is {}'.format(round(mae, 3)))
print('MSE is {}'.format(round(mse, 3)))
print('RMSE is {}'.format(round(mse**(0.5), 3)))
print('R2 score is {}'.format(round(r2, 3)))

print('Adjusted R2 score is {}'.format(adj_rsqrd(x_test, r2)))