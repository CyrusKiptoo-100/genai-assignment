from openai import OpenAI

client = OpenAI(api_key="your_openai_api_key")

prompt = "Give me one simple data science tip in one line."

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print("💡 AI-generated tip:", response.choices[0].message.content.strip())
