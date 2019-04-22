from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='1204628226',charset='utf8')#连接数据库
cur=conn.cursor()
cur.execute('use wikipedia')
class SolutionFound(RuntimeError):#自定义错误信息
    def __init__(self,message):
        self.message=message

def getLinks(fromPageId):
    cur.execute("select toPageId from links where fromPageId=%s",(fromPageId))#根据fromPageId查找toPageId
    if cur.rowcount==0:#如果没有操作成功，则rowcount==0
        return None
    else:

        return [x[0] for x in cur.fetchall()]#遍历所有的结果，取toPageId
def constructDict(currentPageId):
    links=getLinks(currentPageId)
    if links:
        #print(links)
        return dict(zip(links,[{}]*len(links)))#先进行压缩，后生成字典，key=value
    return {}

def searchDepth(targetPageId,currentPageId,linkTree,depth):
    if depth==0:
        return linkTree
    if not linkTree:
        linkTree=constructDict(currentPageId)#获取一个toPageId，传给linkTree
        #print(linkTree)
        if not linkTree:
            return {}
    if targetPageId in linkTree.keys():
        print('TARGET '+str(targetPageId)+' FOUND!')
        raise SolutionFound('PAGE:'+str(currentPageId))
    for branchKey,branchValue in linkTree.items():#将toPageId ,一个一个打开，查看targetPageId是否在其中，如果在其中，逐级返回递归
        try:
           # print(branchKey)
            #print(branchValue)
            linkTree[branchKey]=searchDepth(targetPageId,branchKey,branchValue,depth-1)#故意出错，打印错误信息
        except SolutionFound as e:
            print(e.message)#打印PAGE错误信息
            raise SolutionFound('Page:'+str(currentPageId))#变为page错误信息，即生成下一条错误信息,递归时逐级返回
    return linkTree
try:
    searchDepth(985,1,{},4)#执行递归
    print('No solution found')#except执行后，这一句不会执行
except SolutionFound as e:
    print(e.message)#打印最后一次更改的信息
