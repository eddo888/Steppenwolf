#!/usr/bin/env python3

import os, re, sys

from github import Github

from Spanners.Squirrel import Squirrel

squirrel = Squirrel()

hostname='github.com'
tokenname='rescript'
token=squirrel.get('%s:%s'%(hostname, tokenname))

gh = Github(token)

dirname=os.path.basename(os.getcwd())
print(dirname)

for repo in gh.get_user().get_repos():
	if repo.name == dirname:
		print(repo)
			
		


	
