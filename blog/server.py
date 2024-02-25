from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
import sys, json, datetime

# Configs
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'tables']
FLATPAGES_EXTENSION_CONFIGS = {
    'codehilite': {
        'linenums': True
    }
}

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

# URL Routing
@app.route('/')
def index():
    serialized_posts = [
        {
            'title': page.meta['title'],
            'date': page.meta['date'].strftime('%Y-%m-%d'),
            'path': page.path
        }
        for page in pages
    ]
    serialized_posts = sorted(serialized_posts, key=lambda p: p['date'], reverse=True)
    return render_template('index.html', posts=json.dumps(serialized_posts), total_post=len(serialized_posts))

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page, pages=pages)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('vim'), 200, {'Content-Type': 'text/css'}

# Custom URL Generators
@freezer.register_generator
def generate_tag_urls():
    for page in pages:
        tags = page.meta.get('tags', [])
        for tag in tags:
            yield f'tag', {'tag': tag}

@freezer.register_generator
def generate_page_urls():
    for page in pages:
        yield f'page', {'path': page.path}

# Main Function
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)