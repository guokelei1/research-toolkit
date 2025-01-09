import os
import shutil

def move_files_by_cites(src_dir, parent_dir):
    
    created_dirs = []
    """
    在指定目录中搜寻所有以！开头，.html结尾的文件，并根据文件名中的cites字段对它们分类，
    每个分类创建一个文件夹，文件夹名就是cites后面的数字，同时将每个文件移动到它应该存在的文件夹之中。
    
    :param src_dir: 源目录路径
    :param parent_dir: 创建的文件夹的母路径
    """
    for filename in os.listdir(src_dir):
        if filename.endswith(').html'):
            continue
        if filename.endswith('.html'):
            parts = filename.split('_')
            if '!cites' in parts:
                cites_index = parts.index('!cites')
                cites_number = parts[cites_index + 1]
                dest_dir = os.path.join(parent_dir, cites_number)
                
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                    created_dirs.append(dest_dir)
                    print(f"Created directory: {dest_dir}")
                
                src_file = os.path.join(src_dir, filename)
                dest_file = os.path.join(dest_dir, filename)
                
                shutil.move(src_file, dest_file)
                #print(f"Moved {filename} to {dest_dir}")
        
    return created_dirs