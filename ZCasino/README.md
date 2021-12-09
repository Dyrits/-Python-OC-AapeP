# ZCasino
Le ZCasino est une simulation de jeu de pari pour deviner un nombre aléatoire.  

## Table of contents
- [Related content](#related-content)
- [General information](#general-content)
  - [Rules](#rules)
- [Contributing](#contributing)
- [Contact](#contact)
- [Technologies](#technologies-and-tools)
- [Status](#status)

## Related content
[OpenClassrooms](https://openclassrooms.com/) - Apprenez à programmer en Python  
Le jeu, avec ses règles peu cohérentes, a été fait dans le cadre d'un exercice.

## General information
## Rules 
Le joueur mise sur un numéro compris entre 0 et 49 (50 numéros en tout). En choisissant son numéro, il y dépose la somme qu'il souhaite miser.  
La roulette est constituée de 50 cases allant naturellement de 0 à 49. Les numéros pairs sont de couleur noire, les numéros impairs sont de couleur rouge. Le croupier lance la roulette, lâche la bille et quand la roulette s'arrête, relève le numéro de la case dans laquelle la bille s'est arrêtée. Dans notre programme, nous ne reprendrons pas tous ces détails « matériels » mais ces explications sont aussi à l'intention de ceux qui ont eu la chance d'éviter les salles de casino jusqu'ici. Le numéro sur lequel s'est arrêtée la bille est, naturellement, le numéro gagnant.  
Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50, plutôt faible), le croupier lui remet 3 fois la somme misée.  
Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur que le numéro gagnant (s'ils sont tous les deux pairs ou tous les deux impairs). Si c'est le cas, le croupier lui remet 50 % de la somme misée. Si ce n'est pas le cas, le joueur perd sa mise.  

## Technologies and tools
- Python 3

## Status
**Version 1.00.00 (10/03/2020)**  
Completed

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate (if any).

## Contact
Created by [Dylan J. Gerrits](https://github.com/Dyrits).


