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
