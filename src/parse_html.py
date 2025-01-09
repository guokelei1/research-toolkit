import os
import sys
from time import sleep
from bs4 import BeautifulSoup
from gpt import  explain_text
from myconfig import *

def parse_google_scholar_page(filedir):
    """
    解析指定文件夹中的所有谷歌学术页面的 HTML 内容，提取论文信息。
    
    :param filedir: 包含 HTML 文件的文件夹路径
    :return: 包含所有论文信息的列表和论文数量
    """
    papers = []
    ct = True

    # 遍历文件夹中的所有 HTML 文件
    for filename in os.listdir(filedir):
        if filename.endswith('.html'):
            filepath = os.path.join(filedir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                html_content = f.read()
                soup = BeautifulSoup(html_content, 'lxml')

                # 查找所有论文条目
                for item in soup.find_all('div', class_='gs_r gs_or gs_scl'):
                    paper_info = {}

                    # 提取标题
                    title_tag = item.find('h3', class_='gs_rt')
                    if title_tag:
                        paper_info['title'] = title_tag.get_text().replace('[PDF]', '').strip()
                        link_tag = title_tag.find('a')
                        if link_tag and 'href' in link_tag.attrs:
                            paper_info['link'] = link_tag['href']
                        else:
                            paper_info['link'] = None  # 如果没有找到链接，设置为 None

                    # 提取作者和出版信息
                    authors_tag = item.find('div', class_='gs_a')
                    if authors_tag:
                        paper_info['authors'] = authors_tag.get_text().split('-')[0].strip()
                        paper_info['publication'] = authors_tag.get_text().split('-')[-1].strip()

                    # 提取摘要
                    abstract_tag = item.find('div', class_='gs_rs')
                    if abstract_tag:
                        paper_info['abstract'] = abstract_tag.get_text().strip()
                    
                    if ct:
                        paper_info['conclusion'] = explain_text(paper_info['title'],paper_info['abstract'], Api_key)
                    papers.append(paper_info)
                    sys.stdout.write(f"\r已经解析到 {len(papers)} 篇论文")
                    sys.stdout.flush()

    return papers, len(papers)