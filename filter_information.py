import sys
import pandas as pd

#get file paths to alignment_pi_locs_m25.txt and contigs_SeqLength.tsv
#path_to_seq_lengths: Path to .tsv where contig lengths are located.
#                 Ex: "C://Users/caleb/OneDrive/Desktop/contigs_SeqLength.tsv"
#path_to_sites: Path to .txt file where names of individual sites on contigs are located
#                 Ex: "C://Users/caleb/OneDrive/Desktop/alignment_pi_locs_m25.txt"
#min_threshold: Removes contigs whos percentage of informative sites falls below a certain value.
#                 Ex: If you want to filter out contigs that are less than 25% informative, min_threshold
#                     should be 0.25
#path_to_output: Path to write filtered_data.tsv to. Must include the final backslash.
#                 Ex: "C://Users/caleb/OneDrive/Desktop/"


path_to_seq_lengths, path_to_sites, min_threshold, path_to_output = sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3]



#path_to_seq_lengths, path_to_sites, min_threshold, path_to_output = "C://Users/caleb/OneDrive/Desktop/contigs_SeqLength2.tsv", "C://Users/caleb/OneDrive/Desktop/alignment_pi_locs_m25.txt", 0.1, "C://Users/caleb/OneDrive/Desktop/"



#read in informative site names
with open(path_to_sites) as file:
   sites = file.readlines()


#This function works similar to grep in R or bash, but it searches for an input string through
#a list rather than a file/directory. Strings in the list 'stringList' that contain the substring 'searchString'
#will be returned in list format.

grep = lambda searchString, stringList: [j for j in stringList if j.__contains__(searchString)]

#read in contig names and their overall lengths
contig_info = pd.read_csv(path_to_seq_lengths)


contigs = contig_info.iloc[:, 0]
contig_info_sites = pd.array([*map(lambda i: len(grep(i, sites)), contigs)])


contig_possible_sites = contig_info.iloc[:, 1]
relative_information = contig_info_sites / contig_possible_sites

contig_info['contig_possible_sites'] = contig_possible_sites
contig_info['relative_informational_value'] = relative_information

#contig_info = (contig_info[contig_info['relative_informational_value'] > min_threshold])
contig_info = (contig_info[contig_info['relative_informational_value'] >= min_threshold])
sorted_contig_data = contig_info.sort_values('relative_informational_value', ascending=False)

sorted_contig_data.to_csv(path_to_output + "filtered_data2.csv")
print(sorted_contig_data)

