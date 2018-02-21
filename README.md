# ToDo
- Deployment
- GoogleAnalytics code
- Favicons




# Preparation

### REFERENCES ###
[original template](https://github.com/meshlogic/meshlogic.github.io)
[customizations](http://louistiao.me/posts/how-i-customized-my-nikola-powered-site/#deployment)


### ENV SET-UP ###
Ensure correct directory structure for smoothly pulling notebooks from the working directory to the blog posts.

rprt_Ipynb
	|__Current (working directory for notebooks)
	|__blog
		|__Pipfile (pipenv)
		|__IMTorgDemo.github.io (branch:src)
			|__posts
			|__pages

Pages - referenced by menu bar
Posts - track with tags <tools: node, spark, r, pandas> and categories <processes: data preparation, manipulation, presentation>




# DEVELOPMENT

### PIPENV ###
pipenv shell
pipenv install nikola

### INSTALL & REMOVE PLUGINS ###
nikola plugin -i sidebar
nikola plugin -r sidebar




# OPERATIONS

### PIPENV ###
pipenv shell
pipenv install nikola

### NEW POSTS: BASIC ###
nikola new_post


### NEW POSTS: IPYNB ###
- within _Introduction_ markdown cell, place: `<!-- TEASER_END -->`
- nikola new_post --format=ipynb --import=./prebuild/tests/Display\ System.ipynb --title=Display\ System --tags=test_tag-1,test_tag-2 posts/test_category/
- add 'test_category' to post-metadata: category


### NEW PAGES ###
nikola new_page


### CLEAN OUTPUT ###
nikola orphans
nikola clean
nikola check -f --clean-files


### BUILD ###
nikola build


### RUN LOCALLY ###
nikola serve -a 127.0.0.1 -b




# DEPLOYMENT

### DEPPLOY - INIT GITHUB ACCESS ###
$ git config --global user.name "imtorg"
$ git config --global user.email "information@mgmt-tech.org"
$ git init
$ git remote add origin https://github.com/imtorg/imtorgdemo.github.io.git
$ git pull origin master --allow-unrelated-histories


### DEPPLOY ###
nikola github_deploy






