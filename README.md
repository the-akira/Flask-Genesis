# Flask-Genesis

A simple to use Static Site Generator made with **[Flask](https://flask.palletsprojects.com/en/1.1.x/)**, **[Flask-FlatPages](https://flask-flatpages.readthedocs.io/en/v0.7.1/)** and **[Frozen-Flask](https://pythonhosted.org/Frozen-Flask/)**.

## Features

- Markdown Support
- Syntax Highlighting
- Tables
- Tags
- Dates

You can see an example here: **https://flaskgenesis.netlify.com/**

## Installation

### Clone the Repository

```
git clone https://github.com/the-akira/Flask-Genesis.git
```

### Inside the Main Directory

Create a Virtual Environment

```
python -m venv myvenv
```

Activate the Virtual Environment

```
source myvenv/bin/activate
```

Install Requirements

```
pip install -r requirements.txt
```

Navigate to `blog` and Run the Application

```
python server.py
```

To generate the static site you can run the following command

```
python server.py build
```

You can then navigate to `build` and run `python -m http.server` to see the website. 

You are able to easily deploy to [GitHub Pages](https://pages.github.com/), [GitLab Pages](https://about.gitlab.com/product/pages/), [Netlify](https://www.netlify.com/), [Heroku](https://www.heroku.com), [Python Anywhere](https://www.pythonanywhere.com/)
