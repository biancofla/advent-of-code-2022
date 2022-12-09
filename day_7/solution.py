import json
import os

def load_data(filename):
    """
        Load data from file.

        Args:
            * filename (str): file's name.

        Returns:
            * (dict, list): the file system tree and
            a list containing all the absolute paths.
    """
    with open(filename, "r") as f:
        data = f.read().splitlines()

    # Split commands.
    commands = []  
    for i in range(len(data)):
        command = [data[i]]
        if "$" in data[i]:
            for j in range(i + 1, len(data)):
                if "$" not in data[j]:
                    command.append(data[j])
                else:
                    break
        else:
            continue
        commands.append(command)    

    # Parse commands.
    directories, files = [], []
    for c in commands:
        input_command = c[0]
        if   "cd" in input_command:
            directory_name = input_command.split(" ")[-1]
            if directory_name == "..": files.append({})
            directories.append(directory_name)
        elif "ls" in input_command:
            files_per_path = {}
            for file_info in c[1:]:
                splitted_file_info = file_info.split(" ")
                
                file_size = splitted_file_info[0]
                file_name = splitted_file_info[1]

                if file_size == "dir":
                    files_per_path[file_name] = {}
                else:
                    files_per_path[file_name] = {
                        "file_size": file_size
                    }
            files.append(files_per_path)

    # Get absolute paths.
    absolute_paths = []
    for i in range(len(directories)):
        normalized_path = os.path.normpath(
            "/".join(directories[1: i + 1])
        )
        
        splitted_normalized_path = normalized_path.split("/")
        if splitted_normalized_path[0] == ".":
            splitted_normalized_path[0] = "/"
        else:
            splitted_normalized_path.insert(0, "/")

        absolute_paths.append(splitted_normalized_path)
    
    # Build file system tree.
    file_system = {"/": {}}
    for path, files_per_path in zip(absolute_paths, files):
        if len(files_per_path) > 0: 
            file_system = _insert_node(
                file_system,
                path,
                0,
                files_per_path,
            )
        
    return file_system, absolute_paths
    
def step_1():
    """
        Step 1 implementation.

        Returns:
            * (int): step 1 solution.
    """
    file_system, paths = load_data("./input_1.txt")

    size_per_path = {}
    for path in paths:
        size_per_path["/".join(path)] = _get_directory_size(
            file_system, 
            path, 
            0,
            False
        )

    total_size = 0
    for _, v in size_per_path.items():
        if v < 100001:
            total_size += v

    return total_size

def step_2():
    """
        Step 2 implementation.

        Returns:
            * (int): step 2 solution.
    """
    file_system, paths = load_data("./input_1.txt")

    size_per_path = {}
    for path in paths:
        size_per_path["/".join(path)] = _get_directory_size(
            file_system, 
            path, 
            0
        )
    
    used_space          = size_per_path["/"]
    unused_space        = 70000000 - used_space
    space_to_be_free_up = 30000000 - unused_space

    candidated_directories_to_delete = []
    for k, v in size_per_path.items():
        if v > space_to_be_free_up:
            candidated_directories_to_delete.append(
                (k, v)
            )
    
    return min(
        candidated_directories_to_delete,
        key=lambda x: x[1]
    )[1]

def _insert_node(tree, path, idx, files):
    """
        Insert an element inside a tree.

        Args:
            * tree (dict): input tree.
            * path (list): path to follow.
            * idx (int): index used to move along the path.
            * files (list): content to insert at
            the end of the path.

        Returns:
            * (dict): output tree.
    """
    for file in tree.keys():
        if "file_size" not in tree[file].keys():
            if file == path[idx]:
                if idx == len(path) - 1:
                    tree[file] = files
                else:
                    tree[file] = _insert_node(
                        tree[file],
                        path,
                        idx + 1,
                        files
                    )
    return tree

def _get_directory_size(tree, path, idx, flag=False):
    """
        Get directory size.

        Args:
            * tree (dict): input tree.
            * path (list): path to follow.
            * idx (int): index used to move along the path.
            * flag (bool, default=False): True, if the directory was found;
            False, otherwise (is used internally by the function during the
            recursion).

        Returns:
            * (int): directory size.
    """
    total_size = 0
    for file in tree.keys():
        if "file_size" not in tree[file].keys():
            if file == path[idx]:
                if idx == len(path) - 1:
                    total_size += _get_directory_size(
                        tree[file],
                        path,
                        idx,
                        True
                    )
                else:
                    total_size += _get_directory_size(
                        tree[file],
                        path,
                        idx + 1,
                        False
                    )
            else:
                if flag:
                    total_size += _get_directory_size(
                        tree[file],
                        path,
                        idx,
                        True
                    )
        else:
            if flag:
                total_size += int(
                    tree[file]["file_size"]
                )
    return total_size

if __name__ == "__main__":
    res_step_1 = step_1()
    print(res_step_1)

    res_step_2 = step_2()
    print(res_step_2)
