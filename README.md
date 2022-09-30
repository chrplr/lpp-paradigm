Passation de l'expérience "Le Petit Prince"
===========================================

Time-stamp: <2019-03-12 17:34:07 christophe@pallier.org>


## ACCUEIL DU VOLONTAIRE ##
* Le volontaire est accueilli par l'équipe para-médicale.
* Pas d'entraînement, les consignes sont :
    * Le participant ne connait pas l'histoire du Petit Prince ou ne l'a pas lu, entendu .....  depuis 5 ans.
    * rester éveillé, sinon les données sont perdues.
    * ne pas bouger.
    * relecture des consignes pendant la séquence d'anatomie + présentaiton des images du début du livre.
    * **écouter attentivement avec les yeux fermés lors des blocs**.
    * ouvrir les yeux quand la manip radio l'indique (entre les blocs), lire les questions présentées
          à l'écran et y répondre. Il y a des questions à choix multiple et de questions ouvertes.
        
        
        
## FICHIERS ASSOCIES ## 
* README.pdf : instructions.
* questions_a_presenter.pdf : questions à présenter après chaque bloc.
* questions_reponses_a_imprimer.pdf : questions présentées à la fin de chaque bloc (pour imprimer et noter, utilisé pour calculer un score).
* Le Petit Prince - Antoine de Saint-Exupery.pdf : texte du livre (non utilisé)
* Les fichiers audio présents sur l'ordinateur de stim.



## AVANT L'ACQUISTION ##
* Imprimer (l'expérimentateur) le fichier "questions_reponses_a_imprimer.pdf" :  c'est sur ces feuilles que vous indiquerez les réponses du participant après chaque run.
* Le son doit être réglé au maximum sur le PC. Ce dernier doit être connecté de préférence au sytème OptoActive ou bien soit au système magnacoustics soit au mrconfon (voir avec le/la manip).
* Le TTL doit être branché sur une prise USB de la machine de stimulation, le tester en ouvrant une console et en appuyant sur le bouton TTL.
* **Vérifier le cable de branchement DVI de l'écran BOLD**
* Régler l'affichage :  
    * Lancer NVIDIA Settings (raccourci sur la panneau à gauche de l'écran) sur la PC de stim.  
    * Sur l'interface de NVidia setting (X Server Display Configuration), séparer les 3 écrans qui doivent être reconnus : Boldscreen (CMR BoldScreen), l'écran du PC de stim (ViewSonic x2) et celui qui se trouve en haut à droite dans la salle des consoles (ViewSonic x2), qui doit être le miroir du boldscreen). 
    * Identifier l'écran qui se trouve en haut à droite, et le positionner sur le boldscreen pour qu'ils soient en mode miroir.
    * Cliquer sur **Apply** pour valider. Si le bouton **Apply** est grisé, augmenter la fenêtre ou relancer Nvidia Settings.
    * Vérifer la résolution et le refresh rate : 1920x1080 - 120Hz.
    * Placer le document **questions_a_presenter.pdf** sur l'écran en haut à droite. Le document est à faire défiler pendant l'acquisition Anatomie et pour poser les questions après les runs, mode plein écran (=mode présentation).



## NOTES POUR LES MANIPS ##
* Boîte englobante : priorité aux lobes temporaux (cervelet ou en haut du cerveau peuvent être tronqués si nécessaire).


## PASSATION ##
2 sessions le même jour :

* Session 1 : anatomie (10') +  "Apprentissage son" + 4 runs fonctionnels 
* Session 2 : 5 runs fonctionnels + localizer

Durée d'un bloc fonctionnel ou du localizer : 10 minutes.

Voir s'il est possible de passer un bloc supplémentaire (si moins de 1H30 au final et si le participant est d'accord) pendant la 1re session. Cela laissera plus de temps pour la seconde session si besoin (problème technique par exemple). 


### ANATOMIE ###
* Ouvrir un terminal (Ctrl-Alt-T), puis aller dans le répertoire de l'expérience :

       cd Pallier/LePetitPrince


* Ouvrir le fichier "questions_a_presenter.pdf" et la placer sur l'écran Boldscreen:

        evince questions_a_presenter.pdf
        
        
  * Pendant l'anatomie, présenter au sujet les instructions (page 1) et les pages d'illustrations (pages 2 et 3).


### SON ###
Faire un premier test son, sans séquence, pour s'assurer que le volontaire entend bien des 2 côtés.
Avant le premier bloc fonctionnel, faire un essai d'écoute ou "Apprentissage son" selon le dispositif utilsé. Préparer sa commande, ou utilser
un second terminal, car on peut être géner par le retour du TTL (lettre t qui s'affiche dans le terminal) :


      aplay stimuli/lpp-intro.wav


### ACQUISITIONS EPI (9 runs + 1 localizer) ###

    . run-lepetitprince-mri.sh


Sélectionner le run et appuyer sur 'Entrée'. Le nom du sujet peut être demandé, mais ceci n'a pas d'importance car le NIP est indiqué sur le "questions_reponses_a_imprimer.pdf" et qu'il n'y a pas de fichiers à récupérer. La croix de la stim est verte et passe au blanc quand le programme Expyriment a reçu le TTL. A la fin du run, le curseur est automatiquement déplacé sur le prochain run. N'oubliez pas de poser les questions, faire défiler la questionnaire sur l'écran en haut à droite, entre chaque run et de noter les réponses au QCM, ainsi que le NIP, la date sur le questionnaire et d'entrée du sujet (pour ne pas dépasser 1H30). Veiller à ce que l'écran qui affiche le pdf ait le focus. Indiquer tout problème pouvant avoir eu lieu pendant l'expérience.


### NOTES ###    
* S'il faut quitter Epyriment, appuyer sur Escap.
* Le TTL est renvoyé au terminal qui lance Experiment, si vous avez lancé Experiment et que le TTL ne s'est pas encore déclenché, ne pas utilser la souris ou changer de terminal ce qui pourrait pour changer déplacer le focus et ne pas lancer la stim.
* Experyment peut s'interrompre, dans ce cas attendre la fin du bloc avant de relancer car le "fichier son" fonctionne toujours.
* S'il y a un problème de reconnaissance du BoldScreen, et qu'il faut tout redémarrer, commencer par tout éteindre, rallumer la Boldscreen puis le PC de stimulation.
      

## APRES L'ACQUISTION ##
* Il n'y pas de fichiers Experyment à récupérer sur le PC de stim;
* Demander au participant s'il a dormi ou s'il a eu une gêne.



