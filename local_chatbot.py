import os
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from difflib import get_close_matches

# Load HR data from CSV
def load_hr_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return {row['question'].strip().lower(): row['answer'] for _, row in data.iterrows()}
    except Exception as e:
        print(f"Error loading HR data: {e}")
        return {}

# Find closest matching question
def find_closest_question(user_query, question_list):
    matches = get_close_matches(user_query, question_list, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Initialize chatbot model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Avoid padding issues by setting the pad token
tokenizer.pad_token = tokenizer.eos_token

# Load static HR data
data_file = os.path.join("data", "hr_data.csv")
static_responses = load_hr_data(data_file)

# User memory for name tracking
user_memory = {}

# Default fallback response
fallback_response = "I'm sorry, I don't have an answer for that right now. Could you please clarify or ask something else?"

print("Chatbot is ready! Type 'exit' to stop.")

while True:
    user_input = input("You: ").strip()

    # Exit condition
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Name setting and retrieval
    if user_input.lower().startswith("my name is"):
        user_name = user_input[11:].strip()
        user_memory['name'] = user_name
        print(f"Chatbot: Nice to meet you, {user_name}!")
        continue

    if user_input.lower() in ["what's my name?", "what is my name?"]:
        if 'name' in user_memory:
            print(f"Chatbot: Your name is {user_memory['name']}.")
        else:
            print("Chatbot: I don't know your name yet. Please tell me by saying 'My name is [Your Name]'.")
        continue

    # Static HR responses
    normalized_input = user_input.strip().lower()
    closest_question = find_closest_question(normalized_input, static_responses.keys())

    if closest_question:
        print(f"Chatbot: {static_responses[closest_question]}")
        continue

    # Dynamic response using the model
    try:
        inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True)
        outputs = model.generate(**inputs, max_length=200, pad_token_id=tokenizer.pad_token_id, do_sample=True, temperature=0.7)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Fallback for irrelevant responses
        if response.lower() == user_input.lower() or len(response) < 10:
            print(f"Chatbot: {fallback_response}")
        else:
            print(f"Chatbot: {response}")
    except Exception as e:
        print(f"Chatbot: {fallback_response} (Error: {str(e)})")
