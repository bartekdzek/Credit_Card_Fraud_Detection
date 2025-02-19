# 💳 Credit Card Fraud Detection  

## 📖 Project Overview  
This project focuses on detecting fraudulent credit card transactions using **machine learning models**. The dataset used comes from a real-world financial dataset, where the majority of transactions are legitimate, and only a small fraction represents fraud.  

The project consists of:  
- **Exploratory Data Analysis (EDA)** to understand the dataset.  
- **Data Preprocessing** including handling missing values and class balancing.  
- **Model Training & Evaluation** using Logistic Regression, Decision Tree.  
- **Model Deployment** as a web application using Streamlit.  

### Project Goal
The goal of this project is to develop a machine learning model capable of detecting fraudulent credit card transactions to minimize financial losses for banks and customers. Fraud detection is crucial because unauthorized transactions can cause significant financial damage and undermine user trust in payment systems.

### Problem Description
The dataset consists of 284,807 transactions, of which only 492 are fraudulent (approximately 0.172% of all transactions). This indicates a severely imbalanced dataset, meaning standard models may struggle to correctly identify fraud cases as they are significantly outnumbered by legitimate transactions.
All features (except for Time and Amount) have been transformed using Principal Component Analysis (PCA). As a result, we do not have access to the raw transaction details, only their principal components (V1 – V28).

### Scope of Analysis
This project will follow these key steps:
- **Exploratory Data Analysis (EDA)** – statistical summary and distribution of transaction features; visualization using boxplots and correlation heatmaps to detect anomalies; identifying class imbalance and skewness in features
- **Data Preprocessing & Feature Engineering** – handling missing values and outliers; scaling and normalizing numerical features where necessary; balancing the dataset using oversampling (SMOTE) and undersampling techniques.
- **Model Training** – testing different classification models (Logistic Regression, Decision Tree)
- **Deployment & Application** - Saving the best model using Joblib (credit_card_model.pkl). Creating a Streamlit web application (credit_card.py) for real-time fraud detection. Ensuring user-friendly interaction where users input transaction features and receive fraud predictions instantly.

---

## 📊 Dataset Information  
The dataset used in this project is from **Kaggle’s Credit Card Fraud Detection Dataset**, which contains transactions made by European cardholders in **September 2013**.  

🔹 **Source**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)  
🔹 **Features**:  
- The dataset contains **284,807 transactions**, with only **0.17% fraud cases**.  
- Features **V1 to V28** are **PCA-transformed** to anonymize sensitive data.  
- **Amount** represents the transaction amount.  
- **Class**: `0` (Legitimate) | `1` (Fraud).  

---
## How to run app
type "streamlit run credit_card.py"
Then, open http://localhost:8501/ in your browser.

🖥 Usage Instructions
- 1️⃣  Jupyter Notebook (CreditCardFraudDetection.ipynb)

Run this notebook to explore data, train models, and evaluate performance.
It contains EDA, model training, evaluation, and feature importance analysis.
- 2️ Streamlit App (credit_card.py)

Enter transaction feature values as a comma-separated list.
Click "Predict" to see if the transaction is fraudulent.
If the model detects fraud, a warning will be displayed.

📌 Example Input & Prediction
Here’s an example of how the model makes predictions for a given transaction:

📥 User Input (Transaction Features)

📤 Model Output
✅ "The transaction appears to be safe."
or
⚠️ "Warning! The model detected a potential fraud!"

**Expale Transaction Features**: 
- first)
-0.814053958801928,1.53822155691255,1.11568996367136,-0.0516668053669614,0.0923341570300812,-1.0133978787151,0.748850873917274,-0.124813887886896,-0.207406950350359,0.0728417294342756,0.0582845272450801,0.639903034792989,1.42894200092882,-0.830482497203489,0.782317854199766,0.278964105860231,-0.0836263151106963,-0.33330804312115,-0.158428707782224,0.44519893817017,-0.311451578788249,-0.627543768547017,-0.0164685816473858,0.363402524019832,-0.0146310818509394,0.0769141479206171,0.467478413040824,0.228122870012143,1.98
- second)
-2.3122265423263,1.95199201064158,-1.60985073229769,3.9979055875468,-0.522187864667764,-1.42654531920595,-2.53738730624579,1.39165724829804,-2.77008927719433,-2.77227214465915,3.20203320709635,-2.89990738849473,-0.595221881324605,-4.28925378244217,0.389724120274487,-1.14074717980657,-2.83005567450437,-0.0168224681808257,0.416955705037907,0.126910559061474,0.517232370861764,-0.0350493686052974,-0.465211076182388,0.320198198514526,0.0445191674731724,0.177839798284401,0.261145002567677,-0.143275874698919,0

Try it yourself!
