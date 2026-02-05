import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "GPT-4o-mini"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

messages = [
    SystemMessage("You are a helpful assistant, reply back in kanglish"),
]

print("Chatbot started! Press Ctrl+C to stop.")

try:
    while True:
        user_input = input("your input: ")
        messages.append(UserMessage(user_input))

        response = client.complete(
            messages=messages,
            temperature=1.0,
            top_p=1.0,
            max_tokens=1000,
            model=model
        )

        assistant_response = response.choices[0].message.content
        print(f"Assistant: {assistant_response}")
        
        # Store the assistant's response for context
        messages.append(response.choices[0].message)

except KeyboardInterrupt:
    print("\nNamaskara! Chatbot stopped.")


