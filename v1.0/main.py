import streamlit as st
import pandas as pd
from PIL import Image
import csv
import os

# Load topwear and bottomwear CSVs
topwearDf = pd.read_csv('topwear.csv')
bottomwearDf = pd.read_csv('bottomwear.csv')

# Display a random outfit
def generateRandomOutfit():
    topwear = topwearDf.sample(1).iloc[0]
    bottomwear = bottomwearDf.sample(1).iloc[0]

    topwearImageDir = f"topwearImages/{topwear['id']}.jpg"
    bottomwearImageDir = f"bottomwearImages/{bottomwear['id']}.jpg"

    if os.path.exists(topwearImageDir) and os.path.exists(bottomwearImageDir):
        st.image(Image.open(topwearImageDir), caption=f"Topwear: {topwear['productDisplayName']}")
        st.image(Image.open(bottomwearImageDir), caption=f"Bottomwear: {bottomwear['productDisplayName']}")

    return topwear, bottomwear

# Record User Feedback
def recordFeedback(outfit, feedback, filename='outfitFeedback.csv'):
    # Construct the record dictionary
    record = {
        'topwear_id': outfit[0]['id'],
        'topwear_type': outfit[0]['articleType'],
        'topwear_color': outfit[0]['baseColour'],
        'topwear_gender': outfit[0]['gender'],
        'topwear_name': outfit[0]['productDisplayName'],

        'bottomwear_id': outfit[1]['id'],
        'bottomwear_type': outfit[1]['articleType'],
        'bottomwear_color': outfit[1]['baseColour'],
        'bottomwear_gender': outfit[1]['gender'],
        'bottomwear_name': outfit[1]['productDisplayName'],
        
        'feedback': feedback
    }
    
    # Check if the file exists to determine if we need to write the header
    file_exists = os.path.exists(filename)
    
    # Open the file in append mode
    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=record.keys())
        
        # If the file doesn't exist, write the header
        if not file_exists:
            writer.writeheader()
        
        # Write the record
        writer.writerow(record)

# Streamlit App
st.title("FashionX v1.0")

if 'outfit' not in st.session_state:
    st.session_state.outfit = generateRandomOutfit()

if st.button('👍'):
    recordFeedback(st.session_state.outfit, 'yes')
    st.session_state.outfit = generateRandomOutfit()

if st.button('👎'):
    recordFeedback(st.session_state.outfit, 'no')
    st.session_state.outfit = generateRandomOutfit()