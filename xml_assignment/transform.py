from lxml import etree
# Load XML
xml = etree.parse("products.xml")
xsl = etree.parse("transform.xsl")
# Load XSL
xsl_transform = etree.XSLT(xsl)
# Apply XSLT transformation
html = xsl_transform(xml)
# Write transformed HTML to a file
with open("output.html", "wb") as output_file:
    output_file.write(etree.tostring(html, pretty_print=True))