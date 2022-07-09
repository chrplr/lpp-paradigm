Running the (french version) experiment "Le Petit Prince"
=======================================================================

Time-stamp: <2019-05-31 20:53:52 christophe@pallier.org>


-------------

In  a nutshell:

    . run-lepetitprince-mri.sh


-------------

## Préparatifs ##

* Imprimer le fichier `questions_reponses_a_imprimer.pdf`; c'est sur ces feuilles que vous
indiquerez les réponses du participant après chaque run.
* l'écran de stimulation (boldscreen) doit être allumé et afficher un des écrans du PC.
* le PC doit être connecté soit au système magnacoustics soit au mrconfon (voir avec le/la manip) par l'intermédiare du boitier Aureon.
* le TTL doit être branché sur une  prise USB de la machine de stimulation

## Passation ##

* Ouvrir un terminal (Ctrl-Alt-T), puis aller dans le répertoire de l'expérience :

       cd Pallier/LePetitPrince

* Ouvrir le fichier "questions_a_presenter.pdf" sur l'écran Boldscreen:

        evince questions_a_presenter.pdf

* Pendant l'anatomie, présenter au sujet les instructions (page 1) et les pages d'illustrations (pages 2 et 3).

### Réglage son ###

Avant le premier bloc, faire un essai d'écoute et corriger les volumes si nécessaire (System settings/Sound output/Aureon Digital):

      aplay wav/lpp-intro.wav

### Acquisitions EPI (9 runs + localizer) ###

    . run-lepetitprince-mri.sh

Sélectionner le run et appuyer sur 'Entrée. **Note: Le participant doit garder les yeux fermés pendant les acquisitions**

A la fin du run, le curseur est automatiquement déplacé sur le prochain run. N'oubliez pas de poser les questions entre chaque run et de noter les réponses au QCM, ainsi que le NIP et la date sur le questionnaire. Indiquer tout problème pouvant avoir eu lieu pendant l'expérience.

---
Read README.txt for more detailed instructions.
