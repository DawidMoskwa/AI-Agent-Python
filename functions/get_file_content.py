import os

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_tagert_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_tagert_dir:
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_dir):
            return (f'Error: File not found or is not a regular file: "{file_path}"')

        max_chars = 10000
        with open(target_dir, "r") as f:
            file_content_string = f.read(max_chars)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {max_chars} characters]'
        return file_content_string
    

    except Exception as e:
        return f"Error: {e}"