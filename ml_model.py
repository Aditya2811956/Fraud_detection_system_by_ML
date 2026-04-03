import numpy as np
from sklearn.ensemble import IsolationForest

# -------------------------------
# Train Model (once when app starts)
# -------------------------------
def train_model():

    # Base normal behavior data
    base_data = np.array([
        # Slow traffic
        [10, 1], [12, 1.5], [15, 2], [8, 1], [18, 2.5],

        # Moderate city driving
        [20, 3], [25, 4], [30, 5], [28, 4.5], [22, 3.5],

        # Normal delivery movement
        [35, 6], [40, 7], [38, 6.5], [42, 8], [36, 7],

        # Faster movement
        [45, 9], [50, 10], [48, 9.5], [52, 11], [47, 10],

        # Highway
        [55, 12], [60, 13], [58, 12.5], [62, 14], [57, 13],

        # Mixed patterns
        [33, 5.5], [27, 4.2], [41, 7.5], [29, 4.8], [37, 6.8]
    ])

    # -------------------------------
    # Add noise for realistic variation
    # -------------------------------
    noise = np.random.normal(0, 1, base_data.shape)

    normal_data = base_data + noise

    # -------------------------------
    # Train model
    # -------------------------------
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(normal_data)

    return model


# Train model globally
model = train_model()


# -------------------------------
# Prediction Function
# -------------------------------
def get_model_prediction(speed, distance):

    data = np.array([[speed, distance]])

    prediction = model.predict(data)

    return prediction[0]