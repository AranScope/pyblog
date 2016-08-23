import os
import time
import glob
import markdown

TEMPLATE_URL = "../web/templates"
POST_TEMPLATE_URL = "../web/templates/post.html"
CONTENTS_TEMPLATE_URL = "../web/templates/contents.html"

POSTS_HTML_URL = "../web"
POSTS_MARKDOWN_URL = "../markdown"

def markdown_to_html(markdown_file_url, post_directory_url):
    """ Convert a markdown file to html."""

    print("Converting markdown file: " + os.path.basename(markdown_file_url) + " to html...")

    with open(markdown_file_url) as markdown_file:
        markdown_text = markdown_file.read()

	html = markdown.markdown(markdown_text)

	new_post_url = post_directory_url + "/" + file_name(markdown_file_url) + ".html";

	with open(POST_TEMPLATE_URL) as post_template_html_file:
		new_post_html = post_template_html_file.read()

	new_post_html = new_post_html.replace("{{pyblog-title}}", file_name(markdown_file_url))
	new_post_html = new_post_html.replace("{{pyblog-body}}", html)

	with open(new_post_url, 'w') as new_post_html_file:
		new_post_html_file.write(new_post_html)

def html_link(url, contents):
	""" Return an 'a' html tag with href 'url' and contents 'contents'"""

	return "<a href =\"" + url + "\">" + contents + "</a>"; 

def file_name(path):
	""" Return a file name (excluding extension) from a file path"""

	return os.path.splitext(os.path.basename(path))[0];

def generate_contents(post_directory_url):
	""" Generate an blog page from a directory of html files."""

	print("Generating blog page...")

	contents_url = post_directory_url + "/contents.html"

	with open(CONTENTS_TEMPLATE_URL) as contents_template_file:
		new_contents_html = contents_template_file.read()

	post_urls = glob.glob(POSTS_HTML_URL + "/*.html")

	contents_html_body = ""

	for post_url in post_urls:
		if "contents.html" not in post_url:
			contents_html_body += html_link(post_url, file_name(post_url)) + "<br>";

	new_contents_html = new_contents_html.replace("{{pyblog-body}}", contents_html_body)

	with open(contents_url, 'w') as new_contents_file:
		new_contents_file.write(new_contents_html)

def update_loop():
	""" Check for file changes, reconvert to html. """

	while True:
		markdown_file_urls = glob.glob(POSTS_MARKDOWN_URL + "/*.md")
		template_file_urls = glob.glob(TEMPLATE_URL + "/*")

		for markdown_file_url in markdown_file_urls:
			last_modified_time = os.stat(markdown_file_url).st_mtime

			if time.time() - last_modified_time < 5:
				print("Post: " + markdown_file_url + " updated, converting to html...")
				markdown_to_html(markdown_file_url, POSTS_HTML_URL)
				generate_contents(POSTS_HTML_URL)

		for template_file_url in template_file_urls:
			last_modified_time = os.stat(template_file_url).st_mtime

			if time.time() - last_modified_time < 5:
				print("Template: " + template_file_url + " updated")
				update_all()

		time.sleep(5)


def update_all():
	""" Convert all markdown files to html, generate blog file."""

	print("Updating all posts...")
	post_urls = glob.glob(POSTS_MARKDOWN_URL + "/*.md")

	for post_url in post_urls:
		markdown_to_html(post_url, POSTS_HTML_URL)

	generate_contents(POSTS_HTML_URL)

update_all()
update_loop()
