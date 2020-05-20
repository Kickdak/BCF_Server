class BCF_V2(): #This is a BCF 2.0 Class atm
    def __init__(self, path_to_issues):
        print("BCF class imported")
        self.path_to_issues = path_to_issues

    def unzip_bcf(self, path_to_file):
        from zipfile import ZipFile
        with ZipFile(path_to_file, 'r') as zip_ref:
            zip_ref.extractall(self.path_to_issues + r"\Issue04")  # todo Loop to create issue folder

    def get_all_issue_marup_paths(self):
        from os import walk, sep
        paths = []
        for subdir, dirs, files in walk(self.path_to_issues):
            for filename in files:
                filepath = subdir + sep + filename
                if filepath.endswith(".bcf"):
                    paths.append(filepath)
        return paths

    def read_markup_xml(self, path):
        # Import module for reading xml
        import xml.etree.ElementTree as ET
        # Parses the xml for makeing it readable
        tree = ET.parse(path)
        root = tree.getroot()

        # Loops for each tag
        def loop_topics(root):
            for idx in range(0, 8):
                if x[idx].text is None:
                    x[idx].text = ""
                print("    " + x[idx].tag + ":  " + x[idx].text)

        def loop_comments(root):
            for idx in range(0, 6):
                if x[idx].text is None:
                    x[idx].text = ""
                print("    " + x[idx].tag + ":  " + x[idx].text)

        def loop_viewpoints(root):
            for idx in range(0, 2):
                if x[idx].text is None:
                    x[idx].text = ""
                print("    " + x[idx].tag + ":  " + x[idx].text)

        # Variabels for xml data
        idx_comment = 1
        idx_viewpoint = 1
        # Loop for tags and values
        for x in root:
            if x.tag == "Topic":
                print("___ Topic ___")
                loop_topics(x)
            elif x.tag == "Comment":
                print("___ Comment: ", idx_comment, " ___")
                loop_comments(x)
                idx_comment += 1
            elif x.tag == "Viewpoints":
                print("___ Viewpoint: ", idx_viewpoint, " ___")
                loop_viewpoints(x)
                idx_viewpoint += 1
