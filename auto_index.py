import os
import sys

from jinja2 import Environment, FileSystemLoader, StrictUndefined

def get_topics():
    """Get list of topics (i.e. folder names.)"""
    topics = [
        topic for topic in os.listdir()
        if os.path.isdir(topic) and
        not topic.startswith(('.', '_'))
    ]
    return topics

def render_template(content, path='_templates', file='index.template'):
    env = Environment(
        loader=FileSystemLoader(path),
        undefined=StrictUndefined
    )
    template = env.get_template(file)
    rendered = template.render(**content)
    return rendered

if __name__ == '__main__':
    content = {
        'topics': get_topics()
    }
    rendered = render_template(content)
    with open('index.md', 'w') as file:
        file.write(rendered)
