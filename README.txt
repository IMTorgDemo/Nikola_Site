# ToDo
- Deployment
- GoogleAnalytics code
- Favicons



# References
[original template](https://github.com/meshlogic/meshlogic.github.io)



### NEW POSTS: BASIC###
nikola new_post

### NEW POSTS: IPYNB###
- within markdown, place: `<!-- TEASER_END -->`
- nikola new_post --format=ipynb --import=../Display\ System.ipynb --title=Display\ System --tags=test_tag-1,test_tag-2 posts/jupyter/
- add 'jupyter' to post-metadata: category

### NEW POSTS & PAGES ###
nikola new_page


### CLEAN OUTPUT ###
nikola orphans
nikola clean
nikola check -f --clean-files


### BUILD ###
nikola build


### RUN LOCALLY ###
nikola serve -a 127.0.0.1 -b


### DEPPLOY - INIT GITHUB ACCESS ###
$ git config --global user.name "imtorg"
$ git config --global user.email "information@mgmt-tech.org"
$ git init
$ git remote add origin https://github.com/imtorg/imtorgdemo.github.io.git
$ git pull origin master --allow-unrelated-histories


### DEPPLOY ###
nikola github_deploy


### INSTALL & REMOVE PLUGINS ###
nikola plugin -i sidebar
nikola plugin -r sidebar



