import os

from myconfig import *

from parse_html import parse_google_scholar_page
from move_file import move_files_by_cites
from output_doc import save_papers_to_markdown




def main():
    creat_dir = move_files_by_cites(Src_dir,Parent_dir)
    #debug
    creat_dir = [r'C:\Users\Administrator\Documents\Code\research-toolkit\output\13308965713792370561']
    
    for filedir in creat_dir:
        if not os.path.exists(filedir):
            print(f"文件夹路径不存在: {filedir}")
            return
        papers, paper_count = parse_google_scholar_page(filedir)
        print(f"共找到 {paper_count} 篇论文")
        #pprint.pprint(papers)
        save_papers_to_markdown(papers, os.path.join(filedir, 'papers.md'))
        

    
if __name__ == "__main__":
    main()