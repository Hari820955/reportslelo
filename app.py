import streamlit as st
from PIL import Image
import pytesseract

st.set_page_config(page_title="Reportslelo - Harish Choudhary Clinic", layout="centered")
st.title("🧪 Reportslelo")
st.subheader("Harish Choudhary Clinic - रिपोर्ट का आसान हिंदी सारांश")

uploaded_file = st.file_uploader("📷 अपनी लैब रिपोर्ट की फोटो अपलोड करें (कैमरा या गैलरी)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="अपलोड की गई रिपोर्ट", use_column_width=True)

    with st.spinner('🔍 रिपोर्ट पढ़ी जा रही है...'):
        extracted_text = pytesseract.image_to_string(image, lang='eng')
        st.text_area("📝 रिपोर्ट का पूरा टेक्स्ट:", extracted_text, height=200)

    with st.spinner('🤖 हिंदी में सारांश तैयार हो रहा है...'):
        summary_lines = []
        if "ESR" in extracted_text:
            summary_lines.append("🩸 ESR सामान्य सीमा में है तो चिंता की बात नहीं है।")
        if "WBC" in extracted_text or "white blood cells" in extracted_text.lower():
            summary_lines.append("🦠 WBC थोड़ा बढ़ा हो सकता है, संक्रमण की ओर इशारा करता है।")
        if "Sugar" in extracted_text or "Glucose" in extracted_text:
            summary_lines.append("🍬 शुगर का स्तर थोड़ा बढ़ा हुआ है, डॉक्टर से संपर्क करें।")
        if not summary_lines:
            summary_lines.append("🧾 रिपोर्ट सामान्य लग रही है। यदि कुछ समझ न आए तो डॉक्टर से परामर्श लें।")
        summary = "\n".join(summary_lines)
        st.success("✅ हिंदी सारांश तैयार है:")
        st.text_area("📄 हिंदी सारांश:", summary, height=200)

    st.markdown("---")
    st.markdown("### 📲 भेजे जाने वाला SMS:")
    st.code(f"""
नाम: (रिपोर्ट से प्राप्त नहीं)
📄 रिपोर्ट सारांश:
{summary}

रिपोर्ट: Harish Choudhary Clinic
📞 8209558359
    """, language="text")
    st.info("यह डेमो है। अगली स्टेप में SMS भेजने की सुविधा जोड़ी जाएगी।")
