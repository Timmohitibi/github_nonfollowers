# GitHub Non-Followers

A small Python script that lists the GitHub users you follow who are not following you back.

This repository contains a single script: `github_nonfollowers.py`. The script calls the GitHub REST API to fetch followers and following for a given username, and prints the list of users you follow who do not follow you back.

## Features

- Fetches all followers and following (handles paginated results).
- Prints users you follow who are not following you back.
- Minimal dependencies (requests).

## Requirements

- Python 3.7+
- requests

Install dependencies:

```bash
pip install requests
```

## Usage

By default the script uses the `username` variable set at the top of the file. Edit that variable, or modify the script to accept command-line arguments.

Simple usage:

1. Clone the repository (if you haven't already):

```bash
git clone https://github.com/Timmohitibi/github_nonfollowers.git
cd github_nonfollowers
```

2. Edit the `username` variable in `github_nonfollowers.py` to your GitHub username (or add code to read from args).

3. Run the script:

```bash
python github_nonfollowers.py
```

Example output:

```
People Timmohitibi follows who are not following back:
octocat
another-user
```

## Authentication and Rate Limits

The script uses unauthenticated requests by default, which are limited by GitHub's public API rate limits (60 requests per hour). If you have many followers/following or run the script frequently, you should authenticate to increase the rate limit.

To add authentication:

1. Create a personal access token (no scopes are required for public profile data).
2. Export it as an environment variable:

```bash
export GITHUB_TOKEN="your_token_here"
```

3. Update the script's requests to include the Authorization header. Example snippet:

```python
import os
import requests

TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

r = requests.get(f"{url}?page={page}&per_page=100", headers=HEADERS)
```

Using a token raises the rate limit to typically 5,000 requests per hour.

## Notes and Limitations

- The script currently only supports reading a single username from the hardcoded `username` variable. Consider adding CLI options (argparse) if you want to check different users without editing the file.
- The script only compares login names; it treats organization accounts like users in the same way.
- For very large accounts, the script will make multiple paginated requests. Using an authenticated token is recommended to avoid hitting rate limits.
- The script does not attempt to handle API errors or retries. Consider adding error handling and exponential backoff for production use.

## Suggested Improvements

- Add argparse to accept username and token from command line.
- Add caching to avoid repeated API calls.
- Add unit tests and CI workflow.
- Optionally output results in CSV/JSON.

## Contributing

Contributions are welcome. Feel free to open issues or pull requests to add features or fixes.

## License

This repository does not include a license file. If you want to change that, add a LICENSE file to specify terms (GPL, MIT, etc.).
