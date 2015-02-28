__author__ = 'sudeep'


class Link:
    def __init__(self, url, comment, is_seen):
        self.url = url
        self.comment = comment
        self.is_seen = is_seen


def get_links(raw_list, participant_name):
    url_index = raw_list[0].index(participant_name + '\'s links')
    comment_index = url_index + 1
    is_seen_index = url_index + 2

    if(url_index is not None):
        links = list(Link(i[url_index], i[comment_index], i[is_seen_index]) for i in raw_list[2:(len(raw_list))])
    return filter(None, links)

def is_link_new(link, old_links):
    return not any(i.url == link.url for i in old_links)
