#!/usr/bin/env python3

from git_analyser import GitAnalyser


repo = GitAnalyser("/repo")

# get commits from last 2 days
print(repo.get_commits(days_to_get=2))

print(repo.get_commits_using_git_lib(days_to_get=2))