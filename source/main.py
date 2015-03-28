__author__ = 'king'
#coding: utf-8
import os,json
import win32file

def Read_json(root):
    Fp = open(root+os.sep+'entry.json','r')
    s = json.load(Fp)
#    print s["title"]
    return s["title"]

def Find_cache(rootd,sourced):
    for root,dirs,files in os.walk(rootd):
        for file in files:
            if (file=='lua.flv.bapi.2_remux.mp4'):
                z = Read_json(root+os.sep)
                print z
                srd = root+os.sep+file
                drd = sourced+os.sep+z+'.mp4'
                print srd
                print drd
#                print srd.replace('\\',"/")
                try :
                    win32file.CopyFile(srd.replace("\\","/"),drd.replace("\\ ","/"),1)
                except :
                    print 'error'
def GET_input():
    print 'input rootdir:'
    rootdir = raw_input()
    print 'input sourcedir'
    sourcedir = raw_input()
    Find_cache(rootdir,sourcedir)

if __name__ == "__main__" :
    GET_input()


