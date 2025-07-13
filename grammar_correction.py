import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def correct_grammar(text: str, lang: str) -> str:
    prompt = f"Correct the following {lang} sentence:\n{text}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=60,
        temperature=0
    )
    return response.choices[0].text.strip()