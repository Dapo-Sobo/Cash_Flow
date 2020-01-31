#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:13:25 2020

@author: ibidapo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:12:33 2020

@author: ibidapo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:02:48 2020

@author: ibidapo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:40:41 2020

@author: ibidapo
"""

# importing libraries
import pandas as pd             # data science essentials
import matplotlib.pyplot as plt # essential graphical output
import seaborn as sns           # enhanced graphical output
import statsmodels.formula.api as smf # regression modeling
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.linear_model
from sklearn.neighbors import KNeighborsRegressor # KNN for Regression
from sklearn.preprocessing import StandardScaler # standard scaler


# setting pandas print options
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# specifying file name
file = 'Apprentice_Chef_Dataset.xlsx'


# reading the file into Python
original_df = pd.read_excel(file)

print(original_df.head(2))



# STEP 1: splitting personal emails

# placeholder list
placeholder_lst = []

# looping over each email address
for index, col in original_df.iterrows():
    
    # splitting email domain at '@'
    split_email = original_df.loc[index, 'EMAIL'].split(sep = '@')
    
    # appending placeholder_lst with the results
    placeholder_lst.append(split_email)
    

# converting placeholder_lst into a DataFrame 
email_df = pd.DataFrame(placeholder_lst)


# displaying the results
email_df


# renaming column to concatenate
email_df.iloc [: , 1].value_counts()



# concatenating with original DataFrame
# renaming column to concatenate
email_df.columns = ['0' , 'email_domain']

# renaming column to concatenate
email_df.loc [: ,'email_domain'].value_counts()

# concatenating personal_email_domain with friends DataFrame

original_df = pd.concat([original_df, email_df['email_domain']],
                     axis = 1)

# printing value counts of personal_email_domain
original_df.loc[: ,'email_domain'].value_counts()


original_df['email_domain'].tail(20)

# email domain types
profesional_email_domains = ['mmm.com','amex.com','apple.com','boeing.com',
                             'caterpillar.com','chevron.com','cisco.com',
                             'cocacola.com','disney.com','dupont.com','exxon.com',
                             'ge.org', 'goldmansacs.com', 'homedepot.com', 'ibm.com',
                             'intel.com', 'jnj.com', 'jpmorgan.com', 'mcdonalds.com',
                             'merck.com','microsoft.com','nike.com', 'pfizer.com',
                             'pg.com', 'travelers.com', 'unitedtech.com', 
                             'unitedhealth.com', 'verizon.com', 'visa.com', 
                             'walmart.com']

personal_email_domains  = ['gmail.com', 'yahoo.com', 'protonmail.com']

junk_email_domains=['aol.com', 'hotmail.com', 'live.com', 'msn.com', 'passport.com']

original_df.loc[1887:1945,'email_domain']

# placeholder list
placeholder_lst = []


# looping to group observations by domain type
for domain in original_df['email_domain']:
    
    if domain in profesional_email_domains:
        placeholder_lst.append('profesional')
        

    elif domain in personal_email_domains:
        placeholder_lst.append('personal')
        
    elif domain in junk_email_domains:
        placeholder_lst.append('junk')


    else:
            print('Unknown')


# looping to group observations by domain type
for domain in original_df.loc[1887:1946,'email_domain']:
    
    if domain in profesional_email_domains:
        placeholder_lst.append('profesional')
        

    elif domain in personal_email_domains:
        placeholder_lst.append('personal')
        
    elif domain in junk_email_domains:
        placeholder_lst.append('junk')


    else:
            print('Unknown')

# looping to group observations by domain type
for domain in original_df.loc[1940:1946,'email_domain']:
    
    if domain in profesional_email_domains:
        placeholder_lst.append('profesional')
        

    elif domain in personal_email_domains:
        placeholder_lst.append('personal')
        
    elif domain in junk_email_domains:
        placeholder_lst.append('junk')


    else:
            print('Unknown')
            
            
# concatenating with original DataFrame
original_df.loc[:,'domain_group'] = pd.Series(placeholder_lst)

# concatenating with original DataFrame
original_df.loc[1887:1946,'domain_group'] = pd.Series(placeholder_lst)

# concatenating with original DataFrame
original_df.loc[1940:1946,'domain_group'] = pd.Series(placeholder_lst)

# checking results
original_df['domain_group'].value_counts()

original_df['domain_group']

original_df.loc[:,'domain_group'].tail(101)

#grouping by meail domains
from sklearn.preprocessing import LabelBinarizer

lb_style = LabelBinarizer()
lb_results = lb_style.fit_transform(original_df["domain_group"])
dummy=pd.DataFrame(lb_results, columns=lb_style.classes_)
dummy.head()

#concatenate

dummy.columns

original_df = pd.concat([original_df, dummy.iloc[:,0:3]],
                     axis = 1)

original_df['profesional'].head()
original_df['personal'].head()
original_df['junk'].tail()


#dummy for MAster classes
from sklearn import preprocessing

le = preprocessing.LabelEncoder()
le.fit(original_df['MASTER_CLASSES_ATTENDED'])

list(le.classes_)



lb_style_2 = LabelBinarizer()
lb_results_2 = lb_style_2.fit_transform(original_df["MASTER_CLASSES_ATTENDED"])
dummy_2=pd.DataFrame(lb_results_2, columns=le.classes_)
dummy_2.head()

#concatenate for Master Classes

dummy_2.columns=['Zero_Master_Class',"One_Master_Class","Two_Master_Class","Three_Master_Class"]

dummy_2.head()
original_df = pd.concat([original_df, dummy_2.iloc[:,0:4]],
                     axis = 1)

original_df['Three_Master_Class'].tail(100)

#setting outlier thresholds
meals_ordered_hi=300
contacts_cs_hi=10
contacts_cs_lo=2.5
avg_time_visit_hi=180
total_photos_viewed_hi=800
avg_clicks_lo=8
weekly_plan_hi=20
meals_purch_hi=10
early_del_hi=5
revenue_hi=4500
followed_recommendation_hi=40


#Feature ENgineering
#Developing features(columns) for outliers

# TOTAL_MEALS_ORDERED
original_df['OUT_TOTAL_MEALS_ORDERED'] = 0
condition_hi = original_df.loc[0:,'OUT_TOTAL_MEALS_ORDERED'][original_df['TOTAL_MEALS_ORDERED'] > meals_ordered_hi]

original_df['OUT_TOTAL_MEALS_ORDERED'].replace(to_replace = condition_hi,
                                value      = 1,
                                inplace    = True)


# CONTACTS_W_CUSTOMER_SERVICE
original_df['OUT_CONTACTS_W_CUSTOMER_SERVICE'] = 0
condition_hi = original_df.loc[0:,'OUT_CONTACTS_W_CUSTOMER_SERVICE'][original_df['CONTACTS_W_CUSTOMER_SERVICE'] > 
                           contacts_cs_hi]
condition_lo = original_df.loc[0:,'OUT_CONTACTS_W_CUSTOMER_SERVICE'][original_df['CONTACTS_W_CUSTOMER_SERVICE'] < 
                           contacts_cs_lo]

original_df['OUT_CONTACTS_W_CUSTOMER_SERVICE'].replace(to_replace = condition_hi,
                                    value      = 1,
                                    inplace    = True)

original_df['OUT_CONTACTS_W_CUSTOMER_SERVICE'].replace(to_replace = condition_lo,
                                    value      = 1,
                                    inplace    = True)



# AVG_TIME_PER_SITE_VISIT
original_df['OUT_AVG_TIME_PER_SITE_VISIT'] = 0
condition_hi = original_df.loc[0:,'OUT_AVG_TIME_PER_SITE_VISIT'][original_df['AVG_TIME_PER_SITE_VISIT'] > avg_time_visit_hi]

original_df['OUT_AVG_TIME_PER_SITE_VISIT'].replace(to_replace = condition_hi,
                                    value      = 1,
                                    inplace    = True)


# TOTAL_PHOTOS_VIEWED
original_df['OUT_TOTAL_PHOTOS_VIEWED'] = 0
condition_hi = original_df.loc[0:,'OUT_TOTAL_PHOTOS_VIEWED'][original_df['TOTAL_PHOTOS_VIEWED'] > total_photos_viewed_hi]

original_df['OUT_TOTAL_PHOTOS_VIEWED'].replace(to_replace = condition_hi,
                                    value      = 1,
                                    inplace    = True)



# AVG_CLICKS_PER_VISIT
original_df['OUT_AVG_CLICKS_PER_VISIT'] = 0
condition_lo = original_df.loc[0:,'OUT_AVG_CLICKS_PER_VISIT'][original_df['AVG_CLICKS_PER_VISIT'] < avg_clicks_lo]

original_df['OUT_AVG_CLICKS_PER_VISIT'].replace(to_replace = condition_lo,
                                    value      = 1,
                                    inplace    = True)


# WEEKLY_PLAN 
original_df['OUT_WEEKLY_PLAN'] = 0
condition_hi = original_df.loc[0:,'OUT_WEEKLY_PLAN'][original_df['WEEKLY_PLAN'] > weekly_plan_hi]

original_df['OUT_WEEKLY_PLAN'].replace(to_replace = condition_hi,
                                    value      = 1,
                                    inplace    = True)


# UNIQUE_MEALS_PURCH
original_df['OUT_UNIQUE_MEALS_PURCH'] = 0
condition_hi = original_df.loc[0:,'OUT_UNIQUE_MEALS_PURCH'][original_df['UNIQUE_MEALS_PURCH'] > meals_purch_hi]

original_df['OUT_UNIQUE_MEALS_PURCH'].replace(to_replace = condition_hi,
                                 value      = 1,
                                 inplace    = True)


# EARLY_DELIVERIES
original_df['OUT_EARLY_DELIVERIES'] = 0
condition_hi = original_df.loc[0:,'OUT_EARLY_DELIVERIES'][original_df['EARLY_DELIVERIES'] > early_del_hi]

original_df['OUT_EARLY_DELIVERIES'].replace(to_replace = condition_hi,
                                 value      = 1,
                                 inplace    = True)


# REVENUE
original_df['OUT_REVENUE'] = 0
condition_hi = original_df.loc[0:,'OUT_REVENUE'][original_df['REVENUE'] > revenue_hi]

original_df['OUT_REVENUE'].replace(to_replace = condition_hi,
                                 value      = 1,
                                 inplace    = True)


# FOLLOWED_RECOMMENDATIONS_PCT
original_df['OUT_FOLLOWED_RECOMMENDATIONS_PCT'] = 0
condition_hi = original_df.loc[0:,'OUT_FOLLOWED_RECOMMENDATIONS_PCT'][original_df['FOLLOWED_RECOMMENDATIONS_PCT'] > followed_recommendation_hi]

original_df['OUT_FOLLOWED_RECOMMENDATIONS_PCT'].replace(to_replace = condition_hi,
                                 value      = 1,
                                 inplace    = True)




# creating a (Pearson) correlation matrix
df_corr = original_df.corr().round(2)

print(df_corr.iloc[:,0:7])

print(df_corr.iloc[:,8:16])

print(df_corr.iloc[:,17:24])

print(df_corr.iloc[:,24:30])


# printing (Pearson) correlations with Revenue
print(df_corr.loc['REVENUE'].sort_values(ascending = False))




# making a copy of original_df
original_df_explanatory = original_df.copy()


# dropping SalePrice and Order from the explanatory variable set
original_df_explanatory = original_df_explanatory.drop(['REVENUE'], axis = 1)


# formatting each explanatory variable for statsmodels
for val in original_df_explanatory:
    print(f"original_df['{val}'] +")





# building a full model
    
#DECLARING SET OF X VARIABLES

x_variables = ['CROSS_SELL_SUCCESS','TOTAL_MEALS_ORDERED','UNIQUE_MEALS_PURCH','CONTACTS_W_CUSTOMER_SERVICE',
               'PRODUCT_CATEGORIES_VIEWED' ,'AVG_TIME_PER_SITE_VISIT' ,'MOBILE_NUMBER' ,'CANCELLATIONS_BEFORE_NOON' ,
               'CANCELLATIONS_AFTER_NOON' ,'TASTES_AND_PREFERENCES' ,'MOBILE_LOGINS' ,'PC_LOGINS' ,'WEEKLY_PLAN' ,
               'EARLY_DELIVERIES' ,'LATE_DELIVERIES' ,'PACKAGE_LOCKER' ,'REFRIGERATED_LOCKER' ,'FOLLOWED_RECOMMENDATIONS_PCT' ,
               'AVG_PREP_VID_TIME' ,'LARGEST_ORDER_SIZE' ,'MASTER_CLASSES_ATTENDED' ,'MEDIAN_MEAL_RATING' ,'AVG_CLICKS_PER_VISIT' ,
               'TOTAL_PHOTOS_VIEWED' ,'junk' ,'personal' ,'profesional' ,'OUT_TOTAL_MEALS_ORDERED' ,
               'OUT_CONTACTS_W_CUSTOMER_SERVICE' ,'OUT_AVG_TIME_PER_SITE_VISIT' ,'OUT_TOTAL_PHOTOS_VIEWED' ,
               'OUT_AVG_CLICKS_PER_VISIT' ,'OUT_WEEKLY_PLAN' ,'OUT_UNIQUE_MEALS_PURCH' ,'OUT_EARLY_DELIVERIES' ,'OUT_REVENUE' ,
               'OUT_FOLLOWED_RECOMMENDATIONS_PCT','Zero_Master_Class',"One_Master_Class","Two_Master_Class","Three_Master_Class"]

x_variables_2 = [ 'TOTAL_MEALS_ORDERED','UNIQUE_MEALS_PURCH','CONTACTS_W_CUSTOMER_SERVICE',
                 'AVG_TIME_PER_SITE_VISIT','WEEKLY_PLAN','AVG_PREP_VID_TIME','LARGEST_ORDER_SIZE',
                 'MASTER_CLASSES_ATTENDED','MEDIAN_MEAL_RATING','TOTAL_PHOTOS_VIEWED','junk','profesional',
                 'OUT_CONTACTS_W_CUSTOMER_SERVICE','OUT_TOTAL_PHOTOS_VIEWED','OUT_AVG_CLICKS_PER_VISIT',
                 'OUT_WEEKLY_PLAN','Zero_Master_Class',"One_Master_Class","Two_Master_Class","Three_Master_Class"]

x_variables_3 = ['REVENUE','OUT_REVENUE','TOTAL_MEALS_ORDERED','UNIQUE_MEALS_PURCH','CONTACTS_W_CUSTOMER_SERVICE',
               'PRODUCT_CATEGORIES_VIEWED' ,'AVG_TIME_PER_SITE_VISIT' ,'MOBILE_NUMBER' ,'CANCELLATIONS_BEFORE_NOON' ,
               'CANCELLATIONS_AFTER_NOON' ,'TASTES_AND_PREFERENCES' ,'MOBILE_LOGINS' ,'PC_LOGINS' ,'WEEKLY_PLAN' ,
               'EARLY_DELIVERIES' ,'LATE_DELIVERIES' ,'PACKAGE_LOCKER' ,'REFRIGERATED_LOCKER' ,'FOLLOWED_RECOMMENDATIONS_PCT' ,
               'AVG_PREP_VID_TIME' ,'LARGEST_ORDER_SIZE' ,'MASTER_CLASSES_ATTENDED' ,'MEDIAN_MEAL_RATING' ,'AVG_CLICKS_PER_VISIT' ,
               'TOTAL_PHOTOS_VIEWED' ,'junk' ,'personal' ,'profesional' ,'OUT_TOTAL_MEALS_ORDERED' ,
               'OUT_CONTACTS_W_CUSTOMER_SERVICE' ,'OUT_AVG_TIME_PER_SITE_VISIT' ,'OUT_TOTAL_PHOTOS_VIEWED' ,
               'OUT_AVG_CLICKS_PER_VISIT' ,'OUT_WEEKLY_PLAN' ,'OUT_UNIQUE_MEALS_PURCH' ,'OUT_EARLY_DELIVERIES' ,'OUT_REVENUE' ,
               'OUT_FOLLOWED_RECOMMENDATIONS_PCT','Zero_Master_Class',"One_Master_Class","Two_Master_Class","Three_Master_Class"]

# looping to make x-variables suitable for statsmodels
for val in x_variables:
    print(f"original_df_train['{val}'] +")
    
# looping to make x-variables suitable for statsmodels
for val in x_variables_2:
    print(f"original_df_train['{val}'] +") 


# preparing explanatory variable data
original_df_data   = original_df.loc[ : , x_variables]

original_df_data.info()

# preparing response variable data
original_df_target = original_df.loc[:, 'REVENUE']

'''
# INSTANTIATING a StandardScaler() object
scaler = StandardScaler()


# FITTING the scaler with the data
scaler.fit(original_df_data)


# TRANSFORMING our data after fit
X_scaled = scaler.transform(original_df_data)


# converting scaled data into a DataFrame
X_scaled_df = pd.DataFrame(X_scaled)


# checking the results
X_scaled_df.describe().round(2)


# adding labels to the scaled DataFrame
X_scaled_df.columns = original_df_data.columns

#  Checking pre- and post-scaling of the data
print(f"""
Dataset BEFORE Scaling
----------------------
{pd.np.var(original_df_data)}


Dataset AFTER Scaling
----------------------
{pd.np.var(X_scaled_df)}
""")
'''
# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
            original_df_data,
            original_df_target,
            test_size = 0.25,
            random_state = 222)


# Training set 
print(X_train.shape)
print(y_train.shape)

# Testing set
print(X_test.shape)
print(y_test.shape)




# merging X_train and y_train so that they can be used in statsmodels
#original_df_train = pd.concat([X_train, y_train], axis = 1)

'''
original_df_train = pd.concat([X_train, y_train], axis = 1)
# Step 1: build a model
lm_best = smf.ols(formula = """ REVENUE ~ original_df_train['CROSS_SELL_SUCCESS'] +
                                original_df_train['TOTAL_MEALS_ORDERED'] +
                                original_df_train['UNIQUE_MEALS_PURCH'] +
                                original_df_train['CONTACTS_W_CUSTOMER_SERVICE'] +
                                original_df_train['PRODUCT_CATEGORIES_VIEWED'] +
                                original_df_train['AVG_TIME_PER_SITE_VISIT'] +
                                original_df_train['MOBILE_NUMBER'] +
                                original_df_train['CANCELLATIONS_BEFORE_NOON'] +
                                original_df_train['CANCELLATIONS_AFTER_NOON'] +
                                original_df_train['TASTES_AND_PREFERENCES'] +
                                original_df_train['MOBILE_LOGINS'] +
                                original_df_train['PC_LOGINS'] +
                                original_df_train['WEEKLY_PLAN'] +
                                original_df_train['EARLY_DELIVERIES'] +
                                original_df_train['LATE_DELIVERIES'] +
                                original_df_train['PACKAGE_LOCKER'] +
                                original_df_train['REFRIGERATED_LOCKER'] +
                                original_df_train['FOLLOWED_RECOMMENDATIONS_PCT'] +
                                original_df_train['AVG_PREP_VID_TIME'] +
                                original_df_train['LARGEST_ORDER_SIZE'] +
                                original_df_train['MASTER_CLASSES_ATTENDED'] +
                                original_df_train['MEDIAN_MEAL_RATING'] +
                                original_df_train['AVG_CLICKS_PER_VISIT'] +
                                original_df_train['TOTAL_PHOTOS_VIEWED'] +
                                original_df_train['junk'] +
                                original_df_train['personal'] +
                                original_df_train['profesional'] +
                                original_df_train['OUT_TOTAL_MEALS_ORDERED'] +
                                original_df_train['OUT_CONTACTS_W_CUSTOMER_SERVICE'] +
                                original_df_train['OUT_AVG_TIME_PER_SITE_VISIT'] +
                                original_df_train['OUT_TOTAL_PHOTOS_VIEWED'] +
                                original_df_train['OUT_AVG_CLICKS_PER_VISIT'] +
                                original_df_train['OUT_WEEKLY_PLAN'] +
                                original_df_train['OUT_UNIQUE_MEALS_PURCH'] +
                                original_df_train['OUT_EARLY_DELIVERIES'] +
                                original_df_train['OUT_FOLLOWED_RECOMMENDATIONS_PCT']""",
                                data=original_df_train)

# Step 2: fit the model based on the data
results = lm_best.fit()



# Step 3: analyze the summary output
print(results.summary())


# Step 1: build a model
lm_best_2 = smf.ols(formula =   """ REVENUE ~ original_df_train['TOTAL_MEALS_ORDERED'] +
                                original_df_train['UNIQUE_MEALS_PURCH'] +
                                original_df_train['CONTACTS_W_CUSTOMER_SERVICE']  +
                                original_df_train['AVG_TIME_PER_SITE_VISIT'] +
                                original_df_train['WEEKLY_PLAN']+
                                original_df_train['AVG_PREP_VID_TIME'] +
                                original_df_train['LARGEST_ORDER_SIZE'] +
                                original_df_train['MASTER_CLASSES_ATTENDED'] +
                                original_df_train['MEDIAN_MEAL_RATING'] +
                                original_df_train['TOTAL_PHOTOS_VIEWED'] +
                                original_df_train['junk'] +
                                original_df_train['profesional'] +
                                original_df_train['OUT_CONTACTS_W_CUSTOMER_SERVICE'] +
                                original_df_train['OUT_TOTAL_PHOTOS_VIEWED'] +
                                original_df_train['OUT_AVG_CLICKS_PER_VISIT'] +
                                original_df_train['OUT_WEEKLY_PLAN'] """,
                                data=original_df_train)

# Step 2: fit the model based on the data
results_2 = lm_best_2.fit()



# Step 3: analyze the summary output
print(results_2.summary())

'''

# INSTANTIATING a model object
lr = LinearRegression()


# FITTING to the training data
lr_fit = lr.fit(X_train, y_train)


# PREDICTING on new data
lr_pred = lr_fit.predict(X_test)


# SCORING the results
print('Training Score:', lr.score(X_train, y_train).round(4))
print('Testing Score:',  lr.score(X_test, y_test).round(4))


# saving scoring data for future use
lr_train_score = lr.score(X_train, y_train).round(4)
lr_test_score  = lr.score(X_test, y_test).round(4)



# INSTANTIATING a model object
ridge_model = sklearn.linear_model.Ridge()

# FITTING the training data
ridge_fit = ridge_model.fit(X_train, y_train)


# PREDICTING on new data
ridge_pred = ridge_model.predict(X_test)

print('Training Score:', ridge_model.score(X_train, y_train).round(4))
print('Testing Score:',  ridge_model.score(X_test, y_test).round(4))


# saving scoring data for future use
ridge_train_score = ridge_model.score(X_train, y_train).round(4)
ridge_test_score  = ridge_model.score(X_test, y_test).round(4)




# INSTANTIATING a model object
lasso_model = sklearn.linear_model.Lasso()

# FITTING the training data
lasso_fit = lasso_model.fit(X_train, y_train)


# PREDICTING on new data
lasso_pred = lasso_model.predict(X_test)

print('Training Score:', lasso_model.score(X_train, y_train).round(4))
print('Testing Score:',  lasso_model.score(X_test, y_test).round(4))




# saving scoring data for future use
lasso_train_score = lasso_model.score(X_train, y_train).round(4)
lasso_test_score  = lasso_model.score(X_test, y_test).round(4)


# INSTANTIATING a model object
BAY_model = sklearn.linear_model.BayesianRidge()


# FITTING the training data
BAY_fit = BAY_model.fit(X_train, y_train)


# PREDICTING on new data
BAY_pred = BAY_model.predict(X_test)


print('Training Score:', BAY_model.score(X_train, y_train).round(4))
print('Testing Score:',  BAY_model.score(X_test, y_test).round(4))

bay_train_score = BAY_model.score(X_train, y_train).round(4)
bay_test_score  = BAY_model.score(X_test, y_test).round(4)



# creating lists for training set accuracy and test set accuracy
training_accuracy = []
test_accuracy = []

# building a visualization of 1 to 50 neighbors
neighbors_settings = range(1, 21)


for n_neighbors in neighbors_settings:
    # Building the model
    clf = KNeighborsRegressor(n_neighbors = n_neighbors)
    clf.fit(X_train, y_train)
    
    # Recording the training set accuracy
    training_accuracy.append(clf.score(X_train, y_train))
    
    # Recording the generalization accuracy
    test_accuracy.append(clf.score(X_test, y_test))


# plotting the visualization
fig, ax = plt.subplots(figsize=(12,8))
plt.plot(neighbors_settings, training_accuracy, label = "training accuracy")
plt.plot(neighbors_settings, test_accuracy, label = "test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.show()


# finding the optimal number of neighbors
opt_neighbors = test_accuracy.index(max(test_accuracy)) + 1
print(f"""The optimal number of neighbors is {opt_neighbors}""")



# INSTANTIATING a KNN model object
knn_reg = KNeighborsRegressor(algorithm = 'auto',
                              n_neighbors = 13)


# FITTING to the training data
knn_reg.fit(X_train, y_train)


# PREDICTING on new data
knn_reg_pred = knn_reg.predict(X_test)


# SCORING the results
print('Training Score:', knn_reg.score(X_train, y_train).round(4))
print('Testing Score:',  knn_reg.score(X_test, y_test).round(4))


# saving scoring data for future use
knn_reg_score_train = knn_reg.score(X_train, y_train).round(4)
knn_reg_score_test  = knn_reg.score(X_test, y_test).round(4)

# comparing results

print(f"""
Model      Train Score      Test Score
-----      -----------      ----------
OLS        {lr_train_score}             {lr_test_score}
Ridge      {ridge_train_score}               {ridge_test_score}
Lasso      {lasso_train_score}             {lasso_test_score}
Bayesian   {bay_train_score}             {bay_test_score}
knn        {knn_reg_score_train}             {knn_reg_score_test}
""")



#################


#################


