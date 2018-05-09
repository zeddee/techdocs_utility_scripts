# Sphinx evaluation

PROS

- Automated PDF and HTML builds
- standard tooling:
    - `jinja2` templating engine
    - `reST` or `md` text files as inputs
    - based on python
    - open sourced
- highly customizable
- modular
    - jinja allows breaking site template code-base up
    - fallback to standard solution

- not portable
    - every python project requires it's own project file (`conf.py`), which must contain
        - project name
        - project version
        - theme used
        - important information regarding folder structure
    - cannot pop theme folder into source folder and build to get theme
- pdf customization is opaque
- documentation is (ironically) sparse for customization; difficult to find docs on:
    - search
    - theming
    - toc customization
