import re
def main():
    text = """
    Alice's email is alice@example.com, and Bob's email is bob123@gmail.com.
    You can also contact support at support@company.com.
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.findall(email_pattern, text)
    print("Matched email addresses:")
    for match in matches:
        print(match)
    search_pattern = r'\bBob\b'
    search_result = re.search(search_pattern, text)
    if search_result:
        print("\nFound 'Bob' in the text.")
    else:
        print("\n'Bob' not found in the text.")
if __name__ == "__main__":
    main()
