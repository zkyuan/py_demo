import random

from icecream import ic

"""
安装第三方库超时：
pip --default-timeout=100 install 模块名称 -i 国内镜像网址 --trusted-host 信任国内镜像网址地址 

清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学：https://pypi.mirrors.ustc.edu.cn/simple/
华中科技大学：http://pypi.hustunique.com/
豆瓣镜像地址：http://pypi.douban.com/simple/
"""
# pip --default-timeout=100 install icecream -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn/simple

"""
 * @author: zkyuan
 * @date: 2023/12/27 21:59
 * @descipton:
"""
# 定义规则
rules = """
复合句子 = 句子 , 连词 复合句子 | 句子
连词 = 而且 | 但是 | 不过
句子 = 主语 谓语 宾语
主语 = 龙哥 | 周敏 | 元宝宝
谓语 = 吃 | 玩 | 打
宾语 = 桃子| 蓝球 | 英雄联盟 | 吃鸡 | 云顶之弈 | 女人
"""


def createInfo(message):
    print()


def get_grammer_by_description(description):
    rules_pattern = [r.split('=') for r in description.split('\n') if r.strip()]
    target_with_expend = [(t, ex.split('|')) for t, ex in rules_pattern]
    grammer = {t.strip(): [e.strip() for e in ex] for t, ex in target_with_expend}

    return grammer


def generate_by_grammer(grammer, target='句子'):
    if target not in grammer: return target

    return ''.join([generate_by_grammer(grammer, t) for t in random.choice(grammer[target]).split()])


if __name__ == '__main__':
    print("开始生成100个句子：")
    grammer = get_grammer_by_description(rules)
    # ic(generated)
    # ic(test_v)
    #ic(generate_by_grammer(grammer))
    i = 0
    while i < 100:
        ic(generate_by_grammer(grammer, target='复合句子'))
        i += 1

"""
 * @author: zkyuan
 * @date: 2023/12/23 19:07
 * @descipton: 第一个python注释
 first python program
"""
# num = 3645
# d ='单引号'
# e ="双引号"
# t = """三引号"""
# s = """
#    这是一首简单的歌
#    没有什么独特
#        555
#        555
#    545444
# """
# f = 13.36
# print(d,e,t,s)
# print(d+e+str(36455))
# print(d+"%d"%num+"我真的笑不活啦%d%d"%(num,num))
# print("这是一个浮点数：%.3f"%f)
# print("这是优雅的填充{num}   {f}\n"
#       "但是"
# """
# 视野
# 是的
# 打卡机阿斯顿
# """
# )
