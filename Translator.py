import json
import html #html.escaped()
import sys
import re

def label(name):
  if name == "mbox":
    return ("Email")
  elif name == "ethical_issues_exist":
    return ("Ethical Issues")
  elif name == "keyword":
    return ("Keywords")
  elif name == "cost":
    return ("Costs and Resources")
  else:
    text = name.replace("_", " ").title()
    text = text.replace(" Id", " ID")
    text = text.replace("Dmp", "DMP")
    text = text.replace("Url", "URL")
    return (text)



def show(value):
  if value is None or value == "" or value == [] or value == {}:
    return ""

  if type(value) == list:
    text = ""
    for i in value:
      showed = show(i)
      if showed:
        text += "<div>" + showed + "</div>"
    return text



  if type(value) == dict:
    text = ""
    for k, v in value.items():
      showed = show(v)
      if showed:
        text += '<div class="detail">' + "<b>" + html.escape(label(k)) + "</b>" + showed + "</div>"

    return text


  text = str(value).strip()
  text = re.sub(r"<div>|</div>|<p>|</p>|<b>|</b>|<br>","\n",text)
  text = html.escape(text)
  text = re.sub(r"(https?://[^\s<]+)",r'<a href="\1" target="_blank">\1</a>',text)
  text = text.replace("\n", "<br>")
  return "<p>" + text + "</p>"


def make_html(dmp):
  title = dmp.get("title", "Data management plan")
  projects = dmp.get("project")
  datasets = dmp.get("dataset")
  contributors = dmp.get("contributor")
  costs = dmp.get("cost")
  contact = dmp.get("contact")

  #navigator
  nav = (
    '<a href="#overview">Overview</a>' 
    '<a href="#contributors">Contributors</a>' 
    '<a href="#costs">Costs and Resources</a>' 
    '<div class="nav-title">Descriptions</div>'
  )

  n = 1
  for item in datasets:
    name = item["title"]
    nav += '<a class="description-link" href="#item-' + str(n) + '">' + str(n) + "." + html.escape(str(name)) + '</a>'
    n += 1


  #overview section
  body = '<section class="chapter" id="overview">'
  body += "<h1>" + html.escape(title) + "</h1>"

  created = ""
  for i in dmp.get("created", ""):
    if i == "T":
      break
    created += i

  modified = ""
  for i in dmp.get("modified", ""):
    if i == "T":
      break
    modified += i

  info = {
        "Project": projects[0].get("title"),
        "Contact": contact.get("name"),
        "Email": contact.get("mbox"),
        "Created": created,
        "Updated": modified,
        "Language": dmp.get("language"),
  }

  body += '<div class="metadata">'
  for k,v in info.items():
    if v:
      body += "<div><b>" + html.escape(label(k)) + "</b>" + show(v) + "</div>"
  body += '</div>'

  body += "<h2>DMP Description</h2>"
  body += '<div class="lead">' + show(dmp.get("description","")) + "</div>"

  if dmp.get("dmp_id"):
    body += '<div class="field"><h3>DMP ID</h3>' + show(dmp.get("dmp_id")) + "</div>"
  
  if dmp.get("ethical_issues_exist"):
    body += '<div class="field"><h3>Ethical Issues</h3>' + show(dmp.get("ethical_issues_exist")) + "</div>"

  if projects[0].get("description"):
    body += '<div class="field"><h3>Project Description</h3>' + show(projects[0].get("description")) + "</div>"

  if projects[0].get("funding"):
    body += '<div class="field"><h3>Funding</h3>' + show(projects[0].get("funding")) + "</div>"

  body += '</section>'

  #contributors section
  if contributors:
    body += '<section id="contributors" class="chapter"><h2>Contributors</h2><div class="people">'


    unique_contributors = {}


    for person in contributors:
      contributor_id = person.get("contributor_id", {})
      identifier = contributor_id.get("identifier", person.get("name"))

      if identifier not in unique_contributors:
        unique_contributors[identifier] = {}

      for key, value in person.items():
        if key != "role":
          unique_contributors[identifier][key] = value

    for person in unique_contributors.values():
      body += '<div class="person">' + show(person) + "</div>"


    body += "</div></section>"

  #costs and resources section
  if costs:
    body += '<section id="costs" class="chapter"><h2>Costs and Resources</h2>'
    for item in costs:
      body += '<div class="resource">' + show(item) + "</div>"
    body += '</section>'

  #descriptions section
    if datasets:
        body += '<section class="chapter"><h2>Descriptions</h2></section>'
        n = 1

    for item in datasets:
      name = item["title"]

      body += '<section id="item-' + str(n) + '" class="chapter">'
      body += "<h3>" + html.escape(str(name)) + "</h3>"

      if item.get("description"):
        body += '<div class="field"><h3>Description</h3>' + show(item["description"]) + "</div>"

      for key, value in item.items():
        if key not in ["title", "description"] and value not in [None, "", [], {}]:
          content = show(value)
          body += '<div class="field"><h3>' + html.escape(label(key)) + "</h3>" + content + "</div>"
      body += "</section>"
      n = n + 1  

    css = """
        /*all page basic colors and other settings*/
        :root {
            --bg: #eef2f3;
            --paper: #ffffff;
            --text: #27343c;
            --muted: #6d7880;
            --line: #e2e7ea;
            --blue: #466b80;
            --soft: #f8fafb;
            --highlight: #fff4bf;
        }

        * {
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            margin: 0;
            background: var(--bg);
            color: var(--text);
            font: 16px/1.75 Arial, sans-serif;
        }

        a {
            color: var(--blue);
            overflow-wrap: anywhere;
        }

        /*navigation bar*/
        .sidebar {
            position: fixed;
            top: 0;
            left: 0;
            width: 270px;
            height: 100vh;
            padding: 28px 20px;
            overflow: auto;
            background: #f8fafb;
            border-right: 1px solid var(--line);
        }

        .sidebar strong {
            display: block;
            margin-bottom: 22px;
            font-size: 17px;
            line-height: 1.4;
        }

        .sidebar a {
            display: block;
            margin: 2px 0;
            padding: 8px 10px;
            border-radius: 6px;
            color: #586771;
            font-size: 14px;
            text-decoration: none;
        }

        .sidebar a:hover {
            background: #edf2f4;
            color: #294d5c;
        }

        .nav-title {
            margin: 16px 10px 5px;
            font-weight: bold;
            color: var(--text);
        }

        .sidebar .description-link {
            padding-left: 22px;
            font-size: 13px;
        }

        .sidebar a.active {
            padding-left: 7px;
            background: #e4eef2;
            border-left: 3px solid var(--blue);
            color: #244d5f;
            font-weight: bold;
        }

        /*content*/
        .content {
            margin-left: 270px;
            padding: 34px 40px 80px;
        }

        .chapter {
            max-width: 880px;
            margin: 0 auto 24px;
            padding: 42px 46px;
            background: var(--paper);
            border-bottom: 1px solid var(--line);
            scroll-margin-top: 20px;
        }

        h1, h2, h3 {
            line-height: 1.3;
        }

        h1 {
            margin: 0 0 26px;
            font-size: 38px;
        }

        h2 {
            margin: 0 0 24px;
            font-size: 28px;
        }

        h3 {
            margin: 0 0 10px;
            font-size: 18px;
        }

        p {
            margin: 0 0 14px;
        }

        .lead {
            color: #37464e;
        }

        /*Overview*/
        .metadata {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            margin: 22px 0 32px;
            border-top: 1px solid var(--line);
            border-bottom: 1px solid var(--line);
        }

        .metadata > div {
            padding: 12px;
        }

        .metadata > div > div {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 12px;
        }

        .metadata b,
        .detail b,
        .item > b {
            display: block;
            color: var(--muted);
            font-size: 11px;
            text-transform: uppercase;
        }

        /*Sections*/
        .summary {
            margin: 18px 0 28px;
            padding: 15px 18px;
            background: var(--soft);
            border-left: 2px solid #a8bac2;
        }

        .field {
            margin-top: 28px;
            padding-top: 24px;
            border-top: 1px solid var(--line);
        }

        .detail {
            margin: 9px 0;
            padding: 5px 0;
        }

        .detail p {
            margin: 3px 0;
        }

        /*Short values*/
        .items {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 10px;
            margin: 10px 0;
        }

        .item {
            min-width: 0;
            padding: 12px;
            background: #fafbfc;
            border: 1px solid var(--line);
            border-radius: 6px;
        }

        .item .detail {
            margin: 2px 0;
            padding: 0;
            border: 0;
            background: transparent;
        }

        /*Contributors*/
        .people {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 12px;
            margin: 16px 0 26px;
        }

        .person {
            padding: 14px 16px;
            background: #fafbfc;
            border: 1px solid var(--line);
            border-radius: 8px;
        }

        .person p {
            margin: 3px 0;
            color: #56636c;
        }


        .person .detail {
            margin: 4px 0;
            padding: 0;
            border: 0;
            background: transparent;
        }

        .person .detail > b {
            margin-bottom: 2px;
        }

        /*Costs and Resources*/
        .resource {
            padding: 18px 0;
            border-bottom: 1px solid var(--line);
        }

        /*Reading highliter*/
        .chapter p {
            border-radius: 4px;
            transition: background-color .12s ease, box-shadow .12s ease;
        }

        .chapter p:hover {
            background: var(--highlight);
            box-shadow: 0 0 0 4px var(--highlight);
        }

        /*Mobile*/
        @media (max-width: 800px) {
            .sidebar {
                position: static;
                width: auto;
                height: auto;
            }

            .content {
                margin: 0;
                padding: 20px;
            }

            .chapter {
                padding: 30px 24px;
            }

            .metadata,
            .people,
            .items {
                grid-template-columns: 1fr;
            }
        }
        """

    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        "<title>" + html.escape(title) + "</title><style>" + css + "</style></head>"
        '<body><aside class="sidebar"><strong>' + html.escape(title) + "</strong><nav>" + nav + "</nav></aside>"
        '<main class="content">' + body + "</main>" + "</body></html>"
    )


def main():
    if len(sys.argv) != 2:
        print("The parameters should be two:" \
        "1. python file name" \
        "2. json file name")
        return

    input_file = sys.argv[1]
    output_file = input_file.replace(".json", ".html")

    with open(input_file, encoding="utf-8") as f:
      data = json.load(f)

    page = make_html(data["dmp"])

    with open(output_file, "w",encoding="utf-8") as f:
      f.write(page)

    print("HTML has been generated")

if __name__ == "__main__":
    main()
  
    

