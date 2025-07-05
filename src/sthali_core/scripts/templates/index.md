<p align="center">
    <a href="/{{ project['name'] }}/images/{{ project['name'] }}.svg">
        <img src="/{{ project['name'] }}/images/{{ project['name'] }}.svg" alt="{{ project['name'] }}" height="35%">
    </a>
    <em>{{ project["description"] | safe }}</em>
</p>
<p align="center">
    <a href="https://github.com/{{ organization_name }}/{{ project['name'] }}/actions/workflows/tests.yml" target="_blank">
        <img src="https://github.com/{{ organization_name }}/{{ project['name'] }}/actions/workflows/tests.yml/badge.svg" alt="">
    </a>
    <a href="https://github.com/{{ organization_name }}/{{ project['name'] }}/actions/workflows/deploy.yml" target="_blank">
        <img src="https://github.com/{{ organization_name }}/{{ project['name'] }}/actions/workflows/deploy.yml/badge.svg" alt="">
    </a>
    <a href="https://github.com/{{ organization_name }}/{{ project['name'] }}/actions/workflows/docs.yml" target="_blank">
        <img src="https://github.com/{{ organization_name }}/{{ project['name'] }}/actions/workflows/docs.yml/badge.svg" alt="">
    </a>
</p>

**Docs**: [https://{{ organization_name }}.github.io/{{ project['name'] }}/](https://{{ organization_name }}.github.io/{{ project['name'] }}/)

**PyPI**: [https://pypi.org/project/{{ project['name'] }}/](https://pypi.org/project/{{ project['name'] }}/)

**Source**: [https://github.com/{{ organization_name }}/{{ project['name'] }}/](https://github.com/{{ organization_name }}/{{ project['name'] }}/)

**Board**: [https://github.com/users/{{ organization_name }}/projects/1/](https://github.com/users/{{ organization_name }}/projects/1/)
