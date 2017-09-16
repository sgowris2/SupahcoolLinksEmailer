__author__ = 'sudeep'

import re
from Link import get_links, is_link_new

class Participant:

    global directory
    names_and_emails_list = [('Pujan', 'pujanghelani@gmail.com'), ('Sudeep', 'sgowris2@gmail.com')]
    directory = dict(names_and_emails_list)

    def __init__(self, name, email, old_list, new_list):
        self.name = name
        self.email = email
        self.old_links = get_links(old_list, self.name)
        self.new_links = get_links(new_list, self.name)
        self.diff_links = self.get_diff_links()

    def get_diff_links(self):
        all_links = [i for i in self.new_links if is_link_new(i, self.old_links)]
        return [i for i in all_links if (i.is_seen != 'Yes')]


def get_participants(old_list, new_list):
    titles = ','.join(filter(None, new_list[0])) #TODO : Do a check for new participants and handle them
    participant_names = re.findall(",?(.*?)\'s links,?", titles)
    participants = create_participants(participant_names, old_list, new_list)
    return participants


def create_participants(names, old_list, new_list):
    participants = []
    for i in names:
        if(directory.get(i) is not None):
            participants.append(Participant(i, directory[i], old_list, new_list))
        else:
            participants.append(Participant(i, '', old_list, new_list))
    return participants