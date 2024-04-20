import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "Enter your API key"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def main():
    st.title("GPT-3 Chatbot")

    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if user_input.strip():
            response = chat_with_gpt(user_input)
            st.write("Chatbot:", response)

if __name__ == "__main__":
    main()