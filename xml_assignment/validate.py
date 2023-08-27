from lxml import etree
# Load XML
xml = etree.parse("products.xml")
# Load XSD schema
xsd = etree.parse("product_schema.xsd")
xsd_schema = etree.XMLSchema(xsd)
# Validate XML against XSD
validity = xsd_schema.validate(xml)
if validity:
    print("XML is valid according to the XSD.")
else:
    print("XML is not valid according to the XSD.")
    for error in xsd_schema.error_log:
        print("Error:", error.message)
        if "is not a valid value" in error.message:
            print("Element structure is not valid:", error.message)
            print("Refer XSD and check whether the element definition corresponds to the element in XML")
        elif "is required but missing" in error.message:
            print("Required element is missing:", error.message)
            print("Check if all the elements with required constraint are present")
        elif "This element is not expected" in error.message:
            print("Invalid attribute:", error.message)
            print("Check if the attribute matches the allowed attributes defined in the XSD.")