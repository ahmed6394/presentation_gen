
def parse_repo_url(helper, url: str) -> str:
    """
        Parse GitHub URL and extract owner/repo path
        
        Accepts formats:
        - https://github.com/user/repo
        - https://github.com/user/repo/
        - github.com/user/repo
        - user/repo
        """
    url = url.strip()
        
    # Remove https:// and trailing slashes
    if url.startswith('https://'):
        url = url[8:]
    
    # Remove github.com prefix if present
    if url.startswith('github.com/'):
        url = url[11:]
    
    # Remove trailing slashes
    url = url.rstrip('/')
    
    # Check if we have user/repo format
    parts = url.split('/')
    if len(parts) >= 2:
        # print(f"debug: {parts[0]}/{parts[1]}")
        return f"{parts[0]}/{parts[1]}"
    
    return None