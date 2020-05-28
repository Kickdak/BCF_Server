import sys
import os
import xml.etree.ElementTree as ET
from pyunpack import Archive

bcffil = r'C:\Users\thomasm\BundeGruppen AS\BIM utvikling - General\99 - Scripting\Python\BCF_Server\test.bcf'
temploc= r'C:\temp'
Archive(bcffil).extractall(temploc)
for nr,issues in enumerate(os.listdir(temploc)):
    if os.path.isdir(temploc+'\\'+issues):
        print (issues,'nr: '+str(nr+1))

        #with open(temploc+'\\'+issues+'\markup.bcf','r') as sak:
        #    print (sak.read())

        bcf_parse=ET.parse(temploc+'\\'+issues+'\markup.bcf')
        bcf_root=bcf_parse.getroot()


        # Loops for each tag
        def loop_topics(bcf_root):
            for idx in range(0, len(bcf)):
                if bcf[idx].text is None:
                    bcf[idx].text = ""
                print("    " + bcf[idx].tag + ":  " + bcf[idx].text)


        def loop_comments(bcf_root):
            for idx in range(0, len(bcf)):
                #print (idx)
                if bcf[idx].text is None:
                    bcf[idx].text = ""
                print("    " + bcf[idx].tag + ":  " + bcf[idx].text)


        def loop_viewpoints(bcf_root):
            for idx in range(0, 2):
                if bcf[idx].text is None:
                    bcf[idx].text = ""
                print("    " + bcf[idx].tag + ":  " + bcf[idx].text)

        idx_C=1
        idx_VP=1
        for bcf in bcf_root:
            if bcf.tag == "Topic":
                print("___ Topic ___")
                loop_topics(bcf)
            elif bcf.tag == "Comment":
                print("___ Comment: ", idx_C, " ___")
                loop_comments(bcf)
                idx_C += 1
            elif bcf.tag == "Viewpoints":
                print("___ Viewpoint: ", idx_VP, " ___")
                loop_viewpoints(bcf)
                idx_VP += 1