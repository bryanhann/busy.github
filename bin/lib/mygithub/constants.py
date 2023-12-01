#!/usr/bin/env python3

import os
from pathlib import Path

from github import Github
from github import Auth

TOKEN=os.environ['BRYAN_CRED_GITHUB_CLASSIC_TOKEN']

AUTH = Auth.Token(TOKEN)
GITHUB = Github(auth=AUTH)
USER = GITHUB.get_user()
