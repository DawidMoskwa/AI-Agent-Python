import os

def get_files_info(working_directory : str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_tagert_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_tagert_dir:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not os.path.isdir(target_dir):
            return (f'Error: "{directory}" is not a directory')

        list_of_files = []
        for item in (os.listdir(target_dir)): #returns list of itmes inside target_dir
            item_path = os.path.join(target_dir, item) 
            item_name = (str(item) + ": ")
            item_size = ("file_size=" + str(os.path.getsize(item_path)) + " bytes, ")
            if os.path.isdir(item_path): 
                item_list = f"- {item_name}{item_size}is_dir=True"
                list_of_files.append(item_list)
            else:
                item_list = f"- {item_name}{item_size}is_dir=False"
                list_of_files.append(item_list)
        return "\n".join(list_of_files)     
    except Exception as e:
        return f"Error: {e}"

    




#os.listdir(): List the contents of a directory
#os.path.isdir(): Check if a path points to an existing directory
#os.path.getsize(): Get the size of a file (in bytes)
#.join(): Join a list of strings together with a given separator