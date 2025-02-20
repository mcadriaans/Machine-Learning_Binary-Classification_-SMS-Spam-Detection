
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
   python predict.py --message "Win a free iPhone now!"
   ```

### 🏋️‍♂️ Training the Model
To train the spam detection classifier on the dataset, run:  
```bash
python train.py
```
The trained model will be saved in the `models/` directory.

### 📊 Evaluation
The model is evaluated using:
- **Accuracy:** 99%
- **Precision:** 98%
- **Recall:** 94%
- **F1-Score:** 96%

### 🔥 Example Usage
```python
from src.spam_classifier import SpamClassifier

model = SpamClassifier.load("models/spam_model.pkl")
message = "Congratulations! You've won a lottery."
prediction = model.predict(message)
print("Spam" if prediction else "Not Spam")
```

### 📌 To-Do
- [ ] Improve model accuracy
- [ ] Implement real-time email filtering
- [ ] Deploy as a web API

### 🙌 Contributions
Feel free to contribute! Open a pull request or file an issue.

### 📜 License
[MIT License](LICENSE)

---

Feel free to modify or expand on this as needed for your GitHub repository! 🚀

