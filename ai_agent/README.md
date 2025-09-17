Agent - can continually do prompts until it solves a problem 

4 Tool Calls -
1) Scan files in directory
2) Read files contents 
3) Overwrite a file's contents 
4) Execute python code

Learning Goals: 
1) Introduce you to multi-directory Python projects
2) Understand how AI tools that you'll use work under the hood 
3) Practice Python and functional programming skills 


Read Files Info: 
1) First finds the full directory to working file
2) If there isn't a directory given, just use the working directory as the place we want to point to 
3) If a subfolder is given, find the path to that subfolder 
4) If the abs_directory path doesn't start with working directory path, then we know they aren't on the same path, so we give an error message
5) Then we go to the folder and find all the files within the folder we are looking at 
6) Contents is a list of all those files in the folder 
7) For each item within the folder it asks:
    a) Is this thing a folder or a file
    b) What's the size of the folder or file 

Run Python Files:
1) Check whether the path is to a correct file or not
2) Check whether the file is a Python file or not 
3) If all the above is false, then we run the file 
4) If the path given leads to a process being run, we get the output of the message
5) If stdout and stderror are empty we just say "No output produced" 
6) Then we check the output's returncode, if anything other than 0 is returned, we return the error code as well. 
7) Finally return the output we desire

Call Function File:
1) prints full args if verbose else a short message.
2) Calls the matching function with working_directory and spreads out args(it's an array using ** can make it so each element is an argument).
3) If result is still empty, returns an error message
4) Otherwise prints something with successful result
Impact: This function logs the call, dispatches to the appropriate helper, and wraps the output in types.Content/types.Part.from_function_response for the model to consume.
