import numpy as np
import pandas as pd

from src.const.Const import summary_dir, projList, picProjList, base_dir
from src.tools.FileTool import FileTool
from src.tools.MathTool import MathTool
from src.tools.drawGraph import DrawGraph


class FromSummaryDrawPic:
    def __init__(self):
        self.ft = FileTool()
        self.drawGraph = DrawGraph()
        self.mathTool = MathTool()

    def drawDensityPrecent(self, fileName, x_label, y_label):
        # get datas
        datas = self.ft.get_data_from_csv_df(fileName + ".csv", summary_dir + "summary_csv/")
        # calculate the density percent
        datas = datas.groupby('projName')
        x_data_lists = {}
        y_data_lists = {}
        for key, group in datas:
            # print(group)
            sorted_datas = group[group["density"] > 0].sort_values("no", ascending=False)
            x_data = []
            y_data = []
            density_data = sorted_datas['density'].tolist()
            y_sum = np.sum(density_data)
            now_sum = 0
            for i in range(len(density_data)):
                x_data.append((i + 1) / len(density_data))
                now_sum += density_data[i]
                y_data.append(now_sum / y_sum)
            x_data_lists[key] = x_data
            y_data_lists[key] = y_data
        # drawGraph
        self.drawGraph.drawMutilLineChart(x_data_lists, y_data_lists, x_label, y_label,
                                          '', summary_dir + "2pic/" + fileName + " percent nums")

    def get_spearman_datas(self, targets):
        for i in targets:
            datas = self.ft.get_data_from_csv_df(i + "_summary_datas.csv", summary_dir + "summary_csv/")
            datas = datas.groupby('projName')
            res = []
            for key, group in datas:
                group = group[group['no'] > 0]
                spearman = group[['no', 'all nums']].corr(method="spearman")
                res.append([key, spearman['no']['all nums'], group['no'].tolist(), group['all nums'].tolist()])
            self.ft.save_datas2target_path(['projName', 'spearman', 'no', 'all nums'], res,
                                           summary_dir + "summary_csv/" + i + "_spearman_datas")

    def get_spearman_datas_from_final(self, targets, types):
        for target in targets:
            for group_type in types:
                res = []
                spearman_res = []
                for i in range(len(projList)):
                    datas = self.ft.get_data_from_csv_df(picProjList[i] + ".csv", base_dir + "resource/final/")
                    datas[group_type] = datas[group_type].replace(-1, 0)
                    sum_datas = datas[datas['final_label'] == 'TP'].groupby(target)[group_type].sum()
                    nums_datas = datas[datas['final_label'] == 'TP'].groupby(target)[group_type].count()
                    value_list = sum_datas.values.tolist()
                    index_list = sum_datas.index.tolist()
                    nums_list = nums_datas.values.tolist()
                    spearDf = pd.DataFrame({
                        "nums": nums_list,
                        "sum": value_list
                    })
                    if spearDf.corr(method="spearman")['nums']['sum'] == 'nan':
                        spearDf.corr(method="spearman")['nums']['sum'] = 0
                    spearman_res.append([picProjList[i], spearDf.corr(method="spearman")['nums']['sum'], nums_list,
                                         value_list, np.sum(nums_list)])
                    for j in range(len(value_list)):
                        res.append([picProjList[i], index_list[j], value_list[j]])
                    # print(picProjList[i], "has finished !")
                self.ft.save_datas2target_path(['projName', 'type name', 'all nums', 'sum nums'], res,
                                               summary_dir + "summary_csv/" + target + "_" +
                                               group_type + "_datas")
                self.ft.save_datas2target_path(['projName', 'spearman value', 'all nums', "target sum",'sum nums'], spearman_res,
                                               summary_dir + "summary_csv/" + target + "_" +
                                               group_type + "_spearman_datas")

    def get_density_percent_pic_by_target(self, targets):
        for i in targets:
            filename = i + "_summary_datas"
            self.drawDensityPrecent(filename, '% of ' + i + ' containing actionable warnings',
                                    '% of actionable warning density')


if __name__ == '__main__':
    f = FromSummaryDrawPic()
    # f.get_density_percent_pic_by_target(type)
    # type = ['method', 'file']
    # f.get_spearman_datas(type)
    targets = ['Cyclomatic', 'CountLine']
    type = ['method', 'buggy path']
    f.get_spearman_datas_from_final(type, targets)
