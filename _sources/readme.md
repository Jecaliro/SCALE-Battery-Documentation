Info pour la compilation de la doc:

1. Switcher sur l'environement de doc >CONDA activate FEVDoc
1. Renseigner les fichiers 
    1. _config.yml
    1. _toc.yml
compiler la doc 
> jupyter-book build DOCMD/
Compiler en forcant le rebuild
> jupyter-book build --all DOCMD/