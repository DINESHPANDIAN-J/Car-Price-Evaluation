import streamlit as st
import pickle
import numpy as np
from scipy.stats import boxcox

# Load the trained model
with open('best_model.pkl', 'rb') as f:
    model_data = pickle.load(f)
    best_model = model_data['model']

# Streamlit UI
st.title('Car Price Evaluation')

# Add image
image_path = 'app_image.jpg'
st.image(image_path, caption='Car Image', use_column_width=True, output_format='JPEG')

# Function to preprocess input features
def preprocess_input(kilo_meter, owner_no, model_year, registration_year, fuel_type, seats, engine_displacement,
                     transmission, year_manufacture, mileage, no_of_cylinder, valves_per_cylinder, max_power,
                     max_torque, build_type, oem, insurance_validity):
    # Convert categorical features to binary
    fuel_type_bin = 1 if fuel_type == 'Diesel' else 0
    transmission_bin = 1 if transmission == 'Automatic' else 0

    # Perform one-hot encoding for categorical features
    build_type_encoded = np.array([1 if build_type == b_type else 0 for b_type in ['Hatchback', 'MUV', 'SUV', 'Sedan']])
    oem_encoded = np.array([1 if oem == o else 0 for o in ['Honda', 'Maruti', 'Tata', 'Hyundai', 'Chevrolet', 'Toyota',
                                                           'Ford', 'Skoda', 'Volkswagen', 'Nissan', 'Mahindra',
                                                           'Renault', 'Datsun', 'Kia', 'MG']])
    insurance_validity_encoded = np.array([1 if insurance_validity == i else 0 for i in ['Comprehensive',
                                                                                         'Not Available',
                                                                                         'Third Party insurance',
                                                                                         'Zero Dep']])

    # Apply Box-Cox transformation to kilometer
    Km_transformed_value = boxcox(kilo_meter + 1, lmbda=0.5577997790766174)  # Adding 1 to avoid zero values

    # Create features array
    features1 = np.array([Km_transformed_value, owner_no, model_year, registration_year, fuel_type_bin, seats,
                          engine_displacement, transmission_bin, year_manufacture, mileage, no_of_cylinder,
                          valves_per_cylinder, max_power, max_torque])
    features = np.concatenate([features1, build_type_encoded, oem_encoded, insurance_validity_encoded])

    return features

# Function to perform prediction
def predict_price(features):
    predicted_price = best_model.predict(features.reshape(1, -1))
    return predicted_price



# Input fields
kilo_meter = st.number_input('Kilometer', value=120000)
owner_no = st.number_input('Owner No', value=3)
model_year = st.number_input('Model Year', value=2015)
registration_year = st.number_input('Registration Year', value=2015)
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel'])
seats = st.number_input('Seats', value=5)
engine_displacement = st.number_input('Engine Displacement', value=998)
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
year_manufacture = st.number_input('Year of Manufacture', value=2015)
mileage = st.number_input('Mileage', value=23.1)
no_of_cylinder = st.number_input('Number of Cylinders', value=3)
valves_per_cylinder = st.number_input('Valves per Cylinder', value=4)
max_power = st.number_input('Max Power', value=67.04)
max_torque = st.number_input('Max Torque', value=90)
build_type = st.selectbox('Build Type', ['Hatchback', 'MUV', 'SUV', 'Sedan'])
oem = st.selectbox('OEM', ['Maruti', 'Honda', 'Tata', 'Hyundai', 'Chevrolet', 'Toyota', 'Ford', 'Skoda',
                            'Volkswagen', 'Nissan', 'Mahindra', 'Renault', 'Datsun', 'Kia', 'MG'])
insurance_validity = st.selectbox('Insurance Validity', ['Comprehensive', 'Not Available', 'Third Party insurance',
                                                         'Zero Dep'])

# Preprocess input
features = preprocess_input(kilo_meter, owner_no, model_year, registration_year, fuel_type, seats, engine_displacement,
                            transmission, year_manufacture, mileage, no_of_cylinder, valves_per_cylinder, max_power,
                            max_torque, build_type, oem, insurance_validity)

# Perform prediction
if st.button('Predict'):
    predicted_price = predict_price(features)
    formatted_price = "{:.2f}".format(predicted_price[0])
    st.success(f'Predicted Car Price: {formatted_price} Lakhs')

