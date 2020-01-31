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
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.linear_model
from sklearn.neighbors import KNeighborsRegressor # KNN for Regression


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



# concatenating with original DataFrame
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

#grouping by meail domains
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


#dummy for MAster classes
from sklearn import preprocessing

le = preprocessing.LabelEncoder()
le.fit(housing['MASTER_CLASSES_ATTENDED'])

list(le.classes_)



lb_style_2 = LabelBinarizer()
lb_results_2 = lb_style_2.fit_transform(housing["MASTER_CLASSES_ATTENDED"])
dummy_2=pd.DataFrame(lb_results_2, columns=le.classes_)
dummy_2.head()

#concatenate for Master Classes

dummy_2.columns=['Zero_Master_Class',"One_Master_Class","Two_Master_Class","Three_Master_Class"]

dummy_2.head()
housing = pd.concat([housing, dummy_2.iloc[:,0:4]],
                     axis = 1)

housing['Three_Master_Class'].tail(100)

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
revenue_hi=4000
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




# making a copy of housing
housing_explanatory = housing.copy()


# dropping SalePrice and Order from the explanatory variable set
housing_explanatory = housing_explanatory.drop(['REVENUE'], axis = 1)


# formatting each explanatory variable for statsmodels
for val in housing_explanatory:
    print(f"housing['{val}'] +")





# building a full model
    
#DECLARING SET OF X VARIABLES

x_variables = ['CROSS_SELL_SUCCESS','TOTAL_MEALS_ORDERED','UNIQUE_MEALS_PURCH','CONTACTS_W_CUSTOMER_SERVICE',
               'PRODUCT_CATEGORIES_VIEWED' ,'AVG_TIME_PER_SITE_VISIT' ,'MOBILE_NUMBER' ,'CANCELLATIONS_BEFORE_NOON' ,
               'CANCELLATIONS_AFTER_NOON' ,'TASTES_AND_PREFERENCES' ,'MOBILE_LOGINS' ,'PC_LOGINS' ,'WEEKLY_PLAN' ,
               'EARLY_DELIVERIES' ,'LATE_DELIVERIES' ,'PACKAGE_LOCKER' ,'REFRIGERATED_LOCKER' ,'FOLLOWED_RECOMMENDATIONS_PCT' ,
               'AVG_PREP_VID_TIME' ,'LARGEST_ORDER_SIZE' ,'MASTER_CLASSES_ATTENDED' ,'MEDIAN_MEAL_RATING' ,'AVG_CLICKS_PER_VISIT' ,
               'TOTAL_PHOTOS_VIEWED' ,'junk' ,'personal' ,'profesional' ,'OUT_TOTAL_MEALS_ORDERED' ,
               'OUT_CONTACTS_W_CUSTOMER_SERVICE' ,'OUT_AVG_TIME_PER_SITE_VISIT' ,'OUT_TOTAL_PHOTOS_VIEWED' , 'OUT_REVENUE',
               'OUT_AVG_CLICKS_PER_VISIT' ,'OUT_WEEKLY_PLAN' ,'OUT_UNIQUE_MEALS_PURCH' ,'OUT_EARLY_DELIVERIES' ,
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
               'OUT_AVG_CLICKS_PER_VISIT' ,'OUT_WEEKLY_PLAN' ,'OUT_UNIQUE_MEALS_PURCH' ,'OUT_EARLY_DELIVERIES' ,
               'OUT_FOLLOWED_RECOMMENDATIONS_PCT','Zero_Master_Class',"One_Master_Class","Two_Master_Class","Three_Master_Class"]

x_variables_4 = ['TOTAL_MEALS_ORDERED','AVG_PREP_VID_TIME' ,'MEDIAN_MEAL_RATING' ,'AVG_CLICKS_PER_VISIT','Zero_Master_Class']

# looping to make x-variables suitable for statsmodels
for val in x_variables:
    print(f"housing_train['{val}'] +")
    
# looping to make x-variables suitable for statsmodels
for val in x_variables_2:
    print(f"housing_train['{val}'] +") 


# preparing explanatory variable data
housing_data   = housing.loc[ : , x_variables_4]

housing_data.info()

# preparing response variable data
housing_target = housing.loc[:, 'REVENUE']

'''
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
'''
# Train/Test Split
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




# merging X_train and y_train so that they can be used in statsmodels
#housing_train = pd.concat([X_train, y_train], axis = 1)

'''
housing_train = pd.concat([X_train, y_train], axis = 1)
# Step 1: build a model
lm_best = smf.ols(formula = """ REVENUE ~ housing_train['CROSS_SELL_SUCCESS'] +
                                housing_train['TOTAL_MEALS_ORDERED'] +
                                housing_train['UNIQUE_MEALS_PURCH'] +
                                housing_train['CONTACTS_W_CUSTOMER_SERVICE'] +
                                housing_train['PRODUCT_CATEGORIES_VIEWED'] +
                                housing_train['AVG_TIME_PER_SITE_VISIT'] +
                                housing_train['MOBILE_NUMBER'] +
                                housing_train['CANCELLATIONS_BEFORE_NOON'] +
                                housing_train['CANCELLATIONS_AFTER_NOON'] +
                                housing_train['TASTES_AND_PREFERENCES'] +
                                housing_train['MOBILE_LOGINS'] +
                                housing_train['PC_LOGINS'] +
                                housing_train['WEEKLY_PLAN'] +
                                housing_train['EARLY_DELIVERIES'] +
                                housing_train['LATE_DELIVERIES'] +
                                housing_train['PACKAGE_LOCKER'] +
                                housing_train['REFRIGERATED_LOCKER'] +
                                housing_train['FOLLOWED_RECOMMENDATIONS_PCT'] +
                                housing_train['AVG_PREP_VID_TIME'] +
                                housing_train['LARGEST_ORDER_SIZE'] +
                                housing_train['MASTER_CLASSES_ATTENDED'] +
                                housing_train['MEDIAN_MEAL_RATING'] +
                                housing_train['AVG_CLICKS_PER_VISIT'] +
                                housing_train['TOTAL_PHOTOS_VIEWED'] +
                                housing_train['junk'] +
                                housing_train['personal'] +
                                housing_train['profesional'] +
                                housing_train['OUT_TOTAL_MEALS_ORDERED'] +
                                housing_train['OUT_CONTACTS_W_CUSTOMER_SERVICE'] +
                                housing_train['OUT_AVG_TIME_PER_SITE_VISIT'] +
                                housing_train['OUT_TOTAL_PHOTOS_VIEWED'] +
                                housing_train['OUT_AVG_CLICKS_PER_VISIT'] +
                                housing_train['OUT_WEEKLY_PLAN'] +
                                housing_train['OUT_UNIQUE_MEALS_PURCH'] +
                                housing_train['OUT_EARLY_DELIVERIES'] +
                                housing_train['OUT_FOLLOWED_RECOMMENDATIONS_PCT']""",
                                data=housing_train)

# Step 2: fit the model based on the data
results = lm_best.fit()



# Step 3: analyze the summary output
print(results.summary())


# Step 1: build a model
lm_best_2 = smf.ols(formula =   """ REVENUE ~ housing_train['TOTAL_MEALS_ORDERED'] +
                                housing_train['UNIQUE_MEALS_PURCH'] +
                                housing_train['CONTACTS_W_CUSTOMER_SERVICE']  +
                                housing_train['AVG_TIME_PER_SITE_VISIT'] +
                                housing_train['WEEKLY_PLAN']+
                                housing_train['AVG_PREP_VID_TIME'] +
                                housing_train['LARGEST_ORDER_SIZE'] +
                                housing_train['MASTER_CLASSES_ATTENDED'] +
                                housing_train['MEDIAN_MEAL_RATING'] +
                                housing_train['TOTAL_PHOTOS_VIEWED'] +
                                housing_train['junk'] +
                                housing_train['profesional'] +
                                housing_train['OUT_CONTACTS_W_CUSTOMER_SERVICE'] +
                                housing_train['OUT_TOTAL_PHOTOS_VIEWED'] +
                                housing_train['OUT_AVG_CLICKS_PER_VISIT'] +
                                housing_train['OUT_WEEKLY_PLAN'] """,
                                data=housing_train)

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


#LOGISTIC REGRESSION CROSS SELL SUCCESS

count_no_success = len(housing[housing['CROSS_SELL_SUCCESS']==0])
count_no_success
count_success = 1946-count_no_success
count_success
pct_of_no_sucess = count_no_success/(count_no_success+count_success)
print("percentage of no of cross sell sucess is", pct_of_no_sucess *100 )
pct_of_sub = 1-pct_of_no_sucess
print("percentage of of cross sell sucess is", pct_of_sub*100)


category_1=housing.groupby('domain_group').mean()

category_1['REVENUE']

category_2 = housing.groupby('CROSS_SELL_SUCCESS').mean()
category_2


#Logistic Regression Model Fitting
X=housing.loc[:,x_variables_3]
y=housing.loc[:,'CROSS_SELL_SUCCESS']

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

#Predicting the test set results and calculating the accuracy

y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))


#Confusion Matrix

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#Interpretation: Of the entire test set, 80% of the promoted HALF WAY THERE were liked by customers, hence sucessful. 
#Of the entire test set, 80% of the customer’s preferredhalf way there.

category_4=housing.groupby("TASTES_AND_PREFERENCES").mean()
print(category_4)