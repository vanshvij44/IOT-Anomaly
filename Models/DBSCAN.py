import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.metrics import classification_report

# Load preprocessed data
data = pd.read_csv('data/iot23_combined_preprocessed.csv')

# Select features for DBSCAN (e.g., numeric features)
X = data.drop('label', axis=1)  # Ensure your data has a 'label' column for evaluation

# Fit DBSCAN model
dbscan = DBSCAN(eps=0.10, min_samples=5).fit(X)

# Add labels to data
data['dbscan_labels'] = dbscan.labels_

# Generate evaluation metrics (Assuming 'label' is the true label)
print(classification_report(data['label'], data['dbscan_labels'], target_names=["Benign", "Malicious"]))
