import streamlit as st
import pandas as pd

# Title and Description
st.title("Segmentasi Pelanggan Menggunakan Data Hasil Klasifikasi")
st.write("Aplikasi ini menampilkan informasi dan visualisasi data hasil klasifikasi pelanggan.")

# Upload File Data
uploaded_file = st.file_uploader("Unggah file data hasil klasifikasi (CSV):", type="csv")
if uploaded_file is not None:
    # Load data
    data = pd.read_csv(uploaded_file)
    st.write("### Data Hasil Klasifikasi:")
    st.write(data.head())

    # Data Overview
    st.write("### Informasi Data")
    st.write(data.describe())
    st.write("Data memiliki", data.isnull().sum().sum(), "nilai kosong.")

    # Visualizations
    st.write("### Visualisasi Segmentasi Pelanggan")

    # Pie chart for segment distribution
    if 'Segment' in data.columns:
        segment_counts = data['Segment'].value_counts()
        st.write("#### Distribusi Segmentasi")
        fig, ax = plt.subplots()
        ax.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)

    # Bar chart for other categorical columns
    categorical_columns = data.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        if col != 'Segment':
            st.write(f"#### Distribusi untuk {col}")
            fig, ax = plt.subplots()
            sns.countplot(data=data, x=col, order=data[col].value_counts().index, palette='viridis', ax=ax)
            plt.xticks(rotation=45)
            st.pyplot(fig)

    # Correlation heatmap for numerical columns
    st.write("#### Korelasi Antar Fitur")
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
    if len(numerical_columns) > 1:
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(data[numerical_columns].corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    st.write("### Visualisasi Selesai")
else:
    st.write("Silakan unggah file CSV untuk memulai.")
