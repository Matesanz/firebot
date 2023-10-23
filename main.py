# import openai
import streamlit as st

# # Set up OpenAI API credentials
# openai.api_key = "YOUR_API_KEY"

# # Define function to call GPT-3 and get an answer
# def get_answer(question):
#     prompt = f"Q: {question}\nA:"
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#     answer = response.choices[0].text.strip()
#     return answer

def get_fake_answer(question):
    return "go ask yourself"

# Define Streamlit app
def app():
    st.title("GPT-3 Question Answering")
    question = st.text_input("Enter your question:")
    if st.button("Get answer"):
        answer = get_fake_answer(question)
        st.write(answer)

if __name__ == "__main__":
    app()
