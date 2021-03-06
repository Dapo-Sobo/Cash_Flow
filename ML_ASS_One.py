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
housing = pd.read_excel(file)

print(housing.head(2))



# STEP 1: splitting personal emails

# placeholder list
placeholder_lst = []

# looping over each email address
for index, col in housing.iterrows():
    
    # splitting email domain at '@'
    split_email = housing.loc[index, 'EMAIL'].split(sep = '@')
    
    # appending placeholder_lst with the results
    placeholder_lst.append(split_email)
    

# converting placeholder_lst into a DataFrame 
email_df = pd.DataFrame(placeholder_lst)


# displaying the results
email_df


# renaming column to concatenate
email_df.iloc [: , 1].value_counts()



# STEP 2: concatenating with original DataFrame
# renaming column to concatenate
email_df.columns = ['0' , 'email_domain']

# renaming column to concatenate
email_df.loc [: ,'email_domain'].value_counts()

# concatenating personal_email_domain with friends DataFrame

housing = pd.concat([housing, email_df['email_domain']],
                     axis = 1)

# printing value counts of personal_email_domain
housing.loc[: ,'email_domain'].value_counts()


housing['email_domain'].tail(20)

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

housing.loc[1887:1945,'email_domain']

# placeholder list
placeholder_lst = []


# looping to group observations by domain type
for domain in housing['email_domain']:
    
    if domain in profesional_email_domains:
        placeholder_lst.append('profesional')
        

    elif domain in personal_email_domains:
        placeholder_lst.append('personal')
        
    elif domain in junk_email_domains:
        placeholder_lst.append('junk')


    else:
            print('Unknown')


# looping to group observations by domain type
for domain in housing.loc[1887:1946,'email_domain']:
    
    if domain in profesional_email_domains:
        placeholder_lst.append('profesional')
        

    elif domain in personal_email_domains:
        placeholder_lst.append('personal')
        
    elif domain in junk_email_domains:
        placeholder_lst.append('junk')


    else:
            print('Unknown')

# looping to group observations by domain type
for domain in housing.loc[1940:1946,'email_domain']:
    
    if domain in profesional_email_domains:
        placeholder_lst.append('profesional')
        

    elif domain in personal_email_domains:
        placeholder_lst.append('personal')
        
    elif domain in junk_email_domains:
        placeholder_lst.append('junk')


    else:
            print('Unknown')
            
            
# concatenating with original DataFrame
housing.loc[:,'domain_group'] = pd.Series(placeholder_lst)

# concatenating with original DataFrame
housing.loc[1887:1946,'domain_group'] = pd.Series(placeholder_lst)

# concatenating with original DataFrame
housing.loc[1940:1946,'domain_group'] = pd.Series(placeholder_lst)

# checking results
housing['domain_group'].value_counts()

housing['domain_group']

housing.loc[:,'domain_group'].tail(101)

from sklearn.preprocessing import LabelBinarizer

lb_style = LabelBinarizer()
lb_results = lb_style.fit_transform(housing["domain_group"])
dummy=pd.DataFrame(lb_results, columns=lb_style.classes_)
dummy.head()

#concatenate

dummy.columns

housing = pd.concat([housing, dummy.iloc[:,0:3]],
                     axis = 1)

housing['profesional'].head()
housing['personal'].head()
housing['junk'].tail()

########################
# Visual EDA (Histograms)
########################

fig, ax = plt.subplots(figsize = (10, 8))
plt.subplot(2, 2, 1)
sns.distplot(housing['TOTAL_MEALS_ORDERED'],
             bins  = 'fd',
             color = 'g')
plt.xlabel('TOTAL_MEALS_ORDERED')

########################

plt.subplot(2, 2, 2)
sns.distplot(housing['AVG_PREP_VID_TIME'],
             bins  = 'fd',
             color = 'y')
plt.xlabel('AVG_PREP_VID_TIME')

########################

plt.subplot(2, 2, 3)
sns.distplot(housing['CONTACTS_W_CUSTOMER_SERVICE'],
             bins  = 'fd',
             kde   = False,
             rug   = True,
             color = 'orange')
plt.xlabel('CONTACTS_W_CUSTOMER_SERVICE')

########################
plt.subplot(2, 2, 4)
sns.distplot(housing['AVG_TIME_PER_SITE_VISIT'],
             bins  = 'fd',
             kde   = False,
             rug   = True,
             color = 'r')
plt.xlabel('AVG_TIME_PER_SITE_VISIT')
plt.tight_layout()
plt.savefig('Housing Data Histograms 1 of 5.png')
plt.show()

########################
########################

fig, ax = plt.subplots(figsize = (10, 8))
plt.subplot(2, 2, 1)
sns.distplot(housing['MASTER_CLASSES_ATTENDED'],
             bins  = 'fd',
             color = 'g')
plt.xlabel('MASTER_CLASSES_ATTENDED')

########################

plt.subplot(2, 2, 2)
sns.distplot(housing['MOBILE_NUMBER'],
             bins  = 'fd',
             color = 'y')
plt.xlabel('MOBILE_NUMBER')

########################

plt.subplot(2, 2, 3)
sns.distplot(housing['TOTAL_PHOTOS_VIEWED'],
             bins  = 'fd',
             kde   = False,
             rug   = True,
             color = 'orange')
plt.xlabel('TOTAL_PHOTOS_VIEWED')

########################

plt.subplot(2, 2, 4)
sns.distplot(housing['AVG_CLICKS_PER_VISIT'],
             bins  = 'fd',
             kde   = False,
             rug   = True,
             color = 'r')
plt.xlabel('AVG_CLICKS_PER_VISIT')
plt.tight_layout()
plt.savefig('Housing Data Histograms 2 of 5.png')
plt.show()

########################
########################

fig, ax = plt.subplots(figsize = (10, 8))
plt.subplot(2, 2, 1)
sns.distplot(housing['WEEKLY_PLAN'],
             bins  = 'fd',
             color = 'y')
plt.xlabel('WEEKLY_PLAN')

########################

plt.subplot(2, 2, 2)
sns.distplot(housing['MEDIAN_MEAL_RATING'],
             bins  = 'fd',
             kde   = False,
             rug   = True,
             color = 'orange')
plt.xlabel('MEDIAN_MEAL_RATING')

########################

plt.subplot(2, 2, 3)
sns.distplot(housing['UNIQUE_MEALS_PURCH'],
             bins  = 'fd',
             kde   = False,
             rug   = True,
             color = 'r')
plt.xlabel('UNIQUE_MEALS_PURCH')

########################

plt.subplot(2, 2, 4)
sns.distplot(housing['EARLY_DELIVERIES'],
             bins  = 'fd',
             color = 'g')
plt.xlabel('EARLY_DELIVERIES')
plt.tight_layout()
plt.savefig('Housing Data Histograms 3 of 5.png')
plt.show()

########################
########################

fig, ax = plt.subplots(figsize = (10, 8))
plt.subplot(2, 2, 1)
sns.distplot(housing['PRODUCT_CATEGORIES_VIEWED'],
             bins  = 'fd',
             color = 'y')
plt.xlabel('PRODUCT_CATEGORIES_VIEWED')

########################

plt.subplot(2, 2, 2)
sns.distplot(housing['CROSS_SELL_SUCCESS'],
             bins = 10,
             kde  = False,
             rug  = True,
             color = 'orange')
plt.xlabel('CROSS_SELL_SUCCESS')

########################

plt.subplot(2, 2, 3)
sns.distplot(housing['REVENUE'],
             bins = 'fd',
             kde  = False,
             rug  = True,
             color = 'r')
plt.xlabel('REVENUE')

########################

plt.subplot(2, 2, 4)
sns.distplot(housing['CANCELLATIONS_BEFORE_NOON'],
             bins  = 'fd',
             color = 'g')
plt.xlabel('CANCELLATIONS_BEFORE_NOON')
plt.tight_layout()
plt.savefig('Housing Data Histograms 4 of 5.png')
plt.show()

########################
########################

fig, ax = plt.subplots(figsize = (10, 8))
plt.subplot(2, 2, 1)
sns.distplot(housing['REFRIGERATED_LOCKER'],
             bins  = 10,
             kde   = False,
             rug   = True,
             color = 'r')
plt.xlabel('REFRIGERATED_LOCKER')

########################

plt.subplot(2, 2, 2)
sns.distplot(housing['LARGEST_ORDER_SIZE'],
             bins  = 'fd',
             color = 'r')
plt.xlabel('LARGEST_ORDER_SIZE')

########################
plt.subplot(2, 2, 3)
sns.distplot(housing['CANCELLATIONS_BEFORE_NOON'],
             bins  = 'fd',
             color = 'r')
plt.xlabel('CANCELLATIONS_BEFORE_NOON')

########################
plt.subplot(2, 2, 4)
sns.distplot(housing['CANCELLATIONS_AFTER_NOON'],
             bins  = 'fd',
             color = 'r')
plt.xlabel('CANCELLATIONS_AFTER_NOON')

########################
plt.tight_layout()
plt.savefig('Housing Data Histograms 5 of 5.png')
plt.show()

fig, ax = plt.subplots(figsize = (10, 8))
plt.subplot(2, 2, 1)
sns.distplot(housing['TASTES_AND_PREFERENCES'],
             bins  = 10,
             kde   = False,
             rug   = True,
             color = 'orange')
plt.xlabel('TASTES_AND_PREFERENCES')

########################

plt.subplot(2, 2, 2)
sns.distplot(housing['MOBILE_LOGINS'],
             bins  = 'fd',
             color = 'r')
plt.xlabel('MOBILE_LOGINS')

########################
plt.subplot(2, 2, 3)
sns.distplot(housing['PC_LOGINS'],
             bins  = 'fd',
             color = 'y')
plt.xlabel('PC_LOGINS')

########################
plt.subplot(2, 2, 4)
sns.distplot(housing['LATE_DELIVERIES'],
             bins  = 'fd',
             color = 'g')
plt.xlabel('LATE_DELIVERIES')

########################
plt.tight_layout()
plt.savefig('Housing Data Histograms 6 of 5.png')
plt.show()

############################
############################


fig, ax = plt.subplots(figsize = (10, 8))
plt.subplot(2, 2, 1)
sns.distplot(housing['PACKAGE_LOCKER'],
             bins  = 10,
             kde   = False,
             rug   = True,
             color = 'orange')
plt.xlabel('PACKAGE_LOCKER')

########################

plt.subplot(2, 2, 2)
sns.distplot(housing['FOLLOWED_RECOMMENDATIONS_PCT'],
             bins  = 'fd',
             color = 'r')
plt.xlabel('FOLLOWED_RECOMMENDATIONS_PCT')

########################
plt.subplot(2, 2, 3)
sns.distplot(housing['AVG_PREP_VID_TIME'],
             bins  = 'fd',
             color = 'y')
plt.xlabel('AVG_PREP_VID_TIME')

########################
plt.subplot(2, 2, 4)
sns.distplot(housing['LARGEST_ORDER_SIZE'],
             bins  = 'fd',
             color = 'g')
plt.xlabel('LARGEST_ORDER_SIZE')

########################
plt.tight_layout()
plt.savefig('Housing Data Histograms 7 of 5.png')
plt.show()


fig, ax = plt.subplots(figsize = (10, 8))
plt.subplot(2, 2, 1)
sns.distplot(housing['junk'],
             bins  = 10,
             kde   = False,
             rug   = True,
             color = 'y')
plt.xlabel('JUNK EMAIL DOMAIN')

########################

plt.subplot(2, 2, 2)
sns.distplot(housing['profesional'],
             bins  = 'fd',
             color = 'g')
plt.xlabel('PROFESSIONAL EMAIL DOMAIN')

########################
plt.subplot(2, 2, 3)
sns.distplot(housing['personal'],
             bins  = 'fd',
             color = 'r')
plt.xlabel('PERSONAL EMAIL DOMAIN')

########################
plt.tight_layout()
plt.show()

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
housing['OUT_TOTAL_MEALS_ORDERED'] = 0
condition_hi = housing.loc[0:,'OUT_TOTAL_MEALS_ORDERED'][housing['TOTAL_MEALS_ORDERED'] > meals_ordered_hi]

housing['OUT_TOTAL_MEALS_ORDERED'].replace(to_replace = condition_hi,
                                value      = 1,
                                inplace    = True)


# CONTACTS_W_CUSTOMER_SERVICE
housing['OUT_CONTACTS_W_CUSTOMER_SERVICE'] = 0
condition_hi = housing.loc[0:,'OUT_CONTACTS_W_CUSTOMER_SERVICE'][housing['CONTACTS_W_CUSTOMER_SERVICE'] > 
                           contacts_cs_hi]
condition_lo = housing.loc[0:,'OUT_CONTACTS_W_CUSTOMER_SERVICE'][housing['CONTACTS_W_CUSTOMER_SERVICE'] < 
                           contacts_cs_lo]

housing['OUT_CONTACTS_W_CUSTOMER_SERVICE'].replace(to_replace = condition_hi,
                                    value      = 1,
                                    inplace    = True)

housing['OUT_CONTACTS_W_CUSTOMER_SERVICE'].replace(to_replace = condition_lo,
                                    value      = 1,
                                    inplace    = True)



# AVG_TIME_PER_SITE_VISIT
housing['OUT_AVG_TIME_PER_SITE_VISIT'] = 0
condition_hi = housing.loc[0:,'OUT_AVG_TIME_PER_SITE_VISIT'][housing['AVG_TIME_PER_SITE_VISIT'] > avg_time_visit_hi]

housing['OUT_AVG_TIME_PER_SITE_VISIT'].replace(to_replace = condition_hi,
                                    value      = 1,
                                    inplace    = True)


# TOTAL_PHOTOS_VIEWED
housing['OUT_TOTAL_PHOTOS_VIEWED'] = 0
condition_hi = housing.loc[0:,'OUT_TOTAL_PHOTOS_VIEWED'][housing['TOTAL_PHOTOS_VIEWED'] > total_photos_viewed_hi]

housing['OUT_TOTAL_PHOTOS_VIEWED'].replace(to_replace = condition_hi,
                                    value      = 1,
                                    inplace    = True)



# AVG_CLICKS_PER_VISIT
housing['OUT_AVG_CLICKS_PER_VISIT'] = 0
condition_lo = housing.loc[0:,'OUT_AVG_CLICKS_PER_VISIT'][housing['AVG_CLICKS_PER_VISIT'] < avg_clicks_lo]

housing['OUT_AVG_CLICKS_PER_VISIT'].replace(to_replace = condition_lo,
                                    value      = 1,
                                    inplace    = True)


# WEEKLY_PLAN 
housing['OUT_WEEKLY_PLAN'] = 0
condition_hi = housing.loc[0:,'OUT_WEEKLY_PLAN'][housing['WEEKLY_PLAN'] > weekly_plan_hi]

housing['OUT_WEEKLY_PLAN'].replace(to_replace = condition_hi,
                                    value      = 1,
                                    inplace    = True)


# UNIQUE_MEALS_PURCH
housing['OUT_UNIQUE_MEALS_PURCH'] = 0
condition_hi = housing.loc[0:,'OUT_UNIQUE_MEALS_PURCH'][housing['UNIQUE_MEALS_PURCH'] > meals_purch_hi]

housing['OUT_UNIQUE_MEALS_PURCH'].replace(to_replace = condition_hi,
                                 value      = 1,
                                 inplace    = True)


# EARLY_DELIVERIES
housing['OUT_EARLY_DELIVERIES'] = 0
condition_hi = housing.loc[0:,'OUT_EARLY_DELIVERIES'][housing['EARLY_DELIVERIES'] > early_del_hi]

housing['OUT_EARLY_DELIVERIES'].replace(to_replace = condition_hi,
                                 value      = 1,
                                 inplace    = True)


# REVENUE
housing['OUT_REVENUE'] = 0
condition_hi = housing.loc[0:,'OUT_REVENUE'][housing['REVENUE'] > revenue_hi]

housing['OUT_REVENUE'].replace(to_replace = condition_hi,
                                 value      = 1,
                                 inplace    = True)


# FOLLOWED_RECOMMENDATIONS_PCT
housing['OUT_FOLLOWED_RECOMMENDATIONS_PCT'] = 0
condition_hi = housing.loc[0:,'OUT_FOLLOWED_RECOMMENDATIONS_PCT'][housing['FOLLOWED_RECOMMENDATIONS_PCT'] > followed_recommendation_hi]

housing['OUT_FOLLOWED_RECOMMENDATIONS_PCT'].replace(to_replace = condition_hi,
                                 value      = 1,
                                 inplace    = True)




# creating a (Pearson) correlation matrix
df_corr = housing.corr().round(2)

print(df_corr.iloc[:,0:7])

print(df_corr.iloc[:,8:16])

print(df_corr.iloc[:,17:24])

print(df_corr.iloc[:,24:30])


# printing (Pearson) correlations with Revenue
print(df_corr.loc['REVENUE'].sort_values(ascending = False))

# printing (Pearson) correlations with AVG PREP_VID_TIME
print(df_corr.loc['AVG_PREP_VID_TIME'].sort_values(ascending = False))


# making a copy of housing
housing_explanatory = housing.copy()


# dropping SalePrice and Order from the explanatory variable set
housing_explanatory = housing_explanatory.drop(['REVENUE'], axis = 1)


# formatting each explanatory variable for statsmodels
for val in housing_explanatory:
    print(f"housing['{val}'] +")


# saving feature-rich dataset in Excel
housing.to_excel('housing_Apprentice.xlsx',
                 index = False)




# building a full model

# blueprinting a model type
lm_full = smf.ols(formula = """ REVENUE ~ housing['AVG_PREP_VID_TIME']""",
                  data = housing)


# telling Python to run the data through the blueprint
results_full = lm_full.fit()


# printing the results
print(results_full.summary())


# preparing explanatory variable data
housing_data   = housing.drop(['REVENUE',
                               'OUT_REVENUE'],
                                axis = 1)


# preparing response variable data
housing_target = housing.loc[:, 'REVENUE']


# preparing training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
            housing_data,
            housing_target,
            test_size = 0.25,
            random_state = 222)


# Training set 
print(X_train.shape)
print(y_train.shape)

# Testing set
print(X_test.shape)
print(y_test.shape)


#DECLARING SET OF X VARIABLES

x_variables = ['AVG_PREP_VID_TIME','MEDIAN_MEAL_RATING','TOTAL_MEALS_ORDERED',
               'TOTAL_PHOTOS_VIEWED','MASTER_CLASSES_ATTENDED','LARGEST_ORDER_SIZE',
               'OUT_TOTAL_MEALS_ORDERED','OUT_TOTAL_PHOTOS_VIEWED','AVG_TIME_PER_SITE_VISIT',
               'OUT_UNIQUE_MEALS_PURCH','CONTACTS_W_CUSTOMER_SERVICE','OUT_AVG_CLICKS_PER_VISIT',
               'OUT_AVG_TIME_PER_SITE_VISIT','PRODUCT_CATEGORIES_VIEWED','OUT_WEEKLY_PLAN',
               'MOBILE_NUMBER','CANCELLATIONS_AFTER_NOON','UNIQUE_MEALS_PURCH',
               'OUT_CONTACTS_W_CUSTOMER_SERVICE','profesional','personal','junk']

x_variables_2 = ['AVG_PREP_VID_TIME','MEDIAN_MEAL_RATING','TOTAL_MEALS_ORDERED',
               'TOTAL_PHOTOS_VIEWED','MASTER_CLASSES_ATTENDED','LARGEST_ORDER_SIZE',
               'OUT_TOTAL_PHOTOS_VIEWED','AVG_TIME_PER_SITE_VISIT',
               'CONTACTS_W_CUSTOMER_SERVICE','OUT_AVG_CLICKS_PER_VISIT',
               'OUT_AVG_TIME_PER_SITE_VISIT','UNIQUE_MEALS_PURCH',
               'OUT_CONTACTS_W_CUSTOMER_SERVICE']

x_variables_3 = ['AVG_PREP_VID_TIME','MEDIAN_MEAL_RATING','TOTAL_MEALS_ORDERED','MASTER_CLASSES_ATTENDED',
                 'LARGEST_ORDER_SIZE',
                   'OUT_TOTAL_PHOTOS_VIEWED','AVG_TIME_PER_SITE_VISIT','UNIQUE_MEALS_PURCH',
                   'OUT_CONTACTS_W_CUSTOMER_SERVICE','AVG_CLICKS_PER_VISIT']

# looping to make x-variables suitable for statsmodels
for val in x_variables:
    print(f"housing_train['{val}'] +")
    
# looping to make x-variables suitable for statsmodels
for val in x_variables_2:
    print(f"housing_train['{val}'] +") 

# merging X_train and y_train so that they can be used in statsmodels
#housing_train = pd.concat([X_train, y_train], axis = 1)


housing_train = pd.concat([X_train, y_train], axis = 1)
# Step 1: build a model
lm_best = smf.ols(formula = """ REVENUE ~ housing_train['AVG_PREP_VID_TIME'] +
                               housing_train['MEDIAN_MEAL_RATING'] +
                                housing_train['TOTAL_MEALS_ORDERED'] +
                                housing_train['TOTAL_PHOTOS_VIEWED'] +
                                housing_train['MASTER_CLASSES_ATTENDED'] +
                                housing_train['LARGEST_ORDER_SIZE'] +
                                housing_train['OUT_TOTAL_MEALS_ORDERED'] +
                                housing_train['OUT_TOTAL_PHOTOS_VIEWED'] +
                                housing_train['AVG_TIME_PER_SITE_VISIT'] +
                                housing_train['OUT_UNIQUE_MEALS_PURCH'] +
                                housing_train['CONTACTS_W_CUSTOMER_SERVICE'] +
                                housing_train['OUT_AVG_CLICKS_PER_VISIT'] +
                                housing_train['OUT_AVG_TIME_PER_SITE_VISIT'] +
                                housing_train['PRODUCT_CATEGORIES_VIEWED'] +
                                housing_train['OUT_WEEKLY_PLAN'] +
                                housing_train['MOBILE_NUMBER'] +
                                housing_train['CANCELLATIONS_AFTER_NOON'] +
                                housing_train['UNIQUE_MEALS_PURCH'] +
                                housing_train['OUT_CONTACTS_W_CUSTOMER_SERVICE']""",
                                data=housing_train)

# Step 2: fit the model based on the data
results = lm_best.fit()



# Step 3: analyze the summary output
print(results.summary())



# Step 1: build a model
lm_best_2 = smf.ols(formula =   """ REVENUE ~ housing_train['AVG_PREP_VID_TIME'] +
                                    housing_train['MEDIAN_MEAL_RATING'] +
                                    housing_train['TOTAL_MEALS_ORDERED'] +
                                    housing_train['TOTAL_PHOTOS_VIEWED'] +
                                    housing_train['MASTER_CLASSES_ATTENDED'] +
                                    housing_train['LARGEST_ORDER_SIZE'] +
                                    housing_train['OUT_TOTAL_PHOTOS_VIEWED'] +
                                    housing_train['AVG_TIME_PER_SITE_VISIT'] +
                                    housing_train['CONTACTS_W_CUSTOMER_SERVICE'] +
                                    housing_train['OUT_AVG_CLICKS_PER_VISIT'] +
                                    housing_train['OUT_AVG_TIME_PER_SITE_VISIT'] +
                                    housing_train['UNIQUE_MEALS_PURCH'] +
                                    housing_train['OUT_CONTACTS_W_CUSTOMER_SERVICE'] """,
                                    data=housing_train)

# Step 2: fit the model based on the data
results_2 = lm_best_2.fit()



# Step 3: analyze the summary output
print(results_2.summary())



# applying model in scikit-learn

# Preparing a DataFrame based the the analysis above
housing_data   = housing.loc[ : , x_variables]

housing_data.info()

# Preparing the target variable
housing_target = housing.loc[:, 'REVENUE']


# INSTANTIATING a StandardScaler() object
scaler = StandardScaler()


# FITTING the scaler with the data
scaler.fit(housing_data)


# TRANSFORMING our data after fit
X_scaled = scaler.transform(housing_data)


# converting scaled data into a DataFrame
X_scaled_df = pd.DataFrame(X_scaled)


# checking the results
X_scaled_df.describe().round(2)


# adding labels to the scaled DataFrame
X_scaled_df.columns = housing_data.columns

#  Checking pre- and post-scaling of the data
print(f"""
Dataset BEFORE Scaling
----------------------
{pd.np.var(housing_data)}


Dataset AFTER Scaling
----------------------
{pd.np.var(X_scaled_df)}
""")


# this is the exact code we were using before now standardized
X_train, X_test, y_train, y_test = train_test_split(
            X_scaled_df,
            housing_target,
            test_size = 0.25,
            random_state = 222)

# running train/test split again
#X_train, X_test, y_train, y_test = train_test_split(
#            housing_data,
#            housing_target,
#            test_size = 0.25,
#            random_state = 222)


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
ard_model = sklearn.linear_model.ARDRegression()


# FITTING the training data
ard_fit = ard_model.fit(X_train, y_train)


# PREDICTING on new data
ard_pred = ard_model.predict(X_test)


print('Training Score:', ard_model.score(X_train, y_train).round(4))
print('Testing Score:',  ard_model.score(X_test, y_test).round(4))


# saving scoring data for future use
ard_train_score = ard_model.score(X_train, y_train).round(4)
ard_test_score  = ard_model.score(X_test, y_test).round(4)

# comparing results

print(f"""
Model      Train Score      Test Score
-----      -----------      ----------
OLS        {lr_train_score}           {lr_test_score}
Ridge      {ridge_train_score}           {ridge_test_score}
Lasso      {lasso_train_score}           {lasso_test_score}
ARD        {ard_train_score}           {ard_test_score}
""")


# creating a dictionary for model results
model_performance = {'Model'    : ['OLS', 'Ridge', 'Lasso', 'ARD'],
           
                     'Training' : [lr_train_score, ridge_train_score,
                                   lasso_train_score, ard_train_score],
           
                     'Testing'  : [lr_test_score, ridge_test_score,
                                   lasso_test_score, ard_test_score]
                     }




#################

# INSTANTIATING a KNN model object
knn_reg = KNeighborsRegressor(algorithm = 'auto',
                              n_neighbors = 15)


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



# INSTANTIATING a model object
BAY_model = sklearn.linear_model.BayesianRidge()


# FITTING the training data
BAY_fit = BAY_model.fit(X_train, y_train)


# PREDICTING on new data
BAY_pred = BAY_model.predict(X_test)


print('Training Score:', BAY_model.score(X_train, y_train).round(4))
print('Testing Score:',  BAY_model.score(X_test, y_test).round(4))





