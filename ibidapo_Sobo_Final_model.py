#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:19:40 2020

@author: ibidapo
"""

# timeit

# Student Name : IBIDAPO SOBO
# Cohort       :4

# Note: You are only allowed to submit ONE final model for this assignment.


################################################################################
# Import Packages
################################################################################

# use this space for all of your package imports

# importing libraries
# importing libraries
import pandas as pd             # data science essentials
from sklearn.model_selection import train_test_split
import sklearn.linear_model





################################################################################
# Load Data
################################################################################

# use this space to load the original dataset
# MAKE SURE TO SAVE THE ORIGINAL FILE AS original_df
# Example: original_df = pd.read_excel('Apprentice Chef Dataset.xlsx')

# reading the file into Python
# setting pandas print options

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# specifying file name
file = 'Apprentice_Chef_Dataset.xlsx'
original_df = pd.read_excel(file)

################################################################################
# Feature Engineering and (optional) Dataset Standardization
################################################################################

# use this space for all of the feature engineering that is required for your
# final model

# if your final model requires dataset standardization, do this here as well
# STEP 1: splitting personal emails

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

#original_df.loc[:,'domain_group'].tail(101)

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
#df_corr = original_df.corr().round(2)

#print(df_corr.iloc[:,0:7])

#print(df_corr.iloc[:,8:16])

#print(df_corr.iloc[:,17:24])

#print(df_corr.iloc[:,24:30])


# printing (Pearson) correlations with Revenue
#print(df_corr.loc['REVENUE'].sort_values(ascending = False))




# making a copy of original_df
original_df_explanatory = original_df.copy()


# dropping SalePrice and Order from the explanatory variable set
original_df_explanatory = original_df_explanatory.drop(['REVENUE'], axis = 1)


# formatting each explanatory variable for statsmodels
#for val in original_df_explanatory:
#    print(f"original_df['{val}'] +")





################################################################################
# Train/Test Split
################################################################################

# use this space to set up testing and validation sets using train/test split

# Note: Be sure to set test_size = 0.25

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

# preparing explanatory variable data
original_df_data   = original_df.loc[ : , x_variables]

original_df_data.info()

# preparing response variable data
original_df_target = original_df.loc[:, 'REVENUE']



# Train/Test Split
# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
            original_df_data,
            original_df_target,
            test_size = 0.25,
            random_state = 222)

################################################################################
# Final Model (instantiate, fit, and predict)
################################################################################

# use this space to instantiate, fit, and predict on your final model




# INSTANTIATING a model object
lasso_model = sklearn.linear_model.Lasso()

# FITTING the training data
lasso_fit = lasso_model.fit(X_train, y_train)


# PREDICTING on new data
lasso_pred = lasso_model.predict(X_test)

print('Training Score:', lasso_model.score(X_train, y_train).round(4))
print('Testing Score:',  lasso_model.score(X_test, y_test).round(4))


################################################################################
# Final Model Score (score)
################################################################################

# use this space to score your final model on the testing set
# MAKE SURE TO SAVE YOUR TEST SCORE AS test_score
# Example: test_score = final_model.score(X_test, y_test)

test_score = lasso_model.score(X_test, y_test)



