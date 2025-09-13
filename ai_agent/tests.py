from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def main():
    # get_files_info tests
    working_directory = "calculator"
    # root_contents = get_files_info(working_directory)
    # print(root_contents)
    # pkg_contents = get_files_info(working_directory, "pkg")
    # print(pkg_contents)
    # bin_contents = get_files_info(working_directory, "/bin")
    # print(bin_contents)
    # go_up_contents = get_files_info(working_directory, "../")
    # print(go_up_contents)
    
    # get_file_content tests
    # lorem_contents = get_file_content(working_directory, "lorem.txt")
    # print(lorem_contents)
    
    # main_contents = get_file_content(working_directory, "main.py")
    # print(main_contents)
    
    # calculator_contents = get_file_content(working_directory, "pkg/calculator.py")
    # print(calculator_contents)
    
    # bin_cat_contents = get_file_content(working_directory, "/bin/cat")
    # print(bin_cat_contents)
    
    # does_not_exist_contents = get_file_content(working_directory, "pkg/does_not_exist.py")
    # print(does_not_exist_contents)
    
    # write_file tests
    print(write_file(working_directory, "lorem.txt", "wait, this isn't lorem ipsum"))
    print(get_file_content(working_directory, "lorem.txt"))
    
    print(write_file(working_directory, "pkg/more_lorem.txt", "lorem ipsum dolor sit amet"))
    print(get_file_content(working_directory, "pkg/more_lorem.txt"))
    
    print(write_file(working_directory, "/tmp/temp.txt", "this should not be allowed"))
    
main()