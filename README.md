#  Web Application Vulnerability Scanner

A lightweight web vulnerability scanner built using **Python** and **Flask** that detects basic web threats like **XSS (Cross-Site Scripting)** and **SQL Injection** via form-based payload testing.

---

##  About the Project

This tool scans user-specified URLs for form fields, injects crafted payloads, and analyzes server responses for signs of potential vulnerabilities.

It aims to simulate real-world input-based attacks in a controlled environment — ideal for cybersecurity learning, demos, or small-scale assessments.

---

##  Tech Stack

- **Languages:** Python, HTML
- **Frameworks:** Flask, Bootstrap (via CDN)
- **Libraries:** `requests`, `BeautifulSoup`, `colorama`
- **Tools:** VS Code, Flask Development Server

---

##  Features

-  **Crawls target page** and detects all form fields
-  **Injects test payloads** for XSS and SQLi
-  **Analyzes responses** for indicators of vulnerabilities
-  **Logs scan results** in `.txt` format
-  **Web interface** for simple interaction
-  Styled UI using Bootstrap and custom CSS

---

##  UI Preview

| Home Page Input | Scan Result Example |
|-----------------|---------------------|
| ![index](home_page.png) | ![result](result_page.png) |
