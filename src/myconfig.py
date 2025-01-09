# config.py
Src_dir = r'C:\Users\Administrator\Downloads'
Parent_dir = r'C:\Users\Administrator\Documents\Code\research-toolkit\output'
api_key_file_path = r'C:\Users\Administrator\Documents\Code\research-toolkit\myapi'
def get_api_key(file_path):
    """
    从指定的文件路径读取 API 密钥。
    
    :param file_path: 包含 API 密钥的文件路径
    :return: API 密钥字符串
    """
    with open(file_path, 'r') as file:
        return file.read().strip()

# 示例调用
Api_key = get_api_key(api_key_file_path)