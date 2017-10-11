## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for file in data_files:
    d = pd.read_csv("schools/{0}".format(file))
    key_name = file.replace(".csv","")
    data[key_name] = d

## 5. Exploring the SAT Data ##

print(data["sat_results"].head())

## 6. Exploring the Remaining Data ##

for key in data:
    print(data[key].head())

## 8. Reading in the Survey Data ##

import pandas as pd

all_survey =  pandas.read_csv("schools/survey_all.txt",delimiter="\t",encoding="windows-1252") 
d75_survey =  pandas.read_csv("schools/survey_d75.txt",delimiter="\t",encoding="windows-1252") 
survey = pd.concat([all_survey,d75_survey], axis = 0)

print(survey.head(5))


## 9. Cleaning Up the Surveys ##

survey["DBN"] = survey["dbn"]

lists = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]

survey = survey.loc[:,lists]
data["survey"] = survey
print(survey.info())


## 11. Inserting DBN Fields ##

data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]

def pad_csd(num):
    str_num = str(num)
    if len(str_num) == 1:
        str_num = "0" + str_num 
    return str_num

data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]
print(data["class_size"]["DBN"].head())
        

## 12. Combining the SAT Scores ##

array = ["SAT Math Avg. Score", "SAT Critical Reading Avg. Score", "SAT Writing Avg. Score"]
for val in array:
    data["sat_results"][val] = pd.to_numeric(data["sat_results"][val],errors="coerce")
    
data["sat_results"]["sat_score"] = data["sat_results"][array[0]] + data["sat_results"][array[1]] + data["sat_results"][array[2]]
print(data["sat_results"]["sat_score"].head())

## 13. Parsing Geographic Coordinates for Schools ##

import re
def lat_ext(string):
    cord = re.findall("\(.+\)", string)
    lat_cord = cord[0].split(",")
    latitude = lat_cord[0].replace("(","")
    return latitude
    return cord

data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(lat_ext)
print(data["hs_directory"].head())


#print(lat_ext("1110 Boston Road\nBronx, NY 10456\n(40.8276026690005, -73.90447525699966)"))
    
    

## 14. Extracting the Longitude ##

import re
import pandas as pd
def lon_ext(string):
    cord = re.findall("\(.+\)", string)
    lat_cord = cord[0].split(",")
    longitude = lat_cord[1].replace(")","")
    return longitude
    

data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(lon_ext)

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors="coerce")
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors="coerce")


print(data["hs_directory"].head())