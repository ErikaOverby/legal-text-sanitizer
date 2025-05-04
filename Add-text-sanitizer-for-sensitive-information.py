
import re


# Function to replace sensitive information in text
def sanitize_text(text):
    # Replace email addresses with placeholder
    sanitized_text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', '[REDACTED_EMAIL]', text)

    # Replace phone numbers with placeholder
    sanitized_text = re.sub(r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b', '[REDACTED_PHONE]', sanitized_text)

    # Replace names with placeholder (full names and company names)
    sanitized_text = re.sub(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b', '[REDACTED_NAME]', sanitized_text)
    sanitized_text = re.sub(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b', '[REDACTED_COMPANY]',
                            sanitized_text)  # For company names

    # Replace dates (in format: March 3, 2023 or 03/03/2023)
    sanitized_text = re.sub(r'\b(?:[A-Za-z]+ \d{1,2}, \d{4}|\d{1,2}/\d{1,2}/\d{4})\b', '[REDACTED_DATE]',
                            sanitized_text)

    # Replace legal terms (e.g., plaintiff, defendant, court terms)
    legal_terms = r'\b(plaintiff|defendant|jurisdiction|contract|agreement|court|party|witness|complaint)\b'
    sanitized_text = re.sub(legal_terms, '[REDACTED_LEGAL_TERM]', sanitized_text, flags=re.IGNORECASE)

    # Replace addresses (simple detection of street addresses)
    sanitized_text = re.sub(r'\d+\s[A-Za-z]+\s[A-Za-z]+(?:\s[A-Za-z]+)*,\s[A-Za-z]+\s[A-Za-z]+,\s[A-Za-z]+\s\d{5}',
                            '[REDACTED_ADDRESS]', sanitized_text)

    return sanitized_text


# Example usage
if __name__ == "__main__":
    # Sample legal text with sensitive information
    text = """
    John Doe, a plaintiff, is filing a lawsuit. His email is johndoe@example.com and his phone number is 555-123-4567.
    Jane Smith, the defendant, can be reached at janesmith@example.com, phone 555-765-4321.
    The court date for the trial is set for March 3, 2023. The hearing will take place at 123 Court St, New York, NY 10001.
    Acme Law Firm, representing the defendant, can be reached at 555-111-2222.
    """

    # Sanitizing the text
    sanitized = sanitize_text(text)

    print("Original Text:\n", text)
    print("Sanitized Text:\n", sanitized)
