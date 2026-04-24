# 🌱 Akıllı Tarımsal Sulama Karar Destek Sistemi
### (Smart Irrigation Need Prediction)

Bu proje, Kaggle S6E4 "Predicting Irrigation Need" yarışması kapsamında geliştirilmiş, büyük ölçekli tarımsal verileri analiz ederek tarlaların sulama ihtiyacını tahmin eden uçtan uca bir makine öğrenmesi çözümüdür.

## 🚀 Proje Özeti
Proje, toprak özellikleri (pH, nem, karbon seviyesi vb.) ve meteorolojik verileri (sıcaklık, yağış, rüzgar hızı vb.) kullanarak sulama ihtiyacını üç farklı seviyede (Low, Medium, High) sınıflandırmaktadır. 630.000+ satırlık veri seti üzerinde çalışılmıştır.

## 📊 Model Performansı ve Metrikler
Model, Apple M4 çip mimarisi üzerinde optimize edilerek eğitilmiştir.

* **Algoritma:** Random Forest Classifier
* **Doğruluk Skoru (Accuracy):** %98.59
* **High (Kritik) Sınıf Recall:** %95
* **Özellik Sayısı:** 39 (One-Hot Encoding dahil)

## 🛠️ Kullanılan Teknolojiler
* **Dil:** Python 3.12+
* **Kütüphaneler:** Scikit-learn, Pandas, Numpy, Joblib
* **Arayüz:** Streamlit
* **Donanım:** Apple M4 Pro (14-core CPU, 20-core GPU)

## 📁 Dosya Yapısı
* `app.py`: Streamlit web arayüzü kodu.
* `irrigation_champion_model.pkl`: Eğitilmiş Random Forest model paketi (Model, Features, Mapping).
* `requirements.txt`: Projenin çalışması için gerekli kütüphaneler.
* `README.md`: Proje dokümantasyonu.

## ⚙️ Kurulum ve Kullanım

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/tugcenurkaradeniz/irrigation-prediction.git](https://github.com/tugcenurkaradeniz/irrigation-prediction.git)
    cd irrigation-prediction
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Uygulamayı Çalıştırın:**
    ```bash
    streamlit run app.py
    ```

## 🎯 Karar Destek Sistemi
Uygulama, yüksek sulama ihtiyacı olan durumları yakalamak için olasılık tabanlı bir eşik (Thresholding) kullanmaktadır. Eğer model %40 ve üzerinde "High" ihtimali görürse, kullanıcıyı kırmızı alarm ile uyarmaktadır.


---
*Bu çalışma, veri odaklı tarım ve sürdürülebilir su yönetimi vizyonuyla geliştirilmiştir.*