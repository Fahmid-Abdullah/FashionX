import pandas as pd
from keras.models import load_model

# Load the saved model
model = load_model('model.h5')

# Function to predict feedback for a new outfit
def predict_feedback(topwear_type, topwear_color, topwear_gender, bottomwear_type, bottomwear_color, bottomwear_gender):
    input_data = pd.DataFrame({
        'topwear_type': [topwear_type],
        'topwear_color': [topwear_color],
        'topwear_gender': [topwear_gender],
        'bottomwear_type': [bottomwear_type],
        'bottomwear_color': [bottomwear_color],
        'bottomwear_gender': [bottomwear_gender]
    })
    
    print("Input data:")
    print(input_data)
    
    # One-hot encode categorical variables
    input_data_encoded = pd.get_dummies(input_data)
    
    print("One-hot encoded data:")
    print(input_data_encoded)
    
    # Ensure all columns are of type float32
    input_data_encoded = input_data_encoded.astype('float32')
    
    # Make prediction
    prediction = model.predict(input_data_encoded)
    print("Prediction probability:", prediction)
    return 'yes' if prediction >= 0.5 else 'no'

# Example usage for testing
# Record 1
outfit1 = {
    'topwear_type': 'Shirts',
    'topwear_color': 'Green',
    'topwear_gender': 'Men',
    'bottomwear_type': 'Shorts',
    'bottomwear_color': 'Black',
    'bottomwear_gender': 'Men'
}
print("Feedback for Outfit 1:", predict_feedback(**outfit1))  # Should print 'yes'

# Record 2
outfit2 = {
    'topwear_type': 'Sweater',
    'topwear_color': 'Orange',
    'topwear_gender': 'Men',
    'bottomwear_type': 'Trousers',
    'bottomwear_color': 'Grey',
    'bottomwear_gender': 'Women'
}
print("Feedback for Outfit 2:", predict_feedback(**outfit2))  # Should print 'no'