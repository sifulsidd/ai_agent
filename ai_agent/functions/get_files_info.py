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