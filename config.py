#!/usr/bin/env python3

# TODO some can be generated at container build time

srvname = 'kdlp.underground.software'
production = False

appname = 'orbit'
version = '0.1'
source = 'https://github.com/underground-software/orbit'

radius_port = '9098'

smtp_port = '1465'
smtp_port_ext = '465'

pop3_port = '1995'
pop3_port_ext = '995'

matrix_port = '8448'

# These paths are used by browser GET requests (the are not server abspaths)
logo_get = '/images/kdlp_logo.png'
style_get = '/style.css'

# HTML title: keeping it simple and static for now
title = "KDLP"

# this is also hard-coded in many files
orbit_root = '/orbit'

# read these documents from a filesystem path
doc_root = f'{orbit_root}/docs'
database = f'{orbit_root}/orbit.db'

email_dir = f'{orbit_root}/email'

# duration of authentication token validity period
minutes_each_session_token_is_valid = 180

title = 'Kernel Development Learning Pipeline'
nav_buttons = [
    ('/index.md', 'Home'),
    ('/course/index.md', 'Course'),
    ('/login', 'Login'),
    ('/register', 'Register'),
    ('/dashboard', 'Dashboard'),
    ('/who.md', 'Who'),
    ('/info.md', 'Info'),
    ('/cgit', 'Git')]

sql_verbose = False

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Pass config var name as argument", file=sys.stderr)
        sys.exit(1)
    else:
        print(locals()[sys.argv[1]])
