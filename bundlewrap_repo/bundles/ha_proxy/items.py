from bundlewrap.repo import Repository
repo = Repository("bundlewrap_repo")
#Update the System 
actions = {
    'update repositories': {
        'command': "apt update",
        'expected_return_code': 0,
    },
        'upgrade packages': {
        'command': "apt upgrade -y",
        'expected_return_code': 0,
        'needs': ['action:update repositories'],
    }
}

pkg_apt = {
    "haproxy": {
        "installed": True,  # default
        "needs": ["action:upgrade packages"],
    },
}

apache_servers = repo.nodes_in_group("apache-webserver") #needed as context for templating the dynamic backend
files = {
    "/etc/haproxy/haproxy.cfg": {
        "mode": "0644",
        "owner": "root",
        "group": "root",
        "content_type": "jinja2",
        "encoding": "utf-8",
        "context": {"apache_servers": apache_servers},
        "source": "proxy.conf.j2",
        "needs": ["pkg_apt:haproxy"],
        "triggers": {
            "svc_systemd:haproxy.service:restart",
        },
    },
}


# Restarts the haproxy.service
svc_systemd = {
    "haproxy.service": {
        "triggered": True
    },
}