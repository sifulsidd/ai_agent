import os
from dotenv import load_dotenv
from google import genai
import sys 

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # print("Args:", sys.argv[1])
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=sys.argv[1] if len(sys.argv) > 1 else 'What color is the sky?'
    )

    print(response.text)
    if response is None or response.usage_metadata is None:
        print("Response is malformed")
        return
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    # print("API Key:", api_key)
    
main()