import os
from pathlib import Path

REPO = Path(__file__).parent
AGENTS_DIR = REPO / 'agents'

if __name__ == '__main__':
    print('Agents found:')
    for agent in sorted(AGENTS_DIR.iterdir()):
        if agent.is_dir():
            print('-', agent.name)
            for f in agent.iterdir():
                print('   ', f.name)
    print('\nRunner template: implement task handlers here.')
