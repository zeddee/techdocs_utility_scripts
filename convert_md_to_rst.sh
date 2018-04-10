# Converts all *.md files in directory to rst
echo ".. toc-tree::\n   :maxdepth: 1" > contents.rst
for file in ./*.md; do
    file_base=${file%.md}
    pandoc --from=markdown --to=rst -o ${file_base}.rst $file

    # Adds current file to contents.rst for sphinx builds
    echo $file_base >> contents.rst
done
