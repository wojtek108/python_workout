from collections import defaultdict


def shells_and_users_by_popularity(filename):
    shells = defaultdict(list)
    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue

        username, *rest, shell = one_line.strip().split(':')

        shells[shell].append(username)

    return sorted(shells.items(), key=len)

print(shells_and_users_by_popularity('abc.txt'))
