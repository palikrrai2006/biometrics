import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Biometric System", layout="wide")

st.title("🔐 AI Biometric Authentication System")

menu = st.sidebar.selectbox(
    "Navigation",
    ["Enroll User", "Identify User"]
)

# ---------------- ENROLL ----------------

if menu == "Enroll User":
    st.header("👤 Enroll New User")

    name = st.text_input("Enter User Name")
    files = st.file_uploader(
        "Upload 3–5 Face Images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if st.button("Enroll"):
        if name and files:
            with st.spinner("Processing enrollment..."):

                files_data = [
                    ("files", (file.name, file, file.type))
                    for file in files
                ]

                response = requests.post(
                    f"{BACKEND_URL}/enroll",
                    params={"name": name},
                    files=files_data
                )

                if response.status_code == 200:
                    st.success(response.json()["message"])
                else:
                    st.error(response.text)
        else:
            st.warning("Please enter name and upload images.")

# ---------------- IDENTIFY ----------------

if menu == "Identify User":
    st.header("🔍 Identify User")

    file = st.file_uploader(
        "Upload Face Image",
        type=["jpg", "jpeg", "png"]
    )

    if st.button("Identify"):
        if file:
            with st.spinner("Identifying..."):

                files_data = {
                    "file": (file.name, file, file.type)
                }

                response = requests.post(
                    f"{BACKEND_URL}/identify",
                    files=files_data
                )

                if response.status_code == 200:
                    result = response.json()

                    if result["status"] == "Access Granted":
                        st.success(f"✅ {result['name']}")
                        st.metric("Similarity Score", round(result["similarity_score"], 3))
                    else:
                        st.error("❌ Access Denied")
                else:
                    st.error(response.text)
        else:
            st.warning("Upload an image first.")
