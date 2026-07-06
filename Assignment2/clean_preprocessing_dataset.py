import pandas as pd

# reading the messy dataset file first
raw_df = pd.read_csv("dirty_preprocessing_dataset.csv")
print("initial size of dataset ->", raw_df.shape)

# remove identical rows if any duplicate entry is there
raw_df = raw_df.drop_duplicates()

# gender values are completely messed up (male, Fem, M, etc)
# creating a simple map to standardise them to just Male and Female
clean_gender_dict = {
    'male': 'Male', 'Male': 'Male', 'M': 'Male',
    'Female': 'Female', 'Fem': 'Female', 'F': 'Female'
}
raw_df['Gender'] = raw_df['Gender'].map(clean_gender_dict)

# income column has some negative values which is impossible
# replacing negative entries with None so we can fix them later
raw_df.loc[raw_df['Income'] < 0, 'Income'] = None

# calculating medians for filling the blank cells
# using median because mean can get affected by extreme outliers
avg_age_val = raw_df['Age'].median()
avg_inc_val = raw_df['Income'].median()

# manually putting the median values where cells are empty/null
raw_df.loc[raw_df['Age'].isnull(), 'Age'] = avg_age_val
raw_df.loc[raw_df['Income'].isnull(), 'Income'] = avg_inc_val

# user_id and join_date are useless for training models later, so dropping them
raw_df = raw_df.drop(columns=['User_ID', 'Join_Date'])

# converting categorical gender to dummy variables
# drop_first=True leaves us with just one column (Gender_Male: 1 or 0)
raw_df = pd.get_dummies(raw_df, columns=['Gender'], drop_first=True, dtype=int)

# -------------------------------------------------------------
# Scaling the numeric columns manually using formula: (x - mean)/std
# -------------------------------------------------------------

# age column scaling
m_age = raw_df['Age'].mean()
s_age = raw_df['Age'].std()
raw_df['Age'] = (raw_df['Age'] - m_age) / s_age

# income column scaling
m_inc = raw_df['Income'].mean()
s_inc = raw_df['Income'].std()
raw_df['Income'] = (raw_df['Income'] - m_inc) / s_inc

# transaction amount column scaling
m_trans = raw_df['Transaction_Amount'].mean()
s_trans = raw_df['Transaction_Amount'].std()
raw_df['Transaction_Amount'] = (raw_df['Transaction_Amount'] - m_trans) / s_trans

# print check to see final shape and data sample
print("final shape after manual cleaning ->", raw_df.shape)
print(raw_df.head(4))

# exporting the final output to a new csv file
raw_df.to_csv("cleaned_preprocessing_dataset.csv", index=False)
print("saved successfully!")