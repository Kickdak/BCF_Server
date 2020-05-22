from classes.BCF import *


def main():
    # Initialize class
    bb = BCF_V2(r"BCF\Issues", r"BCF\BCF Files")
    print(bb.get_amount_off_issues())
    #for path in bb.get_all_bcfzip_paths():
    #    bb.unzip_bcf(path)

    idx = 1
    for path in bb.get_all_issue_markup_paths():
        print("------------- issue nr: ", idx, " -------------")
        bb.read_markup_xml(path)
        idx += 1
    #add_comment("real_sample.xml","Open", "Error", "henrik.nystrom@bundebygg.no", "Test Comment 001")

if __name__ == '__main__':
    main()
