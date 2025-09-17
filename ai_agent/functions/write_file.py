import os 
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        # makes directory if it doesn't exist
        os.makedirs(working_directory, exist_ok=True)

    try:
        with open(abs_file_path, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{abs_file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Failed to write to "{abs_file_path}": {e}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write to or overwrite, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file or overwrite file with",
            ),
        },
    ),
)