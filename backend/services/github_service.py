import os
from github import Github
from github.GithubException import GithubException
from dotenv import load_dotenv
from helper import parse_repo_url


load_dotenv()

class GitHubService:
    def __init__(self):
        """Initialize GitHub service with optional token for higher rate limits"""
        token = os.getenv('GITHUB_TOKEN', None)
        self.github = Github(token) if token else Github()
    
    def extract_readme(self, repo_url: str) -> dict:
        """
        Extract README from a GitHub repo
        
        Args:
            repo_url
        
        Returns:
            dict with keys: 'success', 'content', 'error', 'repo_name'
        """
        try:
            # Parse repository URL
            repo_path = parse_repo_url(self, repo_url)
            if not repo_path:
                return {
                    'success': False,
                    'error': 'Invalid GitHub URL format. Use: https://github.com/username/repository',
                    'content': None,
                    'repo_name': None
                }
            
            # Get repository
            try:
                repo = self.github.get_repo(repo_path)
                # print(f"repo details: {repo}")
            except GithubException as e:
                return {
                    'success': False,
                    'error': f'Repository not found: {str(e)}',
                    'content': None,
                    'repo_name': None
                }
            
            # Try to get README in different formats
            readme_content = None
            readme_names = ['README.md', 'readme.md', 'README.MD', 'Readme.md']
            
            for readme_name in readme_names:
                try:
                    readme_file = repo.get_contents(readme_name)
                    readme_content = readme_file.decoded_content.decode('utf-8')
                    break
                except GithubException:
                    continue
            
            if not readme_content:
                return {
                    'success': False,
                    'error': 'README.md not found in this repository',
                    'content': None,
                    'repo_name': repo.name
                }
            
            return {
                'success': True,
                'content': readme_content,
                'error': None,
                'repo_name': repo.name,
                'repo_description': repo.description,
                'repo_url': repo.html_url
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f'An error occurred: {str(e)}',
                'content': None,
                'repo_name': None
            }
    
    


# for Test only 
if __name__ == "__main__":
    service = GitHubService()
    
    # Test with a open repository
    test_url = "https://github.com/pallets/flask"
    print(f"Testing with: {test_url}")
    
    result = service.extract_readme(test_url)
    print(f"Success: {result['success']}")
    print(f"Repo Name: {result['repo_name']}")
    
    if result['success']:
        content_preview = result['content'][:200] + "..." if len(result['content']) > 200 else result['content']
        print(f"Content Preview: {content_preview}")
    else:
        print(f"Error: {result['error']}")