


def save_papers_to_markdown(papers, output_file):
    """
    将 papers 列表中的论文信息保存为 Markdown 文件。

    :param papers: 包含论文信息的字典列表
    :param output_file: 输出的 Markdown 文件路径
    """
    with open(output_file, 'w', encoding='utf-8') as md_file:
        for i, paper in enumerate(papers, start=1):
            # 写入标题
            md_file.write(f"## {i}. {paper.get('title', 'No Title')}\n\n")

            # 写入作者和出版信息
            authors = paper.get('authors', 'Unknown Authors')
            publication = paper.get('publication', 'Unknown Publication')
            md_file.write(f"**Authors:** {authors}\n\n")
            md_file.write(f"**Publication:** {publication}\n\n")

            # 写入摘要
            abstract = paper.get('abstract', 'No abstract available.')
            md_file.write(f"**Abstract:** {abstract}\n\n")

            # 写入链接（如果有）
            link = paper.get('link')
            if link:
                md_file.write(f"**Link:** [{link}]({link})\n\n")
            else:
                md_file.write("**Link:** Not available\n\n")

            # 写入结论（如果有）
            conclusion = paper.get('conclusion')
            if conclusion:
                md_file.write(f"**Conclusion:** {conclusion}\n\n")

            # 添加分隔线
            md_file.write("---\n\n")

    print(f"Markdown 文件已保存到: {output_file}")