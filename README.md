# 🎓 Student Performance Predictor

A Machine Learning web application that predicts a student's academic performance based on their academic information.

## 🚀 Features

- Predicts student performance as:
  - 🟢 Good
  - 🟡 Average
  - 🔴 Poor
- Simple and clean user interface
- Machine Learning classification model
- Flask web application
- Real-time prediction
- Responsive dark-themed UI

## 📊 Input Features

The model uses the following student information:

- Study Time
- Previous Failures
- Absences
- First Period Grade (G1)
- Second Period Grade (G2)

## 🤖 Machine Learning

The project uses a classification model trained on student academic data.

The model achieved approximately:

**83.5% Accuracy**

### Performance Classes

| Class | Meaning |
|---|---|
| Good | Strong academic performance |
| Average | Moderate academic performance |
| Poor | Low academic performance |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS

## 📁 Project Structure

```text
student-performance-predictor/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   └── student_model.pkl
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html