import pandas as pd

# Read the CSV file into a DataFrame
df_original = pd.read_csv('train-lending-club-columns-used.csv')
df_edit = df_original.copy()

#Check that id is unique
ids = df_edit['id'].unique()
if not(len(ids) == len(df_edit['id'])):
    print("id column is not unique")
else:
    print("id column is unique")

def find_unique_vals(df):
    #Determine unique values for (for enumeration later):
    unique_vals = dict()
    cols =['sub_grade','term','home_ownership','application_type','verification_status','addr_state','loan_status']
    for col in cols:
        uni_vals = df_edit[col].unique()
        uni_vals.sort()
        unique_vals[col] = uni_vals.copy()
    return unique_vals

#Sample 1000 randomly
df_sample = df_edit.sample(1000,replace=False,random_state=42,ignore_index=True)

#Check that all options are represented
unique_ori = find_unique_vals(df_original.copy())
unique_sample =find_unique_vals(df_sample.copy())
for key in unique_ori.keys():
    print(key +"_original: " + str(len(unique_ori[key])))
    print(key + "_sample: " + str(len(unique_sample[key])))
#Write DataFrame to CSV
df_sample.to_csv('train-lending-club-filtered1000.csv', index=False)
