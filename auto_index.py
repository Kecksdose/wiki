import os
import sys
from subprocess import call

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

def convert_topics_to_html(topics, html_folder='_html'):
    for topic in topics:
        # Apply same directory structure
        topic_folder_html = os.path.join(html_folder, topic)

        if not os.path.exists(topic_folder_html):
            os.mkdir(topic_folder_html)
        os.system(
            f'pandoc {topic}/README.md > {topic_folder_html}/index.html'
        )

if __name__ == '__main__':
    topics = get_topics()

    content = {
        'topics': topics
    }

    # Render index page
    rendered = render_template(content)
    with open('README.md', 'w') as file:
        file.write(rendered)

    # Topics to html
    convert_topics_to_html(topics)

    # Index to html
    os.system(
        'pandoc README.md > index.html'
    )
