import numpy as np
import pandas as pd

from src.const.Const import summary_dir
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
                x_data.append(i / len(density_data))
                now_sum += density_data[i]
                y_data.append(now_sum / y_sum)
            x_data_lists[key] = x_data
            y_data_lists[key] = y_data
        # drawGraph
        self.drawGraph.drawMutilLineChart(x_data_lists, y_data_lists, x_label, y_label,
                                          '', summary_dir + "2pic/" + fileName + " percent nums")
        return

    def get_density_percent_pic_by_target(self, targets):
        for i in targets:
            filename = i + "_summary_datas"
            self.drawDensityPrecent(filename, '% of ' + i + ' containing actionable warnings',
                                    '% of actionable warning density')


if __name__ == '__main__':
    f = FromSummaryDrawPic()
    type = ['method', 'file']
    f.get_density_percent_pic_by_target(type)