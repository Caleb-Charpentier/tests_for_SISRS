import sys
import pandas as pd

#get file paths to alignment_pi_locs_m25.txt and contigs_SeqLength.tsv
#path_to_seq_lengths, path_to_sites, min_threshold = sys.argv[0], sys.argv[1], sys.argv[2]

#read in informative site names
#with open() as file:
#   sites = file.readlines(pathToSites)
with open("C://Users/caleb/OneDrive/Desktop/alignment_pi_locs_m25.txt") as file:
    sites = file.readlines()

#This function works similar to grep in R or bash, but it searches for an input string through
#a list rather than a file/directory. Strings in the list 'stringList' that contain the substring 'searchString'
#will be returned in list format.

grep = lambda searchString, stringList: [j for j in stringList if j.__contains__(searchString)]

#read in contig names and their overall lengths
#contigLengths = pd.read_csv(pathToSeqLengths)
contig_info = pd.read_csv("C://Users/caleb/OneDrive/Desktop/contigs_SeqLength.tsv").iloc[:,[1,2]]


contigs = contig_info.iloc[:, 0]
contig_info_sites = pd.array([*map(lambda i: len(grep(i, sites)), contigs)])


contig_possible_sites = contig_info.iloc[:, 1]
relative_information = contig_info_sites / contig_possible_sites

contig_info['contig_possible_sites'] = contig_possible_sites
contig_info['relative_informational_value'] = relative_information

#contig_info = (contig_info[contig_info['relative_informational_value'] > min_threshold])
contig_info = (contig_info[contig_info['relative_informational_value'] > 0])
sorted_contig_data = contig_info.sort_values('relative_informational_value', ascending=False)

sorted_contig_data.to_csv("C://Users/caleb/OneDrive/Desktop/filtered_data.csv")
print(sorted_contig_data)