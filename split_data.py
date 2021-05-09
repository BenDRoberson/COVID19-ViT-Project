### This code was used to help select and create the samples that we utilized for our model ###
### You can find the exact images used in /chest-xray/ or you can utilize the directions below to replicate and/or add samples ###

## This code is to split the COVID-19 data into COVID vs. Not
## I did this to then copy it into the folder with the Kaggle data to then load them together
## github for splitting data, assumes you cloned the repo into the same dir as this file: https://github.com/ieee8023/covid-chestxray-dataset
## github with Kaggle data: I only took "train" (since it's already plenty) and "normal" samples: https://github.com/drkhan107/CoroNet
## we can switch the above to pneumonia (or combine them) very easily

import pandas as pd
import numpy as np
from shutil import copyfile
import os

metadata = pd.read_csv('metadata.csv')
metadata['label'] = np.where(metadata['finding'].str.contains('COVID-19'), 1, 0)

print(metadata.groupby('label').size())

pa_only = metadata.query('view == "PA"')

print(pa_only.groupby('label').size()) # checks out


## store new images
if not os.path.exists("newimages/covid/"):
    os.makedirs("newimages/covid/")

if not os.path.exists("newimages/normal/"):
    os.makedirs("newimages/normal/")

## loop through and copy the images to the correct folder
file_path = 'images/'
for index, row in pa_only.iterrows():
    if row['label'] == 1:
        copyfile(file_path + row["filename"], "newimages/covid/" + row["filename"])
    elif row['label'] == 0:
        copyfile(file_path + row["filename"], "newimages/normal/" + row["filename"])
    else:
        raise ValueError("AHHHHHHHHHH!")
