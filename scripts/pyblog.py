import os, time
from time import sleep
from glob import glob
from markdown import markdown

post_template_url = "../templates/post.html"
contents_template_url = "../templates/contents.html"

posts_html_url = "../html"
posts_markdown_url = "../markdown"

def markdown_to_html(markdown_file_url, post_directory_url):
    """ Convert a markdown file to html.
    """

    print "Converting markdown file: " + os.path.basename(markdown_file_url) + " to html..."

    with open(markdown_file_url) as markdown_file:
        markdown_test = markdown_file.read()

	html = markdown(markdown_text)

	new_post_url = posts_html_url + "/" + os.path.basename(markdown_file_url).replace(".md", ".html")

	with open(post_template_url) as post_template_html_file:
		new_post_html = post_template_html_file.read()

	new_post_html = new_post_html.replace("pyblog-title", os.path.basename(markdown_file_url))
	new_post_html = new_post_html.replace("pyblog-body", html)

	with open(new_post_url, 'w') as new_post_html_file:
		new_post_html_file.write(new_post_html)

def generate_contents(post_directory_url):
	""" Generate an blog page from a directory of html files.
	"""

	print "Generating blog page..."

	contents_url = post_directory_url + "/contents.html"

	with open(contents_template_url) as contents_template_file:
		new_contents_html = contents_template_file.read()

	post_urls = glob(posts_html_url + "/*.html")

	contents_html_body = ""

	for post_url in post_urls:
		if "contents.html" not in post_url:
			contents_html_body += "<a href = \"" + post_url.replace("/posts", "") + "\">" + os.path.basename(post_url).replace(".html", "") + "</a><br>\n"

	new_contents_html = new_contents_html.replace("pyblog-body", contents_html_body)

	with open(contents_url, 'w') as new_contents_file:
		new_contents_file.write(new_contents_html)

def update_loop():
	""" Check for file changes, reconvert to html.
	"""

	while True:
		markdown_file_urls = glob(posts_markdown_url + "/*.md")

		for markdown_file_url in markdown_file_urls:
			last_modified_time = os.stat(markdown_file_url).st_mtime

			if time.time() - last_modified_time < 5:
				print "Post: " + markdown_file_url + " updated, converting to html..."
				markdown_to_html(markdown_file_url, posts_html_url)
				generate_contents(posts_html_url)

			sleep(5)


def update_all():
	""" Convert all markdown files to html, generate blog file.
	"""

	print "Updating all posts..."
	post_urls = glob(posts_markdown_url + "/*.md")

	for post_url in post_urls:
		markdown_to_html(post_url, posts_html_url)

	generate_contents(posts_html_url)

update_all()
update_loop()
