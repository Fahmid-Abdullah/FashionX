# Importing Libraries
import pandas as pd
import os
import shutil

# Loading styles CSV
styles = pd.read_csv('styles.csv')

# Creating directories for topwear and bottomwear
topwearDir = 'topwearImages'
bottomwearDir = 'bottomwearImages'
os.makedirs(topwearDir, exist_ok=True)
os.makedirs(bottomwearDir, exist_ok=True)

# Filter out topwear and bottomwear
topwearDf = styles[styles['subCategory'] == 'Topwear']
bottomwearDf = styles[styles['subCategory'] == 'Bottomwear']

# Function to move images and create CSVs
def move_images_create_csv(styles_df, target_dir, csv_name):
    records = []
    for _, row in styles_df.iterrows():
        image_name = str(row['id']) + '.jpg'
        src_path = f'images/{image_name}'
        dst_path = os.path.join(target_dir, image_name)

        # Moving image
        if os.path.exists(src_path):
            shutil.move(src_path, dst_path)

        # Collecting details for CSV creation
        records.append({
            'id': row['id'],
            'articleType': row['articleType'],
            'baseColour': row['baseColour'],
            'gender': row['gender'],
            'productDisplayName': row['productDisplayName']
        })

    # Create new CSV file with selected details
    new_styles_df = pd.DataFrame(records)
    new_styles_df.to_csv(os.path.join('', csv_name), index=False)

# Move images and create CSVs
move_images_create_csv(topwearDf, topwearDir, 'topwear.csv')
move_images_create_csv(bottomwearDf, bottomwearDir, 'bottomwear.csv')
