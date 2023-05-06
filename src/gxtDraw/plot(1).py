import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import warnings

# from src.const.Const import pic_label_font, pic_font_size, pic_tick_font, summary_dir

warnings.filterwarnings("ignore")

pic_label_font = {'style': 'normal', 'weight': 'bold', 'size': 13}
pic_tick_font = fm.FontProperties(style='normal', weight='bold', size=13)
pic_legend_font = {'style': 'normal', 'weight': 'bold', 'size': 9}


def init_plt_years(x_label, y_label, title):
    # plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
    # plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
    # plt.xticks(rotation=0)
    # plt.yticks(rotation=70)

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
    # plt.xticks(rotation=10)
    # plt.yticks(np.asarray([0, 6, 12, 18, 24]), size=pic_font_size)


def priority():
    tips1 = pd.read_csv("../../resource/tmpfile/pr-rk-awd.csv")
    fig = plt.figure(figsize=(8, 7))
    fig.subplots_adjust(bottom=0.15)
    init_plt_years('Prority level', 'Actionable warning lifespan: day(s)', '')
    plt.grid(True)
    ax = sns.boxplot(
        x='Priority level',
        y="Actionable warning lifespan: day(s)",
        hue="Project",
        width=0.6,
        linewidth=2,
        data=tips1)
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    # plt.xticks(rotation=40)
    # plt.legend(loc='upper left', ncol=1, markerscale=1, labelspacing=0, handlelength=1)

    # plt.legend(loc=8, frameon=True, prop=pic_legend_font, fancybox=False,
    #            edgecolor='black', bbox_to_anchor=(0.5, -0.3))
    leg = plt.legend(loc=8, frameon=True, prop=pic_legend_font, fancybox=False,
                     edgecolor='black', bbox_to_anchor=(0.5, -0.2), ncol=5, labelspacing=0.4, columnspacing=0.4,
                     handletextpad=0.1)
    leg.get_frame().set_linewidth(2)

    plt.show()
    # plt.savefig("priotity3", bbox_inches='tight', dpi=1000)


def priority_percentage():
    tips1 = pd.read_csv("../../resource/tmpfile/pr-percentage.csv")
    fig = plt.figure(figsize=(8, 7))
    fig.subplots_adjust(bottom=0.15)
    init_plt_years('Project', 'The density of actionable warnings', '')
    plt.grid(True)
    ax = sns.barplot(
        x='priority',
        y='The density of actionable warnings',
        hue="Project",
        # dodge=True,
        linewidth=2,
        # facecolor=(1, 1, 1, 0),
        errcolor=".2",
        edgecolor=".2",
        data=tips1)
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    # plt.xticks(rotation=40)
    # plt.legend(loc='upper right', ncol=1, markerscale=1, labelspacing=0, handlelength=1)
    pic_legend_font = {'style': 'normal', 'weight': 'bold', 'size': 9}
    leg = plt.legend(loc=8, frameon=True, prop=pic_legend_font,
                     fancybox=False,
                     edgecolor='black', bbox_to_anchor=(0.5, -0.2), ncol=5, labelspacing=0.4, columnspacing=0.4,
                     handletextpad=0.1)
    leg.get_frame().set_linewidth(2)
    plt.show()
    # plt.savefig("priotity2", bbox_inches='tight', dpi=1000)


def rank():
    tips1 = pd.read_csv("../benchmarkdata/pr-rk-awd.csv")
    plt.figure(figsize=(8, 7))
    init_plt_years('Project', 'Actionable warning lifespan: day(s)', '')
    plt.grid(True)
    ax = sns.boxplot(
        x='Project',
        y="Actionable warning lifespan: day(s)",
        hue="Rank",
        hue_order=['Rank 1', 'Rank 5', 'Rank 7', 'Rank 8', 'Rank 9', 'Rank 10', 'Rank 11',
                   'Rank 12', 'Rank 13', 'Rank 14', 'Rank 15', 'Rank 16', 'Rank 17', 'Rank 18', 'Rank 19', 'Rank 20'],
        palette=sns.husl_palette(16, l=.5, s=.7),
        # sns.color_palette("hls", 16),
        linewidth=1.2,
        width=1.5,
        data=tips1)
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    plt.xticks(rotation=40)
    # plt.legend(loc='upper left', ncol=1, markerscale=1, labelspacing=0, handlelength=1)
    # plt.show()
    pic_legend_font = {'style': 'normal', 'weight': 'bold', 'size': 9}
    leg = plt.legend(loc=8, frameon=True, prop=pic_legend_font, fancybox=False,
                     edgecolor='black', bbox_to_anchor=(0.5, -0.3), ncol=5, labelspacing=0.4, columnspacing=0.4,
                     handletextpad=0.1)
    leg.get_frame().set_linewidth(2)
    plt.savefig("rank3", bbox_inches='tight', dpi=1000)


def change_width(ax, new_value):
    for patch in ax.patches:
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)


def rank_percentage():
    tips1 = pd.read_csv("../benchmarkdata/rk_percentage.csv")
    plt.figure(figsize=(12, 7))
    init_plt_years('Project', 'The density of actionable warnings', '')
    plt.grid(True)
    ax = sns.barplot(
        x='Project',
        y='The density of actionable warnings',
        hue="rank",
        hue_order=['Rank 1', 'Rank 5', 'Rank 7', 'Rank 8', 'Rank 9', 'Rank 10', 'Rank 11',
                   'Rank 12', 'Rank 13', 'Rank 14', 'Rank 15', 'Rank 16', 'Rank 17', 'Rank 18', 'Rank 19', 'Rank 20'],
        linewidth=1.2,
        errcolor=".2",
        edgecolor=".2",
        data=tips1)
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    plt.xticks(rotation=40)
    plt.legend(loc='upper right', ncol=1, markerscale=1, labelspacing=0, handlelength=1)
    change_width(ax, .1)
    plt.show()
    # plt.savefig("rank2", bbox_inches='tight', dpi=1000)


def rank_percentage1():
    tips1 = pd.read_csv("../benchmarkdata/rk_percentage.csv")
    plt.figure(figsize=(12, 7))
    init_plt_years('Project', 'The density of actionable warnings', '')
    plt.grid(True)
    ax = sns.swarmplot(
        x='Project',
        y='The density of actionable warnings',
        hue="rank",
        hue_order=['Rank 1', 'Rank 5', 'Rank 7', 'Rank 8', 'Rank 9', 'Rank 10', 'Rank 11',
                   'Rank 12', 'Rank 13', 'Rank 14', 'Rank 15', 'Rank 16', 'Rank 17', 'Rank 18', 'Rank 19', 'Rank 20'],
        linewidth=1.2,
        data=tips1)
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    plt.xticks(rotation=40)
    plt.legend(loc='upper right', ncol=1, markerscale=1, labelspacing=0, handlelength=1)
    plt.show()
    # plt.savefig("rank2", bbox_inches='tight', dpi=1000)


if __name__ == '__main__':
    priority()
    priority_percentage()
    # rank()
    # rank_percentage1()
