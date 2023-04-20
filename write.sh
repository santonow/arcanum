filepath=$(python -m arcanum.create_file diary)

vim "$filepath"

python -m arcanum.edit_mkdocs_yml mkdocs.yml diary
