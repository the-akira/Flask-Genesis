# Flask Genesis

![img](https://raw.githubusercontent.com/the-akira/Flask-Genesis/master/Avatar.png)

A simple to use Static Site Generator made with **[Flask](https://flask.palletsprojects.com/en/1.1.x/)**, **[Flask-FlatPages](https://flask-flatpages.readthedocs.io/en/v0.7.1/)** and **[Frozen-Flask](https://pythonhosted.org/Frozen-Flask/)**.

## Features

- Markdown Support
- Syntax Highlighting
- Tables
- Tags
- Dates

You can see an working example here: **[flaskgenesis.netlify.app](https://flaskgenesis.netlify.app)**

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

You can then navigate to `build` and run `python -m http.server` to see the website on your local machine. 

You are able to easily deploy to [GitHub Pages](https://pages.github.com/), [GitLab Pages](https://about.gitlab.com/product/pages/), [Netlify](https://www.netlify.com/), [Python Anywhere](https://www.pythonanywhere.com/) or [Surge](https://surge.sh/).