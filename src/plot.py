import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import warnings


# from src.const.Const import pic_label_font, pic_font_size, pic_tick_font, summary_dir

warnings.filterwarnings("ignore")

pic_label_font = {'style': 'normal', 'weight': 'bold', 'size': 12}
pic_tick_font = fm.FontProperties(style='normal', weight='bold', size=10)
pic_legend_font = {'style': 'normal', 'weight': 'bold', 'size': 9}

def init_plt_years(x_label, y_label, title):
    plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
    # plt.axis('square')

    # plt.grid(ls=(0, (2, 4)), c='black', linewidth=1)

    plt.xlabel(x_label, fontdict=pic_label_font)
    plt.ylabel(y_label, fontdict=pic_label_font)
    ax = plt.gca()
    for xtlabel in ax.get_xticklabels():
        xtlabel.set_fontproperties(pic_tick_font)

    for ytlabel in ax.get_yticklabels():
        ytlabel.set_fontproperties(pic_tick_font)

    bwith = 2
    ax.spines['left'].set_color((0, 0, 0, 1))
    ax.spines['left'].set_linewidth(bwith)
    ax.spines['right'].set_color((0, 0, 0, 1))
    ax.spines['right'].set_linewidth(bwith)
    ax.spines['top'].set_color((0, 0, 0, 1))
    ax.spines['top'].set_linewidth(bwith)
    ax.spines['bottom'].set_color((0, 0, 0, 1))
    ax.spines['bottom'].set_linewidth(bwith)
    # plt.xlim(2005, 2021)
    # plt.ylim(0, 24)
    plt.xticks(rotation=10)
    # plt.yticks(np.asarray([0, 6, 12, 18, 24]), size=pic_font_size)


def rank_priority():
    tips1 = pd.read_csv("../resource/tmpfile/pr-awd.csv")
    plt.figure(figsize=(10, 6))
    init_plt_years('Project','Actionable warning lifespan: day(s)','')

    ax = sns.boxplot(
        x='Project',
        y="Actionable warning lifespan: day(s)",
        hue="Priority",
        width = 0.6,
        data=tips1)
    # plt.rcParams["font.weight"] = "bold"
    # plt.rcParams["axes.labelweight"] = "bold"
    # plt.xlabel('Project', fontsize=10, fontweight='bold')
    # plt.ylabel('Actionable warning lifespan: day(s)', fontsize=10, fontweight='bold')
    plt.legend(loc='upper left', ncol=1, markerscale=1, labelspacing=0, handlelength=1)
    leg = plt.legend(picProjList, loc=8, frameon=True, prop=pic_legend_font, fancybox=False,
                     edgecolor='black', bbox_to_anchor=(0.5, -0.3), ncol=5, labelspacing=0.4, columnspacing=0.4,
                     handletextpad=0.1)
    leg.get_frame().set_linewidth(2)
    plt.show()
    # plt.savefig("tmp2", bbox_inches='tight', dpi=1000)

if __name__ == '__main__':
    rank_priority()