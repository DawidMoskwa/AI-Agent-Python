import os



def get_files_info(working_directory : str, directory: str = ".") -> str:
    try:
        working_dict_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dict_abs, directory))
        valid_tagert_dir = os.path.commonpath([working_dict_abs, target_dir]) == working_dict_abs
        if not valid_tagert_dir:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not os.path.isdir(target_dir):
            return (f'Error: "{directory}" is not a directory')
        return (f'Success: "{directory}" is within the working directory')
    except Exception as e:
        return f"Error: {e}"