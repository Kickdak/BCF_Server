from classes.BCF import *

def main():
    # Initialize class
    bb = BCF_V2(r"BCF",r"BCF\BCF Files" )
    print(bb.get_all_bcfzip_paths())
    # bb.unzip_bcf()


    #for idx, path in enumerate(bb.get_all_issue_marup_paths()):
    #    print("------------- issue nr: ", idx, " -------------")
    #    bb.read_markup_xml(path)


if __name__ == '__main__':
    main()
