# pyblog
A super simple markdown-html blog generator.

## Usage
### Installing and running pyblog
1. Make sure you have the google drive desktop sync software installed and running.
2. Navigate into a synched google drive folder and run 'git clone https://github.com/aranscope/pyblog.git'
3. Change directory into the pyblog/scripts directory
4. Run the pyblog.py script
5. The website will be generated in the pyblog/web directory

### Writing posts
1. Posts should be written in vanilla markdown and saved as '.md' files in the pyblog/markdown directory

### Modifying templates
#### Html
1. The 'post.html' and 'contents.html' templates are located in pyblog/web/templates
2. The stylesheets for these html templates are also located in pyblog/web/templates
3. You can modify these as much as you wish but be aware, the keywords 'pyblog-title' and 'pyblog-body' are used to inject html

### Using with github.io
1. Clone your 'username'.github.io repository
2. Copy all of the files in the pyblog/web/ directory into the root directory of your github.io repo
3. (Optional) Setup for eg. Cron to automatically complete this task and push to github
