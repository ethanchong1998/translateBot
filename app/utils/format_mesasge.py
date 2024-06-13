from app.config.channel_rules import top7ico_rules
from urlextract import URLExtract
from bs4 import BeautifulSoup


def format_message(text: str, channel: str) -> str:
    text = replace_urls(text)
    text1 = remove_html_tags(text)
    final_text = apply_channel_rules(channel, text1)

    return final_text


def apply_channel_rules(channel, msg):
    formatted_msg = msg
    if channel == "top7ico":
        formatted_msg = top7ico_rules(msg)
    return formatted_msg


def replace_urls(text: str) -> str:
    extractor = URLExtract()
    urls = extractor.find_urls(text)
    for url in urls:
        text = text.replace(url, f"<a href='{url}'>— link</a>")
        print("replaced:", text)

    return text


def remove_html_tags(text: str) -> str:
    soup = BeautifulSoup(text, 'html.parser')
    for e in soup.find_all():
        if e.name not in ['b', 'i', 'a', 'code', 'pre']:
            e.unwrap()

    return text



