from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import classification_report

# Load preprocessed data
data = pd.read_csv('data/iot23_combined_preprocessed.csv')

# Select features for LOF (e.g., numeric features)
X = data.drop(['label' , 'encoded_label'], axis=1) 


# 2. Get the predictions
data['lof_labels'] = lof.predict(X)

# The model outputs 1 for inliers and -1 for outliers (anomalies).

# 3. Generate and print the classification report
print("\n--- Local Outlier Factor Classification Report ---")
print(classification_report(data['encoded_label'], data['lof_labels'],
                            target_names=["Malicious", "Benign"]))