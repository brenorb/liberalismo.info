#!/usr/bin/env bash
set -euo pipefail
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib.sh"
cd "$ROOT_DIR"
build_site

bundle exec ruby - "$ROOT_DIR" "$BUILD_DIR" <<'RUBY'
require "jekyll"
require "nokogiri"
require "tmpdir"
require "fileutils"
root, build_dir = ARGV
{
  "index.html" => "index.md",
  "library/the-law/index.html" => "library/the-law.md",
  "authors/frederic-bastiat/index.html" => "authors/frederic-bastiat.md",
  "docs/VISION/index.html" => "docs/VISION.md"
}.each do |output, source|
  document = Nokogiri::HTML(File.read(File.join(build_dir, output)))
  links = document.css("a[data-edit-page]")
  expected = "https://github.com/brenorb/liberalismo.info/edit/main/#{source}"
  abort "Wrong or missing source edit link for #{output}" unless links.size == 1 && links.first["href"] == expected
end

Dir.mktmpdir("edit-page-fixture") do |directory|
  FileUtils.mkdir_p(File.join(directory, "_includes"))
  FileUtils.mkdir_p(File.join(directory, "nested"))
  FileUtils.cp(File.join(root, "_includes/edit-page.html"), File.join(directory, "_includes/edit-page.html"))
  File.write(File.join(directory, "nested", "two words #.md"), "---\npermalink: /different-public-url/\n---\n{% include edit-page.html %}\n")
  File.write(File.join(directory, "hidden.md"), "---\nedit_page: false\n---\n{% include edit-page.html %}\n")
  config = Jekyll.configuration({ "source" => directory, "destination" => File.join(directory, "_site"), "repository_url" => "https://github.com/example/archive", "repository_branch" => "release/v2", "quiet" => true, "plugins" => [] })
  Jekyll::Site.new(config).process
  document = Nokogiri::HTML(File.read(File.join(directory, "_site/different-public-url/index.html")))
  expected = "https://github.com/example/archive/edit/release%2Fv2/nested/two%20words%20%23.md"
  abort "Source path / branch were not encoded correctly" unless document.at_css("a[data-edit-page]")&.[]("href") == expected
  abort "Disabled page still has edit link" if Nokogiri::HTML(File.read(File.join(directory, "_site/hidden.html"))).at_css("a[data-edit-page]")
end
puts "Source edit links passed"
RUBY
