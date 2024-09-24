import jieba  # 中文分词
import numpy as np  # 数值计算
import string  # 字符串处理
import sys  # 系统功能
from line_profiler import LineProfiler  # 性能分析
import os  # 文件路径处理

def cos_dist(vec1, vec2):
    # 计算余弦相似度
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))

def remove_punctuation(text):
    # 去除文本中的标点符号
    return text.translate(str.maketrans("", "", string.punctuation))

def remove_stopwords(text, stopwordlist):
    # 去除文本中的停用词
    return " ".join([word for word in jieba.cut(text) if word not in stopwordlist])

def read_file(file_path):
    # 读取文件内容
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "文件不存在。"

def write_to_text_file(content, put_outpath, mode='w'):
    # 将内容写入指定文件
    try:
        with open(put_outpath, mode, encoding='utf-8') as file:
            file.write(content + "\n")
        print(f"内容已成功写入 {put_outpath} 文件。")
    except Exception as e:
        print(f"写入文件时出现错误：{e}")

def create_vector(content1, content2, stopwordlist):
    # 创建文本的词向量
    words1 = remove_stopwords(remove_punctuation(content1), stopwordlist)
    words2 = remove_stopwords(remove_punctuation(content2), stopwordlist)
    key_words = list(set(words1.split() + words2.split()))  # 获取所有关键词
    vector1 = np.array([words1.split().count(word) for word in key_words])
    vector2 = np.array([words2.split().count(word) for word in key_words])
    return vector1, vector2

def process_files(file_path1, file_path2, output_path, stopwordlist):
    # 处理文件，计算相似度并输出结果
    content1 = read_file(file_path1)
    content2 = read_file(file_path2)
    vector1, vector2 = create_vector(content1, content2, stopwordlist)
    similarity = round(cos_dist(vector1, vector2), 2)  # 计算相似度
    write_to_text_file(f"查重文件路径: {file_path1}\n对比文件路径: {file_path2}\n相似度: {similarity}", output_path, 'a')

def main():
    # 主函数
    if len(sys.argv) != 4:
        print("请提供原文文件路径、抄袭文件路径和输出文件路径。")
        return
    stopwordlist = stopword_cut([])  # 停用词列表，假设该函数已定义
    process_files(sys.argv[1], sys.argv[2], sys.argv[3], stopwordlist)

if __name__ == "__main__":
    # 性能分析
    LineProfiler().add_function(cos_dist).add_function(remove_punctuation).add_function(remove_stopwords).add_function(read_file).add_function(write_to_text_file).add_function(create_vector).add_function(process_files).run(main)
