import os

from github import Github


g = Github(os.environ.get('ACCESS_TOKEN'))

# useful resource https://developer.github.com/v3/repos/commits/
# get last commit info
for repo in g.get_user('prontotools').get_repos('learntoday'):
    if repo.name == 'learntoday':
        commit = repo.get_commit(
            sha='master',
        )
        print(commit.author)
        print(commit.commit.message)
