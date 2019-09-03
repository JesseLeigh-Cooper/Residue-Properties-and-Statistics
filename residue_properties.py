"""
Author: Jesse Leigh-Cooper
Created: May 2019
"""
import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO

input_sequence = "Insert Amino Acid Sequence Here" ##<--sequence
sequence = input_sequence.upper()

def calc_sequence_length(sequence):
    sequence_length = len(sequence)
    return sequence_length

hydrophobic = ["A", "I", "L", "V"]
aromatic = ["Y", "W", "F"]
non_polar = ["Q", "C", "N", "T"]
acidic = ["D", "E"]
basic = ["K", "H", "R"]
unique = ["P", "G"]
property_list = [hydrophobic, aromatic, non_polar, acidic, basic, unique]
property_list_names = ["hydrophobic", "aromatic", "non polar", "acidic", "basic", "unique"]

def calc_seq_properties(sequence):
    #Create dictionary containing percentages and property
    property_dict = {}
    df = pd.DataFrame(property_dict)
    #Create list containing the counts of residues for each element in property lists
    count_list = []
    for characteristic in property_list:
        accumulator = 0
        for amino_acid in characteristic:
            accumulator+= sequence.count(amino_acid)
        count_list.append(accumulator)
    #Modify empty dictionary with lists and other columns
    df['Property'] = property_list_names
    df['Residues'] = property_list        
    df['Count'] = count_list
    df['Percent'] = round(((df['Count']/sum(df['Count']))*100), 1)
    return(df)

def create_properties_plot(determine_properties):   
    chart_colours = ['c', 'm', 'r', 'b', 'y', 'g']
    plt.pie(determine_properties.Percent, 
            labels=property_list_names, 
            colors=chart_colours, 
            startangle=90, 
            shadow=True, 
            autopct=('%1.1f%%')
            )
    plt.title('Residues by Physiochemical Properties')
    plt.show()

calculate_seq_length = calc_sequence_length(sequence)
determine_properties = calc_seq_properties(sequence)
print("Sequence Length = "+str(calculate_seq_length))
print("Residues by Physiochemical Property")
print(determine_properties)
present_properties = create_properties_plot(determine_properties)