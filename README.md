
## 📌 Spam Detection Classification Project

### 📖 Overview
This project is a machine learning-based spam detection classifier that identifies whether a given message is spam or not. It uses **Support Vector Machine (SVM)** trained on the **SMS spam** dataset to classify text messages.

### 🚀 Features
- **Text preprocessing**: Tokenization, stopword removal, stemming.
- **Feature extraction**: TF-IDF vectorization.
- **Classification model**: Support Vector Machine (SVM).
- **Evaluation metrics**: Accuracy, Precision, Recall, F1-score.


### 📂 Project Structure
```
📁 Machine_Learning_Spam-Detection
│── 📂 data               # Dataset files
│── 📂 models             # Saved trained models
│── 📂 notebooks          # Jupyter notebooks for EDA & training
│── 📜 README.md          # Project documentation
│── 📜 predict.py         # Prediction script
│── 📜 requirements.txt   # Dependencies

```

### 🛠 Installation & Setup
1. **Clone the repository**  
   ```bash
   git clone https://github.com/mcadriaans/Machine_Learning_Spam-Detection.git
   cd Machine_Learning_Spam-Detection
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the model on sample data**  
   ```bash
   python predict.py
   ```


### 📊 Evaluation
The performance of the model is assessed through the following metrics::
- **Accuracy:** 99%
- **Precision:** 98%
- **Recall:** 94%
- **F1-Score:** 96%


### 📌 To-Do
- [ ] Improve Spam F1-Score
- [ ] Implement real-time sms filtering
- [ ] Deploy as a web API

### 🙌 Contributions
Feel free to contribute! Open a pull request or file an issue.

### 📜 License
[MIT License](LICENSE)



