import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from call_function import call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    system_prompt = """
    You are a helpful AI coding agent.
    
    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files
    
    When the user asks about the code project, they are referring to the working directory. So you should typically start by looking at the project files and figure out how to run the project and run it's tests.
    You'll always want to test the project and run it's tests and make sure the behavior is working as intended.
    All paths you provide should be relative to the working directory. 
    You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    Any time you are asked to write code, you should make sure to include a comment above the change you made explaining what the change was and how this new implementation works..
    """
    
    if len(sys.argv) <2:
        print("Please provide a prompt")
        sys.exit()

    # print("Args:", sys.argv)
    user_prompt = sys.argv[1]
    
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    # print(messages)
    
    # available functions
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )
    
    max_iterations = 20
    
    for i in range(0, max_iterations):
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            # if the user provides an argument, use it as the prompt, otherwise use the default prompt
            # contents=sys.argv[1] if len(sys.argv) > 1 else 'What color is the sky?',
            # have to update the messages array with the new messages, previous line just repeats same message
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
        )
        
        # print(response.candidates)
        
        if response is None or response.usage_metadata is None:
            print("Response is malformed")
            return
        
        # check if the user provided the --verbose flag, 
        # if so, print the user prompt, the prompt tokens, and the response tokens
        verbose = len(sys.argv) > 2 and sys.argv[2] == "--verbose"
        
        if verbose:
            print(f"User prompt: {user_prompt}")
            # prints the tokens used by the model
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            # prints the tokens used by the model for the response
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            # print("API Key:", api_key)
        
        # put all the functionas the model wants to call in the array, then we call the messages
        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue
                messages.append(candidate.content)
        
                    
        # if the model wants to call a function, we call the function and add the result to the messages array
        if response.function_calls:
            for function_call in response.function_calls:
                result = call_function(function_call, verbose)
                messages.append(result)
        else:
            # prints the response from the model 
            # final agent text message
            print(response.text)
            return
    
    
    
    
# main()
# print(get_file_content("calculator", "pkg"))
# print(get_file_content("calculator", "lorem.txt"))
main()