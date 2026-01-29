from util import filter_emails

def main():
    try:
        # Read the number of emails
        line = input().strip()
        if not line:
            return
        n = int(line)
        
        # Collect emails
        emails = []
        for _ in range(n):
            emails.append(input().strip())
            
        # Get filtered results
        result = filter_emails(emails)
        
        # Output as a list as per sample format
        print(result)
        
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()