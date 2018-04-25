#####################################
Removing Files from a Git repository
#####################################

Avoid committing large files to a Git repository. Unless you have LFS enabled, large files don't play well with the Git repository structure and will add significant bloat to it. What you want is a small repository that is quick to clone and quick to build. Store large files on a dedicated LFS repository, or on a dedicated file storage system like Google Drive.

By virtue of being a version control system, Git preserves all files that are part of a repo's history. This means that deleting a file in the repository only removes it from the working tree, but does not remove it from the repository's Git database. To remove a file completely from the Git database, you must perform the following:

#. Do not delete the file first.
#. ``git rm -rf --cached <files>``
#. ``rm -rf <files``
#. ``git add --all :/``
#. ``git commit -m "removed <files>"``

If you find that large files have already been committed to the repository, remove them using ``git filter-branch``:

.. code-block:: bash

    # This removes `filename` from the whole repository's history.
    # If the file is not present at any point of the repo's history, running
    # `git filter-branch --tree-filter 'rm filename' HEAD will fail at the first commit
    # where the file is not present.
    # Run with 'rm -f' to avoide that.
    git filter-branch --tree-filter 'rm -f filename' HEAD
