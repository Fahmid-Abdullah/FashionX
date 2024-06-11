import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense

# Loading feedback data
feedbackDf = pd.read_csv('outfitFeedback.csv')

# Data Preprocessing
# Convert categorical variables to numerical representations
le = LabelEncoder()
for col in feedbackDf.columns:
    if feedbackDf[col].dtype == 'object':
        feedbackDf[col] = le.fit_transform(feedbackDf[col])

# Prepare input features and labels
X = feedbackDf[['topwear_type', 'topwear_color', 'topwear_gender', 'bottomwear_type', 'bottomwear_color', 'bottomwear_gender']]
y = feedbackDf['feedback']

# Define a neural network model with more layers
model = Sequential([
    Dense(128, activation='relu', input_shape=(X.shape[1],)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Update X to use one-hot encoded features
X = pd.get_dummies(feedbackDf[['topwear_type', 'topwear_color', 'topwear_gender', 'bottomwear_type', 'bottomwear_color', 'bottomwear_gender']])

# Compile the model (if needed)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Retrain the model
batch_size = 8
for epoch in range(20):
    for i in range(0, len(X), batch_size):
        X_batch = X.iloc[i:i+batch_size]
        y_batch = y.iloc[i:i+batch_size]
        model.train_on_batch(X_batch, y_batch)

# Saving model (if needed)
model.save('model.h5')

