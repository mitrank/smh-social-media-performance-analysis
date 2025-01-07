from dotenv import load_dotenv
import os
import requests
import streamlit as st

load_dotenv()

BASE_API_URL = os.environ.get("BASE_API_URL")
LANGFLOW_ID = os.environ.get("LANGFLOW_ID")
FLOW_ID = os.environ.get("FLOW_ID")
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = os.environ.get("ENDPOINT")


def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {
        "Authorization": "Bearer " + APPLICATION_TOKEN,
        "Content-Type": "application/json",
    }
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


def main():
    st.title("Social Media Performance Analysis")
    st.text("By - Syntax Terrors")

    st.divider()

    message = st.text_area("Input", placeholder="Get insights about the posts...")

    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a valid input message.")
            return

        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)

            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))


if __name__ == "__main__":
    main()
