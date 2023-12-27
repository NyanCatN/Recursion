import markdown

def html_converter(input, output):
    with open(input, "r") as f:
        contents = f.read()

    html = markdown.markdown(contents)

    with open(output, "w") as f:
        f.write(html)

input = "test.txt"
output = "output.html"

html_converter(input, output)
