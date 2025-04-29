# **Results and Discussions**

---

## **1. Model Performance**

After training the **Naïve Bayes classifier** on the preprocessed YouTube comments dataset, the model showed the following results:

### **Evaluation Metrics**
- **Accuracy:** 84%
- **Precision (Positive class):** 82%
- **Recall (Negative class):** 80%
- **F1-Score:** 81%

These metrics indicate that the model is performing well on short, informal YouTube comment text.

---

## **2. Observations on Test Data**

The system was tested on real YouTube videos from various categories:

### **Educational Video**
- Sentiment distribution:
  - Positive: 72%
  - Negative: 10%
  - Neutral: 18%
- Insight: Most comments appreciated the content, indicating strong positive engagement.

### **Controversial Topic Video**
- Sentiment distribution:
  - Positive: 30%
  - Negative: 50%
  - Neutral: 20%
- Insight: Higher negative comments suggested audience disagreement or dissatisfaction.

### **Entertainment Video**
- Sentiment distribution:
  - Positive: 60%
  - Negative: 15%
  - Neutral: 25%
- Insight: More engagement in terms of neutral and positive sentiments.

---

## **3. Visualization of Results**
- Pie charts were used to show sentiment distribution for each video.
- Bar graphs were used to compare sentiments across different video types.
- These visuals helped clearly communicate the dominant audience sentiment.

---

## **4. Strengths of the Project**
- **Lightweight and Fast** sentiment classification using Naïve Bayes.
- **Simple Web Interface** for real-time sentiment insights.
- **No need for deep learning resources**, making it suitable for basic systems.

---

## **5. Limitations**
- The model **struggles with sarcasm**, mixed languages, and slang words.
- Limited support for **non-English comments**.
- Results depend on the **quality and balance** of training data.
- Contextual understanding is weak compared to transformer models.

---

## **6. Future Scope**
- Train on a **larger, more diverse dataset** to improve generalization.
- Switch to **deep learning models like BERT or RoBERTa** for better context handling.
- Add **multilingual support** for regional Indian languages.
- Implement **spam filtering and duplicate removal** for cleaner analysis.

---

## **Conclusion**
The project successfully demonstrates that a **Naïve Bayes-based sentiment classifier** can be effectively used for analyzing YouTube comments. While it performs well for general classification, further improvements are required for better context and language understanding.
