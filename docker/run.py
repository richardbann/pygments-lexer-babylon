import subprocess
import time

import click

from runutils import ensure_user, get_user_ids, runbash, getvar


USER_NAME, USER_ID, GROUP_NAME, GROUP_ID = get_user_ids('lexer-tester', 1000)


@click.group()
def run():
    ensure_user(USER_NAME, USER_ID, GROUP_NAME, GROUP_ID)
    PIP_COMMAND = getvar('PIP_COMMAND')
    subprocess.call([PIP_COMMAND, 'install', '/pygments-lexer-babylon'])


@run.command()
@click.argument('user', default=USER_NAME)
def shell(user):
    runbash(user)


@run.command()
def generate():
    PYTHON_COMMAND = getvar('PYTHON_COMMAND')
    print('generating...')
    t0 = time.time()
    subprocess.call([PYTHON_COMMAND, '/pygments-lexer-babylon/test/runner.py'])
    t1 = time.time()
    print('ellapsed time: %s' % (t1 - t0,))

if __name__ == '__main__':
    run()
