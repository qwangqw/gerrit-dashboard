import sys
import yaml
import webbrowser


def get_team(teamname):
    with open("gerrit_ids.yaml", 'r') as gerrit_ids:
        teams = yaml.load(gerrit_ids)

    return teams[teamname]


def get_url(teamlist):
    base_url = "https://review.openstack.org/#/q/"
    query = list()
    query.append('(' + '+OR+'.join(['owner:' + member for member in teamlist]) + ')')
    query.append('status:open')
    return base_url + '+'.join(query)


def main():
    url = get_url(get_team('Kolla'))
    print("Opening " + url)
    webbrowser.open_new_tab(url)


if __name__ == '__main__':
    sys.exit(main())
