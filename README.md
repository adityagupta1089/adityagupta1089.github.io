# adityagupta1089.github.io
[![Build Status](https://travis-ci.com/adityagupta1089/adityagupta1089.github.io.svg?branch=master)](https://travis-ci.com/adityagupta1089/adityagupta1089.github.io)

My personal Webpage / Blog.

# Setup
- `sudo apt-get install ruby-full build-essential zlib1g-dev`
- `gem install jekyll bundler`
- `bundle install`

# Usage 
- `bundle exec jekyll build` - Builds the site and outputs a static site to a directory called `_site`.
- `bundle exec jekyll serve`- Does jekyll build and runs it on a local web server at `http://localhost:4000`, rebuilding the site any time you make a change.

# Creating Posts/Drafts
Prefix `bundle exec jekyll`
- `post <name>`: create post
- `draft <name>`: create draft
- `publish _drafts/<filename>`: publish draft
- `unpublish _posts/<filename>`: unpublish draft
