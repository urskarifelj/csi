# -*- coding: utf-8 -*-
# --author-- = Urska Rifelj

text_file = open("dna.txt")
lines = text_file.read()

hair_color = {
    "Black": "CCAGCAATCGC",
    "Brown": "GCCAGTGCCG",
    "Blonde": "TTAGCTATCGC"
    }

facial_shape = {
    "Square": "GCCACGG",
    "Round": "ACCACAA",
    "Oval": "AGGCCTCA"
    }

eye_color = {
    "Blue": "TTGTGGTGGC",
    "Green": "GGGAGGTGGC",
    "Brown": "AAGTAGTGAC"
    }

gender = {
    "Female": "TGAAGGACCTTC",
    "Male": "TGCAGGAACTTC",
}

race = {
    "White": "AAAACCTCA",
    "Black": "CGACTACAG",
    "Asian": "CGCGGGCCG"
    }


for hair_key, hair_value in hair_color.iteritems():
    if lines.find(hair_value) > 0:
        print "Hair color: ", hair_key


for facial_key, facial_value in facial_shape.iteritems():
    if lines.find(facial_value) > 0:
        print "Facial shape: ", facial_key


for eye_key, eye_value in eye_color.iteritems():
    if lines.find(eye_value) > 0:
        print "Eye color: ", eye_key


for gender_key, gender_value in gender.iteritems():
    if lines.find(gender_value) > 0:
        print "Gender: ",gender_key


for race_key, race_value in race.iteritems():
    if lines.find(race_value) > 0:
        print "Race: ", race_key
