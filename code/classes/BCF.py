class BCF_V2():  # This is a BCF 2.0 Class atm
    def __init__(self, path_to_issues, path_to_bcfzip_files):
        print("BCF class imported")
        self.path_to_issues = path_to_issues
        self.path_to_bcfzip_files = path_to_bcfzip_files

    def get_amount_off_issues(self):
        """
        Denne funksjonen returnerer antall totale issues som finnes
        """
        from os import walk
        idx = 0
        for subdir, dirs, files in walk(self.path_to_issues):
            nr = len(dirs)
            break
        return nr

    def get_all_bcfzip_paths(self):
        """
        Denne funksjonen returnerer en liste med filbaner til .bcfzip filer.
        """
        from os import walk, sep
        paths = []
        for subdir, dirs, files in walk(self.path_to_bcfzip_files):
            for filename in files:
                filepath = subdir + sep + filename
                if filepath.endswith(".bcfzip"):
                    paths.append(filepath)
        return paths

    def unzip_bcf(self, path_to_file):
        from zipfile import ZipFile
        with ZipFile(path_to_file, 'r') as zip_ref:
            zip_ref.extractall(self.path_to_issues)  # todo Loop to create issue folder

    def get_all_issue_markup_paths(self):
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

# todo Lag en "add comment" funksjon

# todo  Lag en "edit comment" funksjon

# todo Lag en "remove comment" funksjon

# todo Lag en "Add new picture to issue" funksjon

# todo Lag en "Export specific issues to bcfzip" funksjon

# todo Lag en "Delete Issue" funksjon - Kan være en metode som dytter saken til en dump folder som tømmes 1 gang i uken.