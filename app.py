from openai import OpenAI

client = OpenAI(api_key="ask123456")

print("AI Guess Game ")
print("AI picked a word. Try to guess!\n")

# AI makes secret word
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Pick a secret word (one word only)."}]
)
secret = resp.choices[0].message.content.strip().lower()

# game loop
while True:
    guess = input("Your guess: ").lower()
    if guess == secret:
        print("You got it!")
        break
    else:
        # ask AI for a hint
        hint = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": f"Secret word is {secret}. Give a small hint without saying it."}]
        )
        print("Hint:", hint.choices[0].message.content.strip())


