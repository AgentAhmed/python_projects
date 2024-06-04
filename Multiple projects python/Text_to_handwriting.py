import pywhatkit as pw 

txt = """A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern."""


try:
    pw.text_to_handwriting(txt, "demo1.png", [0, 0, 138])
    print("Handwriting image created successfully!")
except pw.core.exceptions.UnableToAccessApi as e:
    print("Error: Unable to access Pywhatkit API right now. Please try again later.")