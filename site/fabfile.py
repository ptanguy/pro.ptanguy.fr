from fabric.api import *
import fabric.contrib.project as project

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = '_build'
DEPLOY_PATH = env.deploy_path

# Github Pages configuration
env.github_pages_branch = "gh-pages"

def pub():
    """Publish to GitHub Pages"""
    local("ghp-import -b {github_pages_branch} {deploy_path}".format(**env))
