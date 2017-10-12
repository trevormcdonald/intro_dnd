# README #

This project allows a Dungeon Master to send the players the linked [Google Form](https://docs.google.com/forms/d/1VGUVROgLdVyAGdP89UKuo0nVxyrmLWX5H5k_a3D5lJg/copy), download the responses, and generate character sheets. Please don't modify this form! The link should make a copy of the form that you can edit in your own account.
Included here is a list of the steps needed to get this in working condition, and to get everyone who fills out the form everything they need to get started!

# Notes #

This is for Fifth Edition Dungeons and dragons, and requires access to a pdf of the Player's Handbook for full functionality.

# Installation #

This project uses Python 2 and relies on a couple other projects.

Pdftk: this can be installed with `apt-get install pdftk`. Pdftk is for generating the PDFs.
Fdfgen: the repo for this is [here](https://github.com/ccnmtl/fdfgen). Install it with one of [these](https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github) methods. This is for filling out PDF forms.
PyPDF2: this can be installed with `pip install pypdf2`. This is for grabbing the parts of the Player's Handbook relevant to the player.

# Run it #
`python dnd.py` should generate a directory for every response in the survey that was filled out! Unfortunately, this project isn't battle-hardened yet. It expects the survey responses in a file called "responses.csv",
and expects a PDF of the Player's Handbook in a file called "phb.pdf".
Both of files are expected to be in the same directory as the source files.

# Results #
A directory with "PlayerName" is generated containing a filled out Character Sheet, a blank Character Sheet, Class info, Race info, and Background info. This file can then be zipped up and sent to the player.
