# AGENTS.md

## Cursor Cloud specific instructions

This is a **Jekyll static blog** (Beautiful Jekyll theme) served via GitHub Pages. There is only one service: Jekyll itself.

### Quick reference

- **Build**: `eval "$(rbenv init -)" && bundle exec jekyll build`
- **Serve (dev)**: `eval "$(rbenv init -)" && bundle exec jekyll serve --host 0.0.0.0 --port 4000`
- **Site URL**: http://localhost:4000/

### Gotchas

- **Ruby version**: The `github-pages` gem v197 requires Ruby < 3.0. Ruby 2.7.8 is installed via `rbenv` at `~/.rbenv/versions/2.7.8`. You must run `eval "$(rbenv init -)"` before any `bundle` or `ruby` command (this is already in `~/.bashrc`).
- **Gemfile.lock platform**: The committed `Gemfile.lock` targets `x64-mingw32` (Windows). On Linux, run `BUNDLE_FORCE_RUBY_PLATFORM=1 bundle install` to resolve native gems correctly. The installed gems live in the rbenv-managed Ruby directory and do not require the lockfile platform to match.
- **No tests or lint**: This is a pure static site with no test suite, no linter configuration, and no CI. Validation is done by building the site (`jekyll build`) and visually inspecting it.
- **`_config.yml` changes** require a full server restart (stop and re-run `jekyll serve`); other file changes are picked up by live reload.
