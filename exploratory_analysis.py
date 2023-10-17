# 导入所需的库
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def create_wordcloud(string):
    """
        为传入图片创造词云
        :return:
        """
    # 创建一个WordCloud对象
    mask = plt.imread("mask.jpg")
    wordcloud = WordCloud(width=800, height=800, background_color="white", mask=mask, stopwords=STOPWORDS).generate(string)

    # 显示词云图像
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


text1 = '^You displayed sanity in this post...until the last paragraph....when you suddenly lost your mind. WTF are you talking ' \
        'about in the last paragraph?Most modern Egyptians ARE indeed mostly descended from the people who built the Pyramids ' \
        'at Giza five thousand years ago. When and how do you think that the ancient Egyptians vanished? And who told you that ' \
        'they vanished?Its true that Spaniards who live in Madrid cant claim that "their ancestors built the Pyramids in ' \
        'Mexico", but modern Mexicans can and do claim that. Most modern Mexicans are Mestizo (mixed European and Native ' \
        'American ancestry)and may not be 100 percent pure Aztecs, but most have a lot of pre columbian indigenious blood. And ' \
        'in some rural areas the modern peasants still speak Nahuatl, or Maya, or Zapotec, or whatever. So they can, and do, ' \
        'claim the builders of Teotihuacan as their own ancestors. The Egypt of the Pharoahs ended with the Persian Empire ' \
        'around 600 BC. Then Egypt was ruled by Greeks, then Romans, and then by the Byzantines. And the Pagan gods were ' \
        'replaced by Coptic Christianity, and finally the Arab followers of Mohammed swept through Egypt in 700 AD- and ' \
        'absorbed Egypt and North Africa into the Muslim Arab culture of today.  But these invaders only added some DNA to the ' \
        'local mix, they didnt replace the local DNA. So there has been a lot of cultural discontinuity between the Egypt of ' \
        'the Pharoahs and modern Egypt. But thats not the same thing as racial discontinuity. '

text2 = "babybird wrote:Yes it is. I'm just saying that I don't think that particular incident was before the original trauma " \
        "occurred.We pinpointed the original trauma and it was a near death experience. And then ongoing trauma after that " \
        "point.If its important enough for you to talk about like this then its important enough to talk to your therapist " \
        "about it. "

if __name__ == '__main__':
    text = text1 + text2
    create_wordcloud(text)
