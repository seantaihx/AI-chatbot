import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_quiz(lang: str, level: str = "beginner") -> str:
    prompt = f"Create a short multiple choice {lang} vocabulary quiz for a {level} learner."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].text.strip()