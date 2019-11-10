import pandas as pd 
import datetime as dt
from datetime import datetime


employee_record = pd.read_csv("employee_data.csv")


ID_list = employee_record["Emp ID"].tolist()
Name_list = employee_record.Name.tolist()	
DOB_list = employee_record.DOB.tolist()	
SSN_list = employee_record.SSN.tolist()	
State_list = employee_record.State.tolist()

def state_function(my_state): 
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

    return us_state_abbrev.get(my_state, "invalid state")



employee_record_zip = zip(ID_list, Name_list, DOB_list, SSN_list, State_list)
first_name_list = []
last_name_list = []
new_DOB_list = []
new_SSN_list = []
new_state_list = []
for ID,name,DOB,SSN,State in employee_record_zip:
    full_name = name.split()
    first_name_list.append(full_name[0])
    last_name_list.append(full_name[1])
    DOB_correct = datetime.strptime(DOB, "%Y-%m-%d").strftime('%m/%d%Y')
    new_DOB_list.append(DOB_correct)
    abv_state = state_function(State)
    new_state_list.append(abv_state)
    new_SSN = f'***-**-{SSN[7]}{SSN[8]}{SSN[9]}{SSN[10]}'
    new_SSN_list.append(new_SSN)

new_employee_df = pd.DataFrame({"ID": ID_list, "First Name": first_name_list, "Last Name": last_name_list, "DOB": new_DOB_list, "SSN": new_SSN_list, "State": new_state_list})
new_employee_df.to_csv("correct_employee_data.csv", index=False)
    


