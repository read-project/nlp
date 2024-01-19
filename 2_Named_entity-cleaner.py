'''1. prendere primo lemma in eng
2. sostituire underscore con spazio
3. sostituire iniziali in maiuscolo
4. match preciso dei lemmi con glossa in eng
--> quelli che non corrispondono a questi criteri vanno mantenuti'''
import csv

with open('dataset_full.csv', 'r', encoding="utf8") as myFile:
    # create a dict
    reader = csv.DictReader(myFile)
    NE_list = []
    C_list = []
    d = dict()
    #crea colonna con prima label in inglese
    for row in reader:
        label = row['lab_en'].split(' ')[0]
        lab = label.replace('_', ' ')
        capital = lab.title()
        capitalOk = capital.replace('Of', 'of')
        row['First_Lab'] = capitalOk
        C_list.append(dict(row))
    #indica tipo di entità
    for line in C_list:
        #synset senza glossa in inglese
        if len(line['gloss_en']) < 1:
            line['Type'] = "NEgl"
            NE_list.append(dict(line))
        #synset con label con 4 parole o più
        elif line['First_Lab'].count(' ') >= 3:
            line['Type'] = "NE4"
            NE_list.append(dict(line))
        #istanze di human
        elif 'bn:00044576n' in line['hypernym']:
            line['Type'] = "NEhuman"
            NE_list.append(dict(line))
        # istanze di museum
        elif 'bn:00056426n' in line['hypernym']:
            line['Type'] = "NEmuseum"
            NE_list.append(dict(line))
        # istanze di painting
        elif 'bn:00060201n' in line['hypernym']:
            line['Type'] = "NEpainting"
            NE_list.append(dict(line))
        # istanze di artgallery
        elif 'bn:00005940n' in line['hypernym']:
            line['Type'] = "NEartgallery"
            NE_list.append(dict(line))
        elif 'bn:26462367n' in line['hypernym']:
            line['Type'] = "NEartgallery"
            NE_list.append(dict(line))
        # istanze di village
        elif 'bn:00042729n' in line['hypernym']:
            line['Type'] = "NEvillage"
            NE_list.append(dict(line))
        # istanze di town
        elif 'bn:00077773n' in line['hypernym']:
            line['Type'] = "NEtown"
            NE_list.append(dict(line))
        # istanze di statue
        elif 'bn:00074064n' in line['hypernym']:
            line['Type'] = "NEstatue"
            NE_list.append(dict(line))
        # istanze di sculpture
        elif 'bn:17175797n' in line['hypernym']:
            line['Type'] = "NEsculpture"
            NE_list.append(dict(line))
        # istanze di street
        elif 'bn:20139967n' in line['hypernym']:
            line['Type'] = "NEstreet"
            NE_list.append(dict(line))
        # istanze di artist
        elif 'bn:00006182n' in line['hypernym']:
            line['Type'] = "NEartist"
            NE_list.append(dict(line))
        # istanze di square
        elif 'bn:00065099n' in line['hypernym']:
            line['Type'] = "NEsquare"
            NE_list.append(dict(line))
        # istanze di hotel
        elif 'bn:00044967n' in line['hypernym']:
            line['Type'] = "NEhotel"
            NE_list.append(dict(line))
        # istanze di art movement
        elif 'bn:00005943n' in line['hypernym']:
            line['Type'] = "NEartmovement"
            NE_list.append(dict(line))
        # istanze di art exhibition
        elif 'bn:00005938n' in line['hypernym']:
            line['Type'] = "NEartexhibition"
            NE_list.append(dict(line))
        # istanze di taxon
        elif 'bn:00076248n' in line['hypernym']:
            line['Type'] = "NEtaxon"
            NE_list.append(dict(line))
        # istanze con first label nei primi 30 caratteri di gloss_en
        elif line['First_Lab'] in line['gloss_en'][0:30]:
            line['Type'] = "NE1"
            NE_list.append(dict(line))
        # istanze di municipality
        elif 'bn:00056337n' in line['hypernym']:
            line['Type'] = "NEmunic"
            NE_list.append(dict(line))
        elif 'is a town' in line['gloss_en']:
            line['Type'] = "NEmunic"
            NE_list.append(dict(line))
        # istanze con virgola nella label
        elif ',' in line['First_Lab']:
            line['Type'] = "NEvirgola"
            NE_list.append(dict(line))
        #concetti
        else:
            line['Type'] = "Concept"
            NE_list.append(dict(line))

fieldnames = ['id', 'First_Lab', 'Type', 'lab_it', 'lab_en', 'gloss_it', 'gloss_en', 'meronimia', 'olonimia', 'instance_of', 'type_of', 'hypernym', 'hyponym', 'NE']
with open('speriamo1.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(NE_list)


