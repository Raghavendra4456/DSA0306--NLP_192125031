import openai
openai.api_key = 'YOUR_API_KEY'
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,  
        temperature=0.7,  
    )
    return response.choices[0].text.strip()
def main():
    prompt = "Once upon a time, in a land far, far away,"
    generated_text = generate_text(prompt)
    print(generated_text)
if __name__ == "__main__":
    main()
