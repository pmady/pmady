#!/usr/bin/env python3
"""Update GitHub stats in README.md"""

import re
from datetime import datetime

def main():
    with open('README.md', 'r') as f:
        readme = f.read()
    
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    
    stats_section = f"""## 📊 GitHub Stats

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=pmady&show_icons=true&include_all_commits=true&count_private=true&theme=github_dark&rank_icon=github)](https://github.com/pmady)

*Stats updated on {timestamp}*

"""
    
    # Replace the GitHub Stats section
    updated_readme = re.sub(
        r'## 📊 GitHub Stats.*?(?=\n## |\Z)',
        stats_section.rstrip(),
        readme,
        flags=re.DOTALL
    )
    
    with open('README.md', 'w') as f:
        f.write(updated_readme)
    
    print(f"✅ README updated successfully at {timestamp}")

if __name__ == '__main__':
    main()
