from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Github Pages configuration
env.github_pages_branch = "gh-pages"

# Port for `serve`
PORT = 8000

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def gh_pages():
    """Publish to GitHub Pages"""
    local("ghp-import -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))
