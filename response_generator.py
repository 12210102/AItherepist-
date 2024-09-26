import openai

openai.api_key = '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'

def generate_therapist_response(user_input):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"Student: {user_input}\nTherapist:",
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()
