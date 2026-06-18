import os
from google.genai import types

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

    from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)