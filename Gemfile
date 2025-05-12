source "https://rubygems.org"

gem "jekyll", "~> 4.3.3"
gem "jekyll-theme-chirpy", "~> 7.2", ">= 7.2.4"
gem "html-proofer", "~> 5.0", group: :test

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"
  gem "jekyll-seo-tag", "~> 2.8"
  gem "jekyll-sitemap", "~> 1.4"
  gem "jekyll-paginate", "~> 1.1"
  gem "jekyll-archives", "~> 2.2"
end

platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.2.0", platforms: [:mingw, :x64_mingw, :mswin]