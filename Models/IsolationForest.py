from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

# Load preprocessed data
data = pd.read_csv('data/iot23_combined_preprocessed.csv')

# Select features for IsolationForest (e.g., numeric features)
X = data.drop('label', axis=1)  

iso_forest = IsolationForest(contamination=0.1, random_state=42)
data['iso_forest_labels'] = iso_forest.fit_predict(X)

# The model outputs 1 for inliers and -1 for outliers (anomalies).

print("--- Isolation Forest Classification Report ---")
print(classification_report(data['encoded_label'], data['iso_forest_labels'],
                            target_names=["Malicious", "Benign"]))