---
title: 'Web-Based Chemistry Article Parser for Easy Document Annotation'
date: 2022-05-11
permalink: /posts/2022/05/chem-parser/
toc: true
tags:
  - Doccano
  - Website
  - Parser
  - English
---

This article covers the instruction of [Chemistry Article Parsing Portal](http://sciannotate.cc.gatech.edu/) (currently only accessible through Georgia Tech network or VPN) for automatic Chemistry article parsing and uploading to [doccano](https://yinghao-li.github.io/posts/2022/02/doccano/) for document annotation.

{% include user_def %}

## 1. About the Portal

Chemistry Article Parsing Portal is a portal website for automatic Chemistry article parsing and uploading to the doccano annotation system.
It is designed to provide a more user-friendly GUI for non-technical users to upload and annotate articles without being frustrated by command lines.

The website is available at [http://sciannotate.cc.gatech.edu](http://sciannotate.cc.gatech.edu/).
Notice that the website is hosted with the same URL as [doccano](http://sciannotate.cc.gatech.edu:8000/) but at different ports (*80* for the portal and *8000* for doccano).

The code of the Portal website is not publicly available due to safety concerns, but you can find and contribute to the HTML article parsing source code [here](https://github.com/Yinghao-Li/ChemistryHTMLPaperParser).

## 2. Website Elements

### 2.1. Main Page

A screenshot of the website is shown below:

![portal index]({{base_path}}/images/web-portal/main-page.png)

It mainly consists of two parts: the input boxes and the "Upload" button.
The input boxes are for users to input their user credentials and the DOIs of the articles they want to parse and upload to doccano.
The "Upload" button is for users to click to start the parsing and uploading process.

The portal uses the same credentials as the doccano system.
If you do not have an account on doccano, you can create one following [the instructions]({{base_path}}/posts/2022/02/doccano/#1-3).
To upload the articles, you also need to specify your target doccano project.
Check [this section]({{base_path}}/posts/2022/02/doccano/#3) for more information about accessing your projects.

At last, you need to provide the DOIs of the articles you want to upload.
You can provide multiple DOIs at the same time, each separated by commas.
You can also write each DOI on a separate line, but the comma separator is still necessary.

{{ hint_info }}
If you find the input box too small, you can resize it by dragging the border.
{{ _hint }}

When you click the "Upload" button, the portal will start the parsing and uploading process.
There is no process bar, but you can check the status of the process by looking at your browser's tab's status.
If the tab shows "loading", the process is still running.
Otherwise, the process is finished, and the webpage will show whether the process is successful.
Each article will take approximately 10-20 seconds to process.
If there's an error, the portal will show the error message at the top of the page.

{{ hint_info }}
You can find more information on the web page.
{{ _hint }}

### 2.2. Success Upload

![success page]({{base_path}}/images/web-portal/success-page.png)

If the upload is successful, a success page as above will show.
The page lists the DOIs of the articles that are uploaded.
At the right of each DOI, you can find a "Preview and HTML" button.
You can preview the parsed articles as HTML pages to check if the parsing result is correct.
You can also download the HTML files for future use.

At the bottom of the page are a "Go to Doccano" button and a "Return" button.
The "Go to Doccano" button will take you to the doccano project page, while the "Return" button will return you to the portal's main page.

## 3. Annotation

Once the articles are uploaded, you can start annotating the articles with doccano.
You can find a tutorial on how to annotate the articles at [my website]({{base_path}}/posts/2022/02/doccano/), the [official website](https://doccano.github.io/doccano/) and the [GitHub repo](https://github.com/doccano/doccano).
