.. warning::
   This repository is out of date. Kraken has moved to a new zenodo based
   repository, i.e. this repository won't be updated in the future and listing
   the available models through `kraken list` is not in any way connected to
   the data here.

kraken-models
=============

This repository contains recognition models for `kraken <http://kraken.re>`_,
both legacy pyrnn (converted to pronn) and clstm ones. To have one or more
model added open a pull request or send an email to ``models@kraken.re``.

Metadata
--------

Each model is linked to a JSON metadata record containing the following fields:

author
        Name of the entity that training the model.

author-email
        Email address of trainer.

summary
        A short description of the model's purpose.

description
        An in-depth explanation of what the model is supposed to recognize,
        which training data has been employed, pertinent transcription
        standards, and duration of training/validation set accuracy achieved.

script
        An `ISO15924 <http://www.unicode.org/iso15924/iso15924-codes.html>`_
        script 4 character script identifier.

graphemes
        A list of UTF-8 code points of possible model outputs.

license
        License of the model.

name
        File name of the model in the repository.

url
        Link to further information regarding the model/organization responsible.


