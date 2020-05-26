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
            for idx in range(0, len(x)):
                if x[idx].text is None:
                    x[idx].text = ""
                print("    " + x[idx].tag + ":  " + x[idx].text)

        def loop_comments(root):
            for idx in range(0, len(x)):
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

    def add_comment(file, VerbalStatus, Status, Date, Author, Comment):
        from xml.etree import ElementTree
        from uuid import uuid4
        def time_now():
            from datetime import datetime
            current_time = datetime.now().strftime("%y-%m-%dT%H:%M:%S+02:00")  # todo "02:00" hva er det for noe?
            print("Current Time =", current_time)
            return current_time

        def indent(elem, level=2):
            i = "\n" + level * "  "
            j = "\n" + (level - 1) * "  "
            if len(elem):
                if not elem.text or not elem.text.strip():
                    elem.text = i + "  "
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
                for subelem in elem:
                    indent(subelem, level + 1)
                if not elem.tail or not elem.tail.strip():
                    elem.tail = j
            else:
                if level and (not elem.tail or not elem.tail.strip()):
                    elem.tail = j
            return elem

        def sub_elem(element, tag, value):
            sub = ElementTree.SubElement(element, str(tag))
            sub.text = str(value)

        root = ElementTree.parse(file).getroot()
        c = ElementTree.Element("Comment")
        c.text = ""
        c.set("Guid", str(uuid4()))
        sub_elem(c, "VerbalStatus", VerbalStatus)
        sub_elem(c, "Status", time_now())
        sub_elem(c, "Date", Date)
        sub_elem(c, "Author", Author)
        sub_elem(c, "Comment", Comment)
        sub_elem(c, "ModifiedDate",
                 time_now())  # todo Lag en funksjon som endrer denne datoen hvis kommentaren er redigert

        for idx, x in enumerate(root):
            print(x.tag, " - ", idx)
            if x.tag == "Comment":
                i = idx + 1
        root.insert(i, c)
        indent(root, level=3)
        with open(file, 'w') as file:
            file.writelines(r'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + '\n')
            file.writelines(ElementTree.tostring(root, encoding='unicode'))

# todo  Lag en "edit comment" funksjon

# todo Lag en "remove comment" funksjon

# todo Lag en "add viewpoint" funksjon - Nytt bilde til issue

# todo Lag en "Export specific issues to bcfzip" funksjon

# todo Lag en "Delete Issue" funksjon - Kan være en metode som dytter saken til en dump folder som tømmes 1 gang i uken.
