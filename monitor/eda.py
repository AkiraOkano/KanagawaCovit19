'''
Created on 2020/02/25

@author: aokan
'''
import collections
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import HTML, display
import patsy
from matplotlib import rcParams

def getFig():
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

    pd.options.display.max_rows = 1000
    pd.options.display.max_columns = 20

    fig = plt.figure()
    fig.subplots_adjust(bottom=0.1, left=0.1, top=0.9, right=0.9,wspace=0.2,hspace=0.5)
    #fig.subplots_adjust(bottom=1)
    data = pd.read_csv('神奈川COVIT19.csv',encoding="SHIFT-JIS")

    kyoju = collections.Counter(data['居住地'])
    values, counts = zip(*kyoju.most_common())
    ax1 = fig.add_subplot(2, 2, 1)
    #ax1.bar(kyoju.keys(), kyoju.values(), color="#9999ff", width=0.5)
    ax1.bar(values, counts, color="#9999ff", width=0.5)
    ax1.tick_params(axis='x', labelrotation= 90)
    ax1.set_title("発生地")

    age = collections.Counter(data['年代'])

    agesex=pd.pivot_table(data, index='年代', columns='性別', values='ID', aggfunc='count',fill_value=0)

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.bar(agesex.index.values.tolist(), agesex['男'].tolist(), color="#9999ff", width=4)
    ax2.bar(agesex.index.values.tolist(), agesex['女'].tolist(), bottom=agesex['男'].tolist(), color="#ff9999", width=4)
    ax2.legend(["男", "女"],fontsize=6)
    ax2.set_title("年代別")

    ax3 = fig.add_subplot(2, 2, 3)
    agestatus=pd.pivot_table(data, index='年代', columns='状況', values='ID', aggfunc='count',fill_value=0)
    x=agestatus.index.values.tolist()
    dead=agestatus['死亡'].tolist()
    severe=agestatus['重症'].tolist()
    hospital=agestatus['入院'].tolist()
    home=agestatus['自宅'].tolist()
    chiyu=agestatus['退院'].tolist()

    ax3.bar(x, dead, color="tab:blue", width=4)
    ax3.bar(x, severe, bottom=dead, color="tab:orange", width=4)
    bottom=dead
    bottom = (np.array(dead) + np.array(severe)).tolist()
    ax3.bar(x, hospital, bottom=bottom, color="tab:green", width=4)
    bottom = (np.array(bottom) + np.array(hospital)).tolist()
    ax3.bar(x, home, bottom=bottom, color="tab:red", width=4)
    bottom = (np.array(bottom) + np.array(home)).tolist()
    ax3.bar(x, chiyu, bottom=bottom, color="tab:cyan", width=4)
    ax3.set_title("年代別状況")
    ax3.legend(["死亡", "重症","入院","自宅","退院"],fontsize=6)
    return fig
 #   plt.show()