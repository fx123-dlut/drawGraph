from src.const import Const
from src.const.Const import projList, fileMap, picProjList
from src.dao.AllFileConnector import AllFileConnector
from src.tools.FileTool import FileTool
from src.tools.MathTool import MathTool

ft = FileTool()
# allDatas = AllFileConnector()
mt = MathTool()


def get_init_datas():
    root_dir = Const.base_dir + "resource/final/"
    alldatas = {}
    for proj in Const.projList:
        files = root_dir + picProjList[Const.projList.index(proj)] + ".csv"
        data = ft.get_data_from_csv(files, "")
        alldatas[proj] = data
    return alldatas


def get_datas(based):
    allDatas = get_init_datas()
    headers = ['projName', 'Top1-' + based, 'no', 'density', 'max lifetime', 'ave lifetime', 'min lifetime',
               'median lifetime', 'all nums']
    res = []
    for projName in projList:
        datas = allDatas[projName]
        res += mt.get_nums_density_max_min_average_mid(projName, datas, fileMap.get(based + "_line"))
    ft.save_to_target_file("summary/summary_csv/" + based + "_summary_datas", headers, res)
    print(based + ".csv has finished ! ")


# 506表格
if __name__ == '__main__':
    needed = ['category', 'vtype', 'file', 'priority', 'rank', 'method']
    for i in needed:
        get_datas(i)
