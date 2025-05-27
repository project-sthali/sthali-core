# Requirements

## Prerequisites

- Python {{ python_version }}
- `pip` package manager

## Runtime Dependencies

This project requires the following Python packages with specific versions:

{% for dependency in dependencies %}
- `{{ dependency }}`
{% endfor %}

## Optional Dependencies
{% for group, deps in optional_dependencies.items() %}
### {{ group }}
{% for dep in deps %}
- `{{ dep }}`
{% endfor %}
{% endfor %}
