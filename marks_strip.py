#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-28 13:29:20
# @Author  : Yunyu2019 (yunyu2010@yeah.net)
# @Link    : ${link}
# @descp   : The document description
# ━━━━━━神兽出没━━━━━━
# 　　　┏┓　　　┏┓
# 　　┏┛┻━━━┛┻┓
# 　　┃　　　　　　　┃
# 　　┃　　　━　　　┃
# 　　┃　┳┛　┗┳　┃
# 　　┃　　　　　　　┃
# 　　┃　　　┻　　　┃
# 　　┃　　　　　　　┃
# 　　┗━┓　　　┏━┛Code is far away from bug with the animal protecting
# 　　　　┃　　　┃    神兽保佑,代码无bug
# 　　　　┃　　　┃
# 　　　　┃　　　┗━━━┓
# 　　　　┃　　　　　　　┣┓
# 　　　　┃　　　　　　　┏┛
# 　　　　┗┓┓┏━┳┓┏┛
# 　　　　　┃┫┫　┃┫┫
# 　　　　　┗┻┛　┗┻┛
#
# ━━━━━━感觉萌萌哒━━━━━━

import re
import codecs
import argparse

class stripMarks(object):
    """docstring for stripMarks"""
    def __init__(self, source,dist):
        super(stripMarks, self).__init__()
        self.source=source
        self.dist=dist
        self.rule=['add_date','icon','last_modified']

    def strip(self,rule=None,rel='',strs='',flags=None):
        rules=re.compile(rule,re.I)
        return re.sub(rules,rel,strs)

    def stripAttr(self,strs):
        rule='(?:{0})="[^\"]*"'.format('|'.join(self.rule))
        strs=self.strip(rule=rule,strs=strs,flags=re.I)
        strs=self.strip(rule='<h3\s{2,}([^<]*)>',strs=strs,flags=re.I,rel='<H3 \\1>')
        return strs

    def readMarks(self):
        with codecs.open(self.source,'r',encoding="utf-8") as fp:
            for line in fp:
                yield line
    def run(self):
        with codecs.open(self.dist,'w+',encoding="utf-8") as fp:
            for line in self.readMarks():
                strs=self.stripAttr(line)
                fp.write(strs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='strip attr in chrom marks')
    parser.add_argument('-i','--file',type=str,required=True,help='the chrom marks file path,extensions is .html')
    parser.add_argument('-o','--output',type=str,default='marks_dist.html',help='the dist chrom marks file path,extensions is .html')
    args=parser.parse_args()
    source=args.file
    dist=args.output
    marks=stripMarks(source,dist)
    marks.run()