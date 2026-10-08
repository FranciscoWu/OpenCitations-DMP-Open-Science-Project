# OpenCitations-DMP-Open-Science-Project
This project was developed for the Open Science course at the University of Bologna.

The main goal of the project is to create a **Data Management Plan (DMP)** for OpenCitations and to develop a **Python converter** that transforms the machine-readable **JSON** exported by Argos into a human-readable **HTML** document.

| Workflow                                                   |
| ---------------------------------------------------------- |
| 1. Study OpenCitations and related literature              |
| 2. Create the Data Management Plan in Argos                |
| 3. Create the 6 Descriptions                               |
| 4. Export the DMP as machine-readable JSON on Argos        |
| 5. Use Python to convert the JSON into human-readable HTML |
| 6. Generate and deploy the HTML through GitHub Pages       |

HTML Page
https://franciscowu.github.io/OpenCitations-DMP-Open-Science-Project/

# Translator.py

Its purpose is to convert any JSON files exported from Argos into a human-readable HTML document.

### Main logic

The converter has four main parts:

1. **`label()`**

The `label()` function converts machine-readable JSON field names into human-readable labels.



2.  **`show()`**

The `show()` function is responsible for converting JSON values into HTML.

It's workable with strings, lists, dictionaries, nested dictionaries and nested lists.



3. **`make_html()`**

The `make_html()` function creates the structure of the final webpage.



4. **`main()`**

The `main()` function reads the input JSON file, sends the DMP data to `make_html()`, and saves the generated HTML file.



# How to use?

```bash
python Translator.py OpenCitations_Data_Management_Plan.json
```

The program will generate the HTML



# Project Materials

### Argos PDF export

OpenCitations_Data_Management_Plan.pdf

### Argos JSON

OpenCitations_Data_Management_Plan.json

```text
JSON
└── dmp                                  dict
    │
    ├── contact                          dict
    │   ├── contact_id                   dict
    │   │   ├── identifier               str
    │   │   └── type                     str
    │   ├── mbox                         str
    │   └── name                         str
    │
    ├── contributor                      list
    │   └── contributor                  dict
    │       ├── contributor_id            dict
    │       │   ├── identifier            str
    │       │   └── type                  str
    │       ├── mbox                      str
    │       ├── name                      str
    │       └── role                      list
    │           └── role                  str
    │
    ├── cost                             list
    │   └── cost item                    dict
    │       └── description               str
    │
    ├── created                          str
    │
    ├── dataset                          list
    │   └── dataset item                 dict
    │       │
    │       ├── data_quality_assurance    list
    │       │   └── text                  str
    │       │
    │       ├── dataset_id                dict
    │       │   ├── identifier            str
    │       │   └── type                  str
    │       │
    │       ├── description               str
    │       │
    │       ├── distribution              list
    │       │   └── distribution item     dict
    │       │       │
    │       │       ├── format            list
    │       │       │   └── format        str
    │       │       │
    │       │       └── host              dict
    │       │           ├── title         str
    │       │           └── url           str
    │       │
    │       ├── keyword                   list
    │       │   └── keyword               str
    │       │
    │       ├── language                  str
    │       │
    │       ├── metadata                  list
    │       │   └── metadata item         dict
    │       │       └── description       str
    │       │
    │       ├── personal_data             str
    │       │
    │       ├── preservation_statement    str
    │       │
    │       ├── sensitive_data            str
    │       │
    │       ├── title                     str
    │       │
    │       └── type                      str
    │
    ├── description                      str
    │
    ├── dmp_id                           dict
    │   ├── identifier                    str
    │   └── type                          str
    │
    ├── ethical_issues_exist             str
    │
    ├── language                         str
    │
    ├── modified                         str
    │
    ├── project                          list
    │   └── project item                  dict
    │       ├── description               str
    │       │
    │       ├── funding                   list
    │       │   └── funding item          dict
    │       │       ├── funder_id         dict
    │       │       │   ├── identifier    str
    │       │       │   └── type          str
    │       │       │
    │       │       └── grant_id          dict
    │       │           ├── identifier    str
    │       │           └── type          str
    │       │
    │       └── title                     str
    │
    └── title                            str
```



## References

### Academic literature

1. Daquino, M., Peroni, S., Shotton, D., Colavizza, G., Ghavimi, B., Lauscher, A., Mayr, P., Romanello, M., & Zumstein, P. (2020). The OpenCitations Data Model. The Semantic Web – ISWC 2020, 12507, 447–463. https://doi.org/10.1007/978-3-030-62466-8_28 - OA at http://arxiv.org/abs/2005.11981
2. Heibi, I., Moretti, A., Peroni, S., & Soricetti, M. (2024). The OpenCitations Index: Description of a database providing open citation data. Scientometrics, 129(12), 7923–7942. https://doi.org/10.1007/s11192-024-05160-7
3. Massari, A., Mariani, F., Heibi, I., Peroni, S., & Shotton, D. (2024). OpenCitations Meta. Quantitative Science Studies, 5(1), 50–75. https://doi.org/10.1162/qss_a_00292
4. Peroni, S., & Shotton, D. (2020). OpenCitations, an infrastructure organization for open scholarship. Quantitative Science Studies, 1(1), 428–444. https://doi.org/10.1162/qss_a_00023
5. Persiani, S., Daquino, M., & Peroni, S. (2022). A Programming Interface for Creating Data According to the SPAR Ontologies and the OpenCitations Data Model. In P. Groth, M.-E. Vidal, F. Suchanek, P. Szekley, P. Kapanipathi, C. Pesquita, H. Skaf-Molli, & M. Tamper (Eds.), The Semantic Web (Vol. 13261, pp. 305–322). Springer. https://doi.org/10.1007/978-3-031-06981-9_18 - OA at https://2022.eswc-conferences.org/wp-content/uploads/2022/05/paper_69_Persiani_et_al.pdf
6. Peroni, S., & Rizzetto, E. (2025). A Tool for Validating and Monitoring Bibliographic Data in Open Research Information Systems: The OpenCitations Collections. In M. Cornia, G. M. D. Nunzio, D. Firmani, S. Mizzaro, G. Serra, S. Tonelli, & A. Tremamunno (Eds.), Proceedings of the 21st Conference on Information and Research science Connecting to Digital and Library science, Udine, Italy, February 20-21, 2025 (Vol. 3937). CEUR-WS.org. https://ceur-ws.org/Vol-3937/paper13.pdf





### OpenCitations resources

OpenCitations. (n.d.). *OpenCitations*. Official website. [OpenCitations official website](https://opencitations.net/)

OpenCitations. (n.d.). *Publications*. OpenCitations. This page provides the official publication list and documentation related to the OpenCitations infrastructure, datasets, and data model. [OpenCitations](https://opencitations.net/publications/?utm_source=chatgpt.com) [OpenCitations Publications](https://opencitations.net/publications/)

OpenCitations. (n.d.). *Metadata*. GitHub repository. This repository contains resources related to OpenCitations bibliographic metadata and data-model implementation. [OpenCitations metadata repository](https://github.com/opencitations/metadata)

OpenCitations. (n.d.). *OpenCitations data downloads*. Official data download service. [OpenCitations Downloads](https://download.opencitations.net)



### Data Management Plan and standards

OpenAIRE. (n.d.). *Argos: Plan and follow your data*. Argos Data Management Planning Service. Used in this project to create the Data Management Plan and export it in machine-actionable JSON format. [Argos DMP service](https://argos.openaire.eu/)



# AI Use Declaration

Artificial Intelligence (AI) tools were used during this project as supporting tools for reading, understanding, organizing, and reviewing academic and technical materials.

**AI tools were mainly used for:**

- supporting the understanding of technical concepts related to Open Science, OpenCitations, OCDM, RDF, provenance, DMPs, and the related software components.
- helping organize notes and documentation.
- supporting language revision and the improvement of English expressions.
- supporting the creation of some visual materials used in the slides.

- helping transform my HTML UI design drafts and layout ideas into CSS structures and styling rules.
- supporting deeper searches for some DMP-related questions when I could not find clear answers directly in the papers or official webpages; after AI helped identify possible sources, I checked the original sources myself and double-checked the information before using it in the project.

The author remains responsible for the final content, accuracy, interpretation, and structure of the project.
