import streamlit as st
import pandas as pd
from textblob import TextBlob

# عنوان الصفحة
st.title("Omar-Consultant")

# وصف البرنامج
st.markdown("""
    **Omar-Consultant** هو برنامج ذكي يعمل بالذكاء الصناعي لتقديم استشارات واستراتيجيات 
    مخصصة، تحليل البيانات، وتنظيف الملفات بطريقة احترافية.
""")

# شريط البحث الذكي
query = st.text_input("أدخل سؤالك أو استفسارك:")

if query:
    # تحليل النص باستخدام TextBlob
    analysis = TextBlob(query)
    sentiment = analysis.sentiment

    # عرض النتائج
    st.write(f"تحليل النص: {analysis}")
    st.write(f"المشاعر: {sentiment}")

# تحميل الملفات
uploaded_file = st.file_uploader("تحميل ملف", type=["txt", "csv", "xlsx"])

if uploaded_file is not None:
    # تحديد نوع الملف
    file_type = uploaded_file.type
    st.write(f"نوع الملف: {file_type}")

    if file_type == "text/plain":
        # قراءة ملف نصي
        text = uploaded_file.read().decode("utf-8")
        st.write("محتوى الملف:")
        st.text(text)

        # تحليل النص
        blob = TextBlob(text)
        st.write(f"المشاعر: {blob.sentiment}")

    elif file_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        # قراءة ملف Excel
        df = pd.read_excel(uploaded_file)
        st.write("محتوى الملف:")
        st.dataframe(df)

# قائمة الخدمات الاستراتيجية
st.header("الخدمات الاستراتيجية من Omar-Consultant")
options = ["SWOT Analysis", "PESTEL Analysis", "Business Model Canvas"]
selected_option = st.selectbox("اختر الخدمة:", options)

if selected_option:
    st.write(f"لقد اخترت: {selected_option}")
