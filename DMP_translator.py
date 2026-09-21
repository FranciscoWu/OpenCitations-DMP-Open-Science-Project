import json
import html

#define input and output file

input_file = "OpenCitations_Data_Management_Plan.json"
output_file = "OCDM_DMP.html"


#read DMP json

file = open(input_file, "r", encoding="utf-8")
data = json.load(file)
file.close()


#HTML start structure

page = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>OpenCitations Data Management Plan</title>

<style>
body { font-family: Arial; max-width: 1100px; margin: 30px auto; line-height: 1.5; }
.box { border: 1px solid #cccccc; padding: 12px; margin: 10px 0; }
.key { font-weight: bold; }
.value { margin-left: 20px; white-space: pre-wrap; }
.level { margin-left: 20px; border-left: 2px solid #eeeeee; padding-left: 12px; }
</style>

</head>
<body>
<h1>OpenCitations Data Management Plan</h1>

"""

#translator function

def show_data(value):

    text = ""

    #if dictionary
    if isinstance(value, dict):

        text = text + "<div class='level'>"

        for key in value:

            text = text + "<div class='box'>"
            text = text + "<div class='key'>" + html.escape(str(key)) + "</div>"

            item = value[key]

            if isinstance(item, dict) or isinstance(item, list):
                text = text + show_data(item)

            else:
                text = text + "<div class='value'>"
                text = text + html.escape(str(item))
                text = text + "</div>"

            text = text + "</div>"

        text = text + "</div>"

    #if list
    elif isinstance(value, list):

        text = text + "<div class='level'>"

        number = 1

        for item in value:

            text = text + "<div class='box'>"
            text = text + "<div class='key'>Item " + str(number) + "</div>"

            if isinstance(item, dict) or isinstance(item, list):
                text = text + show_data(item)

            else:
                text = text + "<div class='value'>"
                text = text + html.escape(str(item))
                text = text + "</div>"

            text = text + "</div>"

            number = number + 1

        text = text + "</div>"

    #if value
    else:

        text = text + "<div class='value'>"
        text = text + html.escape(str(value))
        text = text + "</div>"

    return text


#to show all json contents

page = page + show_data(data)


#HTML end structure

page = page + """
</body>
</html>
"""


#save html file

file = open(output_file, "w", encoding="utf-8")
file.write(page)
file.close()

print("HTML created")
print(output_file)