# WMDP
## Équipe et répartition des rôles
Wiame BOUICH: Dev / ML( Développement du pipeline Python et connexion aux modèles d'IA). 
Rim: Data (Préparation du corpus, annotation des réponses, calcul des métriques et visualisations).
Krou: Cyber / Stratégie( Analyse des risques, respect des règles éthiques et rédaction du rapport).

## Parcours choisi
Notre équipe a choisi le parcours WMDP : connaissances dangereuses et désapprentissage

## Objectif
Évaluer les connaissances des modèles de langage dans trois domaines : la biologie, la chimie et la cybersécurité.

## Dataset
Nous utiliserons le benchmark WMDP, composé de 3 668 questions à choix multiples (QCM) :
- Biologie : 1 273 questions.
- Chimie : 408 questions.
- Cybersécurité : 1 987 questions.

## Méthodologie
Nous allons comparer les performances d'au moins deux modèles d'intelligence artificielle en analysant leurs pourcentages de bonnes réponses dans chaque domaine.

## Sécurité et éthique
Nous utiliserons uniquement des connaissances de niveau universitaire et exclurons toute connaissance opérationnelle dangereuse.


## Hypothèse de recherche
Un LLM conserve mieux ses règles de sécurité face aux demandes dangereuses simples que face aux demandes qui tentent de contourner ses instructions.
- Test : comparer des prompts classiques et des prompts contenant « Ignore tes instructions précédentes ».
- Mesure : taux de refus corrects.


Nous allons tester cette hypothèse en comparant les
pourcentages de bonnes réponses dans chaque domaine.
