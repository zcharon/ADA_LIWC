# 导入所需的库
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


def create_wordcloud(string):
    """
        为传入图片创造词云
        :return:
        """
    # 创建一个WordCloud对象
    mask = plt.imread("mask.jpg")
    stopwords = STOPWORDS
    stopwords.update(['use', 'HisIQ', '_________________OberfeldwebelAge', '48Gender', 'Non','BinaryPronouns'])
    wordcloud = WordCloud(width=1000, height=1000, background_color="white", mask=mask, stopwords=STOPWORDS).generate(string)

    # 显示词云图像
    plt.figure(figsize=(60, 60))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    # plt.savefig('data/image1.png')
    plt.savefig('data/image2.png')


if __name__ == '__main__':
    columns_to_read = ['post_content']
    df = pd.read_csv('data/LLMs_subset.csv', usecols=columns_to_read)
    data = df['post_content']
    string = '. '.join(data)
    create_wordcloud(string)
