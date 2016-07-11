import os, time
from time import sleep
from glob import glob
from markdown import markdown

post_template_url = "../templates/html/post.html"
blog_template_url = "../templates/html/blog.html"

posts_html_url = "../posts/html"
posts_markdown_url = "../posts/markdown"

def markdown_to_html(markdown_file_url, post_directory_url):
	""" Convert a markdown file to html.
	"""

	print "Converting markdown file: " + os.path.basename(markdown_file_url) + " to html..."
	markdown_file = open(markdown_file_url)
	markdown_text = markdown_file.read()
	markdown_file.close()

	html = markdown(markdown_text)

	new_post_url = posts_html_url + "/" + os.path.basename(markdown_file_url).replace(".md", ".html")

	with open(post_template_url) as post_template_html_file:
		new_post_html = post_template_html_file.read()

	new_post_html = new_post_html.replace("postname", os.path.basename(markdown_file_url))
	new_post_html = new_post_html.replace("postbody", html)

	new_post_html_file = open(new_post_url, 'w')
	new_post_html_file.write(new_post_html)
	new_post_html_file.close()

def generate_blog(post_directory_url):
	""" Generate an blog page from a directory of html files.
	"""

	print "Generating blog page..."

	blog_url = post_directory_url + "/blog.html"

	with open(blog_template_url) as blog_template_file:
		new_blog_html = blog_template_file.read()

	post_urls = glob(posts_html_url + "/*.html")

	blog_html_body = ""

	for post_url in post_urls:
		if "blog.html" not in post_url:
			blog_html_body += "<a href = \"" + post_url.replace("/posts", "") + "\">" + os.path.basename(post_url).replace(".html", "") + "</a><br>\n"

	new_blog_html = new_blog_html.replace("blogbody", blog_html_body)
	
	new_blog_file = open(blog_url, 'w')
	new_blog_file.write(new_blog_html)
	new_blog_file.close()

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
				generate_blog(posts_html_url)

			sleep(5)


def update_all():
	""" Convert all markdown files to html, generate blog file.
	"""

	print "Updating all posts..."
	post_urls = glob(posts_markdown_url + "/*.md")

	for post_url in post_urls:
		markdown_to_html(post_url, posts_html_url)

	generate_blog(posts_html_url)

update_all()
update_loop()