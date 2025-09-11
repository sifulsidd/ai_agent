import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    if len(sys.argv) <2:
        print("Please provide a prompt")
        sys.exit()

    # print("Args:", sys.argv)
    user_prompt = sys.argv[1]
    
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    # print(messages)
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        # if the user provides an argument, use it as the prompt, otherwise use the default prompt
        contents=sys.argv[1] if len(sys.argv) > 1 else 'What color is the sky?'
    )

    # prints the response from the model 
    print(response.text)
    if response is None or response.usage_metadata is None:
        print("Response is malformed")
        return
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print("User prompt:", user_prompt)
        # prints the tokens used by the model
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        # prints the tokens used by the model for the response
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        # print("API Key:", api_key)
    
main()