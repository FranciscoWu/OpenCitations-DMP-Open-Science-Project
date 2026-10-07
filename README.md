# OpenCitations-DMP-Open-Science-Project
Open Science course project. An OpenAIRE Argos Data Management Plan for OpenCitations



# JSON Structure

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

