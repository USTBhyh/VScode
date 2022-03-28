# -*- coding:utf-8 -*-

# here put the import lib
import requests
from bs4 import BeautifulSoup  
import csv
import matplotlib.pyplot as plt
import pandas as pd

# 设置显示中文
plt.rcParams['font.sans-serif'] = ['simhei'] # 指定默认字体
# plt.rcParams['font.sans-serif']=['Fangsong'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来显示负号 
plt.rcParams['figure.dpi'] = 100 # 每英寸点数 


def getKobeList(code):
	url = "http://www.stat-nba.com/player/stat_box/195_"+code+".html"
	response = requests.get(url)
	resKobe = response.text
	return resKobe

#获取kobe历史数据
def getRow(resKobe,code):
	soup = BeautifulSoup(resKobe,"html.parser") 
	table = soup.find_all(id='stat_box_avg')
	
	#表头
	header = []
	if code == "season":
		header = ["赛季","出场","首发","时间","投篮","命中","出手","三分","命中","出手","罚球","命中","出手","篮板","前场","后场","助攻","抢断","盖帽","失误","犯规","得分","胜","负"]
	if code == "playoff":
		header = ["赛季","出场","时间","投篮","命中","出手","三分","命中","出手","罚球","命中","出手","篮板","前场","后场","助攻","抢断","盖帽","失误","犯规","得分","胜","负"]
	if code == "allstar":
		header = ["赛季","首发","时间","投篮","命中","出手","三分","命中","出手","罚球","命中","出手","篮板","前场","后场","助攻","抢断","盖帽","失误","犯规","得分"]
	#数据
	rows = [];
	rows.append(header)
	
	for tr in table[0].find_all("tr",class_="sort"): 
		row = []
		for td in tr.find_all("td"):
			rank = td.get("rank")
			if rank != "LAL" and rank != None:
				row.append(td.get_text())
		rows.append(row)
	return rows
	
#写入csv文件,rows为数据，dir为写入文件路径
def writeCsv(rows,dir):
	with open(dir, 'w', encoding='utf-8-sig', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(rows)


#常规赛数据
resKobe = getKobeList("season")
rows = getRow(resKobe,"season")
#print(rows)
writeCsv(rows,"season.csv")
print("season.csv saved")

#季后赛数据
resKobe = getKobeList("playoff")
rows = getRow(resKobe,"playoff")
#print(rows)
writeCsv(rows,"playoff.csv")
print("playoff.csv saved")

#全明星数据
resKobe = getKobeList("allstar")
rows = getRow(resKobe,"allstar")
#print(rows)
writeCsv(rows,"star.csv")
print("star.csv saved")

# 篮板、助攻、得分
def show_score(game_name='season', item='篮板', plot_name='line'):
    # game_name: season, playoff, star
    # item: 篮板，助攻，得分
    # plot_name: line,bar
    file_name = game_name+'.csv'
    data = pd.read_csv(file_name)
    X= data['赛季'].values.tolist()
    X.reverse()
    if item=='all':
        Y1 = data['篮板'].values.tolist()
        Y2 = data['助攻'].values.tolist()
        Y3 = data['得分'].values.tolist()
        Y1.reverse()
        Y2.reverse()
        Y3.reverse()
    else:
        Y = data[item].values.tolist() 
        Y.reverse() 

    if plot_name=='line':
        if item=='all':
            plt.plot(X,Y1,c='r',linestyle="-.")
            plt.plot(X,Y2,c='g',linestyle="--")
            plt.plot(X,Y3,c='b',linestyle="-")
            legend=['篮板','助攻','得分']
        else:
            plt.plot(X,Y,c='g',linestyle="-")
            legend=[item]
    elif plot_name=='bar':
        #facecolor:表面的颜色;edgecolor:边框的颜色
        if item=='all':
            fig = plt.figure(figsize=(15,5))
            ax1 = plt.subplot(131)
            plt.bar(X,Y1,facecolor = '#9999ff',edgecolor = 'white')
            plt.legend(['篮板'])
            plt.title('Kobe职业生涯数据分析：'+game_name)
            plt.xticks(rotation=60)
            plt.ylabel('篮板')

            ax2 = plt.subplot(132)
            plt.bar(X,Y2,facecolor = '#999900',edgecolor = 'white')
            plt.legend(['助攻'])
            plt.title('Kobe职业生涯数据分析：'+game_name)
            plt.xticks(rotation=60)
            plt.ylabel('助攻')

            ax3 = plt.subplot(133)
            plt.bar(X,Y3,facecolor = '#9988ff',edgecolor = 'white')
            legend=['得分']
        else:
            plt.bar(X,Y,facecolor = '#9900ff',edgecolor = 'white')
            legend=[item] 
    else:
        return


    plt.legend(legend)
    plt.title('Kobe职业生涯数据分析：'+game_name)
    plt.xticks(rotation=60)
    plt.xlabel('赛季')
    if item!='all':
        plt.ylabel(item)
    else:
        plt.ylabel('得分')
    plt.savefig('work/Kobe职业生涯数据分析_{}_{}.png'.format(game_name,item))
    plt.show()
    

# 篮板、助攻、得分  
game_name = 'season' 
for game_name in ['season','playoff','star']:
    show_score(game_name=game_name, item='篮板', plot_name='bar')
    show_score(game_name=game_name, item='助攻', plot_name='bar')
    show_score(game_name=game_name, item='得分', plot_name='bar')
    show_score(game_name=game_name, item='篮板', plot_name='line')
    show_score(game_name=game_name, item='助攻', plot_name='line')
    show_score(game_name=game_name, item='得分', plot_name='line')
    show_score(game_name=game_name, item='all', plot_name='bar')
    show_score(game_name=game_name, item='all', plot_name='line')

