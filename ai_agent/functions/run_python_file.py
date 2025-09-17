import os 
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_file_path.endswith('.py'):
        return f'Error: "{abs_file_path}" is not a Python file.'

    try:
        final_args = ["python3", abs_file_path]
        final_args.extend(args)
        output = subprocess.run(final_args, 
                                cwd=abs_working_directory, 
                                timeout=30,
                                capture_output=True, 
                                )
        # print(output)
        # format output with markdown code block
        final_string = f"""
    STDOUT: {output.stdout}
    STDERR: {output.stderr}
    """
        
        if output.stdout == "" and output.stderr == "":
            final_string = "No output produced.\n"
        
        if output.returncode != 0:
            final_string += f"Process exited with code {output.returncode}"
            
        return final_string
    
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments, constrained to the working directory. Accepts additional CLI arguments as a list of strings.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file that is run relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings to be used as CLI arguments for the python file",
                items= types.Schema(
                    type=types.Type.STRING,
                    description="A string to be used as a CLI argument for the python file"
                )
            ),
            
        },
    ),
)