import joblib
from app.model.TrafficState import TrafficState
from joblib import load

class SVMController:
    def __init__(self):
        self.model_path = 'best_model.joblib'
        self.scaler_path = 'scaler.joblib'
        self.clf = load(self.model_path)
        self.scaler = load(self.scaler_path)  # Load the scaler if features need scaling

    def predict(self, features):
        # Apply scaling to the features if a scaler is used
        scaled_features = self.scaler.transform(features)
        prediction = self.clf.predict(scaled_features)
        return TrafficState(prediction)