from ntpath import isdir
import os

def get_files_info(working_directory, directory="."):
    # pass in working directory and directory to get the full path
    abs_working_directory = os.path.abspath(working_directory)   
    # pass in the directory to get the full path
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    # if the directory is not inside the working directory, return a string for LLM to understand
    if not abs_directory.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # gives all the files within the directory 
    contents = os.listdir(abs_directory)
    
    final_response = ""
    for content in contents:
        # finds the path to the contents within the folder we are checking 
        content_path = os.path.join(abs_directory, content)
        # checks whether the content is a file or a folder 
        is_dir = os.path.isdir(content_path)
        # then returns the size of the file or folder
        size = os.path.getsize(content_path)
        final_response += f"- {content}: file_size={size} bytes, is_dir={is_dir} \n"
    return final_response

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{abs_file_path}"'
    
    max_chars = 10000
    with open(abs_file_path, 'r') as file:
        file_content_string = file.read(max_chars)
        if len(file_content_string) > max_chars:
            return file_content_string +f'[...File "{abs_file_path}" truncated to first {max_chars} characters]'
        return file_content_string