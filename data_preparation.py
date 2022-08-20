import os
import pandas as pd
import os
import numpy as np


""" Data preparation steps for X features.
    Following methods define feature selection from every source file 
    and creation of final combined feature datasets. 
    Apllied and used for both data modalities - audio and visual seperately.  

"""


# Selecting necessary features from source files
# --- PARAMETERS ---
#   audio data: column_start = 2 
#   visual data: column_start = 5
def select_features_all(file_df, columns_start):
    file_df = file_df.iloc[:, columns_start:]
    return file_df


# Creating a combined data collection for each modality
# --- PARAMETERS ---
#   audio data: column_start = 2, delimiter_char = ';'
#   visual data: column_start = 5, delimiter_char = ','
def prepare_x_data(file_location, delimiter_char, columns_start, scaler):
    X = []
    
    for file in os.scandir(file_location):
        temp_df = pd.read_csv(file, delimiter=delimiter_char)
        temp_df = select_features_all(temp_df, columns_start)
        temp_df = scaler.fit_transform(temp_df)
        temp_df = pd.DataFrame(temp_df)
        X.append(temp_df)
        
    return X


# Reshaping feature data for the model fitting.
def reshape_X(x_data):
    x_shaped = np.array(x_data).reshape((1, x_data.shape[0], -1))
    
    return x_shaped



""" Data preparation steps for Y labels.
    Following methods define label selection for train and prediction data sets.
    As well as simple methods for labels into necessary data format. 

"""

# Selecting necessary labels from source file
# --- PARAMETERS ---
#   Train data: start_index = 0, end_index = 60
#   Prediction data: start_index = 60, end_index = 164
def get_Y_labels(file_location, start_index, end_index, scaler):
    init_labels_df = pd.read_csv(file_location, delimiter=',')
    labels_df = init_labels_df.drop(init_labels_df.columns[[1,2,3,6]], axis=1) 
    labels_df = labels_df.iloc[start_index:end_index]
    labels_df.reset_index(inplace=True)
    y_label = labels_df['Total_YMRS']
    y_label = scaler.fit_transform(y_label.to_numpy().reshape(-1, 1))
        
    return y_label

    
    
# Unscaling label data to initial YMRS score scale
def unscale_Y(y_scaled, scaler):
    unscaled = scaler.inverse_transform(y_scaled)
    
    return unscaled



# Reshaping label data for model training
# --- PARAMETERS ---
#   n_samples = len(x_train)
#   timesteps = 1
#   features = 1
def reshape_Y(y_labels, n_samples, timesteps, features):
    y_shaped = np.array(y_labels).reshape((n_samples, timesteps, features)) 

    return y_shaped



