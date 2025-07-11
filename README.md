
### Anomaly Detection in IoT Security

#### **Aim**
The aim of this project is to develop an anomaly detection system for IoT security using various machine learning algorithms. The proposed system aims to detect malicious network traffic in IoT devices by evaluating the performance and computational cost of different models. The best-performing model can be selected based on criteria such as accuracy and efficiency, tailored to the specific requirements of users.

#### **Methodology**
The methodology involves:
1. Capturing network traffic from IoT devices and storing it in a central unit for processing.
2. Using machine learning (ML) and deep learning (DL) algorithms to detect anomalies in the captured traffic.
3. Evaluating multiple algorithms on the basis of performance metrics (accuracy, precision, recall, F1-score) and computational cost.
4. Sending alerts or executing predefined actions (e.g., dropping packets, blacklisting IPs, triggering physical inspections) if an anomaly is detected.

#### **Dataset**
The IoT-23 dataset was used for this study, which consists of network traffic from smart home IoT devices such as Amazon Echo, Philips HUE, and Somfy Door Lock. The dataset includes 23 scenarios with 20 malicious and 3 benign captures, each containing real and labeled traffic for various IoT malware infections. Data is provided in the Zeek `conn.log.labeled` format.

#### **Steps**
1. **Data Preprocessing**
   - Load each dataset scenario separately, skip the first 10 rows, and read the next 100,000 rows to reduce memory consumption.
   - Combine all 23 datasets into a single DataFrame.
   - Drop irrelevant columns such as timestamps and IP addresses.
   - Convert categorical variables (e.g., `proto`, `conn_state`) into numerical representations using one-hot encoding.
   - Fill missing values with 0.
   - Save the preprocessed data as `iot23_combined.csv`.

2. **Machine Learning Algorithms**
   - **DBSCAN**: Used with parameters `eps=0.10` and `min_samples=5` to cluster the data and detect anomalies.
   - **Isolation Forest**: Configured with a contamination level of 0.1 to identify outliers in the dataset.
   - **Local Outlier Factor (LOF)**: Applied with `n_neighbors=20` and a contamination rate of 0.1 to detect local anomalies in the data.

3. **Evaluation Metrics**
   - Each algorithm was evaluated using standard metrics: confusion matrix, precision, recall, and F1-score. These metrics helped determine the model's ability to distinguish between normal and anomalous traffic.

#### **Conclusion**
Based on the evaluation results, the following observations were made:
- **Isolation Forest** generally showed better performance in terms of precision and recall for detecting anomalies, making it suitable for scenarios with a high proportion of normal traffic.
- **DBSCAN** was effective at clustering anomalies in well-separated regions but performed poorly when anomalies were scattered.
- **LOF** performed adequately by detecting local anomalies but had higher false-positive rates compared to Isolation Forest.

Overall, **Isolation Forest** outperformed the other two algorithms in most cases due to its ability to handle a variety of anomaly patterns without prior knowledge of the data distribution. However, each algorithm has its strengths depending on the specific characteristics of the dataset, and choosing the best approach should be based on the specific use case requirements. 

---
