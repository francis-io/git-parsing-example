#!/usr/bin/env python3

from git import Repo
import os
import json
import subprocess
import datetime


class GitAnalyser:

    def __init__(self, repo_path):
        self.repo_path = repo_path

    def get_commits(self, days_to_get):
        #task: change hard coded dates to relative dates from now. e.g. 1 year from now, 1 day...
        #git rev-list --all --after="2020-12-10 00.00" --before="2021-03-10 23.59"

        # git supports relative dates: https://alexpeattie.com/blog/working-with-dates-in-git/#log-whatchanged-since-and-until
        rev_list_command = [
            'git',
            'rev-list',
            '--all',
            '--since={0} day ago'.format(days_to_get)
        ]

        rev_list_response = subprocess.Popen(
            rev_list_command,
            stdout=subprocess.PIPE,
            cwd=self.repo_path
            ).communicate()

        return rev_list_response


    def get_commits_using_git_lib(self, days_to_get):

        repo = Repo(self.repo_path)

        rev_list_response = repo.git.rev_list(
                                '--all',
                                '--since={0} day ago'.format(days_to_get)
                                )

        return rev_list_response

