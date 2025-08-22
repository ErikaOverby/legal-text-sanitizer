# Legal Text Sanitizer (Redaction) 

## Description  
The **Legal Text Sanitizer** is a Python-based tool designed to help sanitize sensitive data in legal documents via redaction. It utilizes regular expressions to replace personal and confidential information such as names, email addresses, phone numbers, dates, legal terms, and addresses with placeholders. This tool ensures privacy compliance by anonymizing sensitive information while maintaining the original structure of the document. It is ideal for legal professionals and others handling confidential documents.  

### Key Features:  
- **Name Redaction**: Identifies and replaces both individual and company names with the placeholder `[REDACTED_NAME]` or `[REDACTED_COMPANY]`.  
- **Email Redaction**: Replaces email addresses with the placeholder `[REDACTED_EMAIL]`.  
- **Phone Number Redaction**: Redacts phone numbers by replacing them with `[REDACTED_PHONE]`.  
- **Date Redaction**: Detects dates in various formats (e.g., "March 3, 2023" or "03/03/2023") and replaces them with `[REDACTED_DATE]`.  
- **Legal Term Redaction**: Identifies and redacts specific legal terms (e.g., "plaintiff", "defendant", "jurisdiction") by replacing them with `[REDACTED_LEGAL_TERM]`.  
- **Address Redaction**: Replaces street addresses with the placeholder `[REDACTED_ADDRESS]`.  

## Installation  
1. Clone the repository:  
`git clone https://github.com/YourUsername/legal-text-sanitizer.git`  
2. Navigate to the project directory:  
`cd legal-text-sanitizer`  
3. Ensure you have Python 3.x installed (this script works with Python 3.6+).  

## Usage  
To run the script and sanitize an example legal text:  
1. Open a terminal or command prompt.  
2. Run the Python script `text_sanitizer.py`:  
`python text_sanitizer.py`  

### Example Output  
#### Original Text:  

John Doe, a plaintiff, is filing a lawsuit. His email is johndoe@example.com and his phone number is 555-123-4567.  
Jane Smith, the defendant, can be reached at janesmith@example.com, phone 555-765-4321.  
The court date for the trial is set for March 3, 2023. The hearing will take place at 123 Court St, New York, NY 10001.  
Acme Law Firm, representing the defendant, can be reached at 555-111-2222.

#### Sanitized Text:  

[REDACTED_NAME], a [REDACTED_LEGAL_TERM], is filing a lawsuit. His email is [REDACTED_EMAIL] and his phone number is [REDACTED_PHONE].  
[REDACTED_NAME], the [REDACTED_LEGAL_TERM], can be reached at [REDACTED_EMAIL], phone [REDACTED_PHONE].  
The court date for the trial is set for [REDACTED_DATE]. The hearing will take place at [REDACTED_ADDRESS].  
[REDACTED_COMPANY], representing the defendant, can be reached at [REDACTED_PHONE].

## 📁 Examples

The `examples/` folder contains a sample input and the corresponding sanitized output. These demonstrate how the script redacts sensitive legal information.

### 📥 Input (`examples/input_sample.txt`)
John Doe, a plaintiff, is filing a lawsuit. His email is johndoe@example.com and his phone number is 555-123-4567.
Jane Smith, the defendant, can be reached at janesmith@example.com, phone 555-765-4321.
The court date for the trial is set for March 3, 2023. The hearing will take place at 123 Court St, New York, NY 10001.
Acme Law Firm, representing the defendant, can be reached at 555-111-2222.

### 📤 Output (`examples/output_sample.txt`)
[REDACTED_NAME], a [REDACTED_LEGAL_TERM], is filing a lawsuit. His email is [REDACTED_EMAIL] and his phone number is [REDACTED_PHONE].
[REDACTED_NAME], the [REDACTED_LEGAL_TERM], can be reached at [REDACTED_EMAIL], phone [REDACTED_PHONE].
The [REDACTED_LEGAL_TERM] date for the trial is set for [REDACTED_DATE]. The hearing will take place at [REDACTED_ADDRESS].
[REDACTED_COMPANY], representing the [REDACTED_LEGAL_TERM], can be reached at [REDACTED_PHONE].

## 📦 Requirements

- Python 3.6 or higher  
- No external libraries are required (uses Python’s built-in `re` module)  

> You can run this script using any standard Python 3 environment such as PyCharm, VS Code, or a terminal.

## License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  

## Contributing  
Contributions are welcome! Feel free to open issues or submit pull requests for improvements, bug fixes, or additional features.  

## Future Improvements  
 - Extend tool to cover HIPAA compliance by removing the 18 identifiers specified by the HIPAA Privacy Rule  
- Include a web interface or API for document sanitization.




