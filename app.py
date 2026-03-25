from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from payloads import XSS_PAYLOAD, SQLI_PAYLOAD  # imported from payloads.py

app = Flask(__name__)

# ------------------------ Scanner Logic ------------------------

def get_forms(url):
    try:
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        return soup.find_all("form")
    except Exception:
        return []

def get_form_details(form):
    action = form.attrs.get("action", "").strip()
    method = form.attrs.get("method", "get").lower()
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})

    return {"action": action, "method": method, "inputs": inputs}

def submit_form(form_details, url, payload):
    target_url = urljoin(url, form_details['action'])
    inputs = form_details['inputs']
    data = {}

    for input_field in inputs:
        if input_field['type'] != "submit":
            name = input_field['name']
            if name:
                data[name] = payload

    try:
        if form_details['method'] == 'post':
            response = requests.post(target_url, data=data)
        else:
            response = requests.get(target_url, params=data)
        return response
    except:
        return None

def analyze_response(response, payload):
    if response and payload in response.text:
        return "Potential XSS Detected" if "<script>" in payload else "Potential SQL Injection Detected"
    elif response and ("sql" in response.text.lower() or "error" in response.text.lower()):
        return "Potential SQL Injection Detected"
    return "No obvious vulnerabilities"

# ------------------------ Flask Routes ------------------------

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target_url = request.form.get('url')
        forms = get_forms(target_url)
        results = []

        for i, form in enumerate(forms, start=1):
            details = get_form_details(form)
            xss_response = submit_form(details, target_url, XSS_PAYLOAD)
            sqli_response = submit_form(details, target_url, SQLI_PAYLOAD)

            results.append({
                "form_id": i,
                "action": details['action'],
                "method": details['method'],
                "inputs": details['inputs'],
                "xss_result": analyze_response(xss_response, XSS_PAYLOAD),
                "sqli_result": analyze_response(sqli_response, SQLI_PAYLOAD)
            })

        return render_template('results.html', url=target_url, results=results)

    return render_template('index.html')

# ------------------------ Run Server ------------------------

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
