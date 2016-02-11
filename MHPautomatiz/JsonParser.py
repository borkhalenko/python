#date: 10.02.16
#author: Borkhalenko Oleg
#email: borkhalenko@gmail.com

#importing base libraries
import json

##from enum import Enum
##
##class DictionaryType(Enum):
##    IsUOM = 1
##    IsGoodsCategory = 2
##    IsGoodsItem = 3
##jstring = '[{"_UOMId":1,"_UOMName":"oo"},{"_UOMId":2,"_UOMName":"aa"}]'

#ParseUomArr = 

def ParseUom(jstr):
    res = []
    jobj = json.loads(jstr)
    for item in jobj:
        res.append(str(item['_UOMId'])+","+str(item['_UOMName']+";"))
    return res

def ParseGoodsCategories(jstr):
    res = []
    jobj = json.loads(jstr)
    for item in jobj:
        res.append(str(item['_TopGoodsCategoryId'])+","
                   +str(item['_GoodsCategoryId'])+","
                   +str(item['_GoodsCategoryName'])+";")
    return res

def ParseGoodsItems(jstr):
    res = []
    jobj = json.loads(jstr)
    for item in jobj:
        IsClosed = 0;
        if (item['_IsClosed']==True):
            IsClosed = 1
        res.append(str(item['_GoodsItemId'])+","
                   +str(item['_GoodsItemName'])+","
                   +str(item['_Price'])+","
                   +str(item['__UOM']['_UOMId'])+","
                   +str(item['_GoodsCategory']['_GoodsCategoryId'])+","
                   +str(IsClosed)+","
                   +str(item['_Comment'])+","
                   +str(item['_AnalyticCode'])+";")
    return res    
