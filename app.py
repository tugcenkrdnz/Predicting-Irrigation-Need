import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. Varlıkları Yükle
paket = joblib.load('irrigation_champion_model_v2.pkl')
model = paket['model']
features = paket['features']
target_mapping = paket['target_mapping']

st.set_page_config(page_title="Akıllı Tarım", page_icon="🌱", layout="wide")
st.title("🌱 Akıllı Tarımsal Sulama Karar Destek Sistemi")

# 2. Giriş Alanları (İki Sütunlu Yapı)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧪 Toprak ve Tarla Verileri")
    soil_moisture = st.slider("Toprak Nemi (%)", 0.0, 100.0, 15.0)
    soil_ph = st.slider("Toprak pH", 4.0, 9.0, 6.5)
    organic_carbon = st.slider("Organik Karbon", 0.0, 3.0, 1.2)
    elec_cond = st.slider("Elektriksel İletkenlik", 0.0, 5.0, 1.5)
    field_area = st.number_input("Tarla Alanı (Hektar)", 0.1, 50.0, 5.0)

with col2:
    st.subheader("🌤️ Hava Durumu")
    temp = st.slider("Sıcaklık (°C)", 10.0, 50.0, 42.0)
    humidity = st.slider("Hava Nemi (%)", 0.0, 100.0, 20.0)
    rainfall = st.number_input("Yıllık Yağış (mm)", 0, 4000, 200)
    sunlight = st.slider("Güneşlenme Süresi (Saat)", 0.0, 14.0, 12.0)
    wind_speed = st.slider("Rüzgar Hızı (km/h)", 0.0, 80.0, 35.0)

# Sidebar: Kategorik Seçimler (39 sütunu tamamlamak için şart)
st.sidebar.header("📍 Konum ve Yöntem")
region = st.sidebar.selectbox("Bölge", ["North", "South", "East", "West"])
irr_type = st.sidebar.selectbox("Sulama Yöntemi", ["Drip", "Sprinkler", "Rainfed"])
water_source = st.sidebar.selectbox("Su Kaynağı", ["Rainwater", "Reservoir", "River", "Well"])

if st.button("📊 Analiz Et"):
    # ADIM 1: Modelin beklediği 39 sütunluk boş tabloyu oluştur
    input_data = pd.DataFrame(0, index=[0], columns=features)
    
    # ADIM 2: Sayısal Sütunları Doldur
    input_data['Soil_Moisture'] = soil_moisture
    input_data['Soil_pH'] = soil_ph
    input_data['Organic_Carbon'] = organic_carbon
    input_data['Electrical_Conductivity'] = elec_cond
    input_data['Temperature_C'] = temp
    input_data['Humidity'] = humidity
    input_data['Rainfall_mm'] = rainfall
    input_data['Sunlight_Hours'] = sunlight
    input_data['Wind_Speed_kmh'] = wind_speed
    input_data['Field_Area_hectare'] = field_area
    
    # ADIM 3: One-Hot Kategorik Sütunları İşaretle (1 yap)
    # Bölge
    reg_col = f"Region_{region}"
    if reg_col in features: input_data[reg_col] = 1
    # Sulama Tipi
    irr_col = f"Irrigation_Type_{irr_type}"
    if irr_col in features: input_data[irr_col] = 1
    # Su Kaynağı
    wat_col = f"Water_Source_{water_source}"
    if wat_col in features: input_data[wat_col] = 1
    
    
    # ADIM 4: Tahmin ve Olasılıklar
    probs = model.predict_proba(input_data)[0]
    
    # Senin istediğin o 'High' sonucunu daha hassas yakalamak için eşik değerini kullanalım:
    if probs[2] > 0.40: # High olasılığı %40'ı geçerse doğrudan High de
        result_text = "High"
    else:
        prediction_index = np.argmax(probs)
        result_text = target_mapping[prediction_index]
    
    # ADIM 5: Görselleştirme (Artık result_text tanımlı olduğu için hata vermez)
    st.divider()
    c1, c2 = st.columns([1, 2])
    
    with c1:
        st.metric("Tahmin Edilen İhtiyaç", result_text)
        if result_text == 'High':
            st.error("🚨 Acil Sulama Gerekli!")
        elif result_text == 'Medium':
            st.warning("⚠️ Takip Edilmeli.")
        else:
            st.success("✅ Nem Seviyesi Yeterli.")