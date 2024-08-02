# Let's create the CHANGELOG.md file to keep track of updates and changes to the repository
changelog_content = """
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.0.0] - 2024-08-01
### Added
- Created Notes App
  - Added feature to list .md and .html files from directories
  - Added pagination for notes list
  - Added search functionality
  - Added note detail view to display the contents of selected note

"""

with open("/mnt/data/CHANGELOG.md", "w") as file:
    file.write(changelog_content)

