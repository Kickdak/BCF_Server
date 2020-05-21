from xml.etree import ElementTree
def indent(elem, level=1):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem

root = ElementTree.parse("real_sample.xml").getroot()
c = ElementTree.Element("Comment")
c.text = "0"

root.insert(2, c)
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