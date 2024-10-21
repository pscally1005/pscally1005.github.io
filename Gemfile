# frozen_string_literal: true

source "https://rubygems.org"
gemspec

gem "jekyll", ENV["JEKYLL_VERSION"] if ENV["JEKYLL_VERSION"]
gem "kramdown-parser-gfm" if ENV["JEKYLL_VERSION"] == "~> 3.9"
gem 'jemoji', '~> 0.13.0'
gem 'wdm', '>= 0.1.0' if Gem.win_platform?
gem "webrick", "~> 1.8"
gem 'jekyll-sitemap'