__author__ = 'king'
#coding: utf-8
import os,json
def Read_json(root):
    try:
        Fp = open(root+os.sep+'entry.json','r')
        s = json.load(Fp)
        Fp.close()
        return s["title"]
    except:
        print "Read json error ",root
def Read_json_page(root):
    try:
        Fp = open(root+os.sep+'entry.json','r')
        s = json.load(Fp)
        Fp.close()
        return s["page_data"]
    except:
        print "Read json page error ",root
def Soup(name):
    name = name.replace('?','')
    name = name.replace('*','')
    name = name.replace('\"','')
    name = name.replace('<','')
    name = name.replace('>','')
    name = name.replace(';','')
    name = name.replace('/','')
    name = name.replace('|','')
    return  name
def Find_cache(rootd,sourced):
    BUG = 0
    for root,dirs,files in os.walk(rootd):
        for file in files:
            if (os.path.splitext(root+os.sep+file)[1]==".mp4"):
                if os.path.isfile(root+os.sep+"entry.json"):
                    try:
                        z = Read_json(root+os.sep)
                        zz =Read_json_page(root+os.sep)
                        z = Soup(z)
                        zz["part"] = Soup(zz["part"])
                    except:
                        print "GET name error"
                    srd = root+os.sep+file
                    if (z==zz["part"]):
                        drd = sourced+os.sep+z+".mp4"
                    else:
                        drd = sourced+os.sep+z+zz["part"]+'.mp4'
                    try :
                        if os.path.isfile(drd.replace("\\","/")):
    #                        print os.path.splitext(drd.replace("\\","/"))[0]
                            try:
                                open(drd.replace("\\ ","/"), "wb").write(open(srd.replace("\\","/"), "rb").read())
                            except:
                                print "error 1",drd.replace("\\ ","/")
                        else:
                            try:
                                open(drd.replace("\\","/"), "wb").write(open(srd.replace("\\","/"), "rb").read())
                            except:
                                print 'error',drd.replace("\\","/")
                    except:
                         BUG = BUG + 1
                         print drd.replace("\\","/") ,'is error the num is' ,BUG
                else:
                    print file+"Json file LOST!"
def GET_input():
    print "Input RootDir"
    rootdir = raw_input()
#    rootdir = "C:\download"
    print "Input Sourcedir"
#    sourcedir = "D:\\test"
    sourcedir = raw_input()
    Find_cache(rootdir,sourcedir)
if __name__ == "__main__" :
    GET_input()