from xml.etree import ElementTree


def indent(elem, level=1):
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


root = ElementTree.parse("real_sample.xml").getroot()


def comment_template(VerbalStatus, Status, Date, Author, Comment):
    from uuid import uuid4
    def time_now():
        from datetime import datetime
        current_time = datetime.now().strftime("%y-%m-%dT%H:%M:%S+02:00")  # todo "02:00" hva er det for noe?
        print("Current Time =", current_time)
        return current_time

    def sub_elem(element, tag, value):
        sub = ElementTree.SubElement(element, str(tag))
        sub.text = str(value)

    c = ElementTree.Element("Comment")
    c.text = ""
    c.set("Guid", str(uuid4()))
    sub_elem(c, "VerbalStatus", VerbalStatus)
    sub_elem(c, "Status", Status)
    sub_elem(c, "Date", Date)
    sub_elem(c, "Author", Author)
    sub_elem(c, "Comment", Comment)
    sub_elem(c, "ModifiedDate", time_now())

    for idx, x in enumerate(root):
        print(x.tag, " - ", idx)
        if x.tag == "Comment":
            i = idx + 1

    root.insert(i, c)


comment_template("Open", "Error", "2020-05-15T10:06:05+02:00", "henrik.nystrom@bundebygg.no", "Test Comment 001")

indent(root)
ElementTree.dump(root)

"""
<Comment Guid="f5a88273-8fb0-4cff-a0b5-6ef16ca2dce6">
<VerbalStatus>Open</VerbalStatus>
<Status>Error</Status>
<Date>2020-05-15T10:06:05+02:00</Date>
<Author>henrik.nystrom@bundebygg.no</Author>
<Comment></Comment>
<ModifiedDate>2020-05-15T10:06:05+02:00</ModifiedDate>
</Comment>
"""
