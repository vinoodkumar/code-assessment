#!/usr/bin/python
import requests
from datetime import datetime, timedelta

def get_pull_requests_summary(owner, repo):
    # GitHub API URL
    base_url = "https://api.github.com"
    endpoint = f"/repos/{owner}/{repo}/pulls"

    # Retrieve pull requests
    response = requests.get(base_url + endpoint)
    pull_requests = response.json()

    # Calculate date range (last week)
    last_week = datetime.now() - timedelta(days=7)

    # Filter pull requests by date
    opened = []
    closed = []
    draft = []

    for pr in pull_requests:
        pr_date = datetime.strptime(pr['created_at'], "%Y-%m-%dT%H:%M:%SZ")

        if pr_date >= last_week:
            if pr['state'] == 'open':
                opened.append(pr)
            elif pr['state'] == 'closed':
                closed.append(pr)
            elif pr['state'] == 'draft':
                draft.append(pr)

    # Generate email content
    email_from = "your_email@example.com"
    email_to = "recipient@example.com"
    email_subject = f"Pull Request Summary for {owner}/{repo} - Last Week"

    email_body = f"Summary of Pull Requests for {owner}/{repo} in the last week:\n\n"
    email_body += f"Opened Pull Requests ({len(opened)}):\n"
    for pr in opened:
        email_body += f"- #{pr['number']}: {pr['title']}\n"
        email_body += f"Title: {pr['title']}\n"
        email_body += f"Number: #{pr['number']}\n"
        email_body += f"State: {pr['state']}\n"
        email_body += f"URL: {pr['html_url']}\n"
        email_body += f"Created At: {pr['created_at']}\n"
        email_body += f"Closed At: {pr['closed_at']}\n"
        email_body += "--------------------------------------\n"

    email_body += f"\nClosed Pull Requests ({len(closed)}):\n"
    for pr in closed:
        email_body += f"- #{pr['number']}: {pr['title']}\n"
        email_body += f"Title: {pr['title']}\n"
        email_body += f"Number: #{pr['number']}\n"
        email_body += f"State: {pr['state']}\n"
        email_body += f"URL: {pr['html_url']}\n"
        email_body += f"Created At: {pr['created_at']}\n"
        email_body += f"Closed At: {pr['closed_at']}\n"
        email_body += "--------------------------------------\n"

    email_body += f"\nDraft Pull Requests ({len(draft)}):\n"
    for pr in draft:
        email_body += f"- #{pr['number']}: {pr['title']}\n"
        email_body += f"Title: {pr['title']}\n"
        email_body += f"Number: #{pr['number']}\n"
        email_body += f"State: {pr['state']}\n"
        email_body += f"URL: {pr['html_url']}\n"
        email_body += f"Created At: {pr['created_at']}\n"
        email_body += f"Closed At: {pr['closed_at']}\n"
        email_body += "--------------------------------------\n"

    return email_from, email_to, email_subject, email_body 


# Example usage
owner = "vinoodkumar"
repo = "DevOps-CICD"
email_from, email_to, email_subject, email_body = get_pull_requests_summary(owner, repo)

print("From:", email_from)
print("To:", email_to)
print("Subject:", email_subject)
print("Body:", email_body)
