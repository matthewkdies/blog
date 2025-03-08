import re
import urllib.parse
from textwrap import dedent

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

# I'm not using "X" -- what am I, a racist?
bluesky_intent = "https://bsky.app/intent/compose"
include = re.compile(r"blog/[1-9].*")


def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files: Files):
    if not include.match(page.url):
        return markdown

    page_url = config.site_url + page.url
    text = urllib.parse.quote(f"{page.title}\n{page_url}")

    return markdown + dedent(f"\n\n[Share on :simple-bluesky:]({bluesky_intent}?text={text}){{ .md-button }}")
