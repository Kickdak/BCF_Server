import sys
import os
import xml.etree.ElementTree as ET
from pyunpack import Archive

bcffil = r'C:\Playground\BCF_Server\BCF_2.1_Server\test.bcf'
temploc= r'C:\temp'
Archive(bcffil).extractall(temploc)

saker = {}
for nr,issues in enumerate(os.listdir(temploc)):

    if os.path.isdir(temploc+'\\'+issues):
        saker[issues]={}
        #print (issues,'nr: '+str(nr+1))

        #with open(temploc+'\\'+issues+'\markup.bcf','r') as sak:
        #    print (sak.read())

        bcf_parse=ET.parse(temploc+'\\'+issues+'\markup.bcf')
        bcf_root=bcf_parse.getroot()


        # Loops for each tag
        def loop_topics(bcf_root):
            topic={}
            for idx in range(0, len(bcf)):
                if bcf[idx].text is None:
                    bcf[idx].text = ""
                topic[bcf[idx].tag]=bcf[idx].text
            return (topic)


        def loop_comments(bcf_root):
            comments={}
            for idx in range(0, len(bcf)):
                #print (idx)
                if bcf[idx].text is None:
                    bcf[idx].text = ""
                comments[bcf[idx].tag]=bcf[idx].text
            return comments


        def loop_viewpoints(bcf_root):
            vps={}
            for idx in range(0, 2):
                if bcf[idx].text is None:
                    bcf[idx].text = ""
                vps[bcf[idx].tag]=bcf[idx].text
            return vps
                #print("    " + bcf[idx].tag + ":  " + bcf[idx].text)

        idx_C=1
        idx_VP=1
        for bcf in bcf_root:
            if bcf.tag == "Topic":
                print("___ Topic ___")
                saker[issues]['Sak']=(loop_topics(bcf))

            elif bcf.tag == "Comment":
                #print("___ Comment: ", idx_C, " ___")
                saker[issues]['Comments']=loop_comments(bcf)
                idx_C += 1
            elif bcf.tag == "Viewpoints":
                #print("___ Viewpoint: ", idx_VP, " ___")
                saker[issues]['Viewpoints']=loop_viewpoints(bcf)
                idx_VP += 1
#print (saker)
for sak,val in saker.items():
    print (sak,' - ',val)

