import os 

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