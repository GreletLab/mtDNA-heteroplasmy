import os

def reverse_complement(seq):
    """Generate the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

def count_reads_wt_and_mut(fastq_file, wt_seq, mut_seq):
    """Count the total number of reads and those containing WT or mutated sequences, including reverse complements."""
    total_reads = 0
    reads_with_wt = 0
    reads_with_mut = 0
    
    # Calculate the reverse complements
    wt_seq_rc = reverse_complement(wt_seq)
    mut_seq_rc = reverse_complement(mut_seq)

    with open(fastq_file, 'r') as f:
        while True:
            # Read four lines per entry (identifier, sequence, +, quality score)
            identifier = f.readline().strip()
            sequence = f.readline().strip()
            plus = f.readline().strip()
            quality = f.readline().strip()

            # Break if end of file is reached
            if not quality:
                break

            total_reads += 1

            # Check if the WT sequence or its reverse complement is present
            if wt_seq in sequence or wt_seq_rc in sequence:
                reads_with_wt += 1

            # Check if the mutated sequence or its reverse complement is present
            if mut_seq in sequence or mut_seq_rc in sequence:
                reads_with_mut += 1

    return total_reads, reads_with_wt, reads_with_mut

# Function to calculate the percentage of reads
def calculate_percentage(total, count):
    """Calculate the percentage of reads containing a given sequence."""
    if total == 0:
        return 0
    return (count / total) * 100

def process_all_fastq_in_folder(folder_path, wt_seq, mut_seq, output_file):
    """Process all FASTQ files in a folder and save the results in an output file."""
    
    # Create the output directory if it does not exist
    output_dir = os.path.dirname(output_file)
    
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except OSError as e:
            print(f"Error creating directory: {e}")
            return

    with open(output_file, 'w') as out_f:
        # Column headers
        out_f.write("File,Total Reads,WT Reads,Mut Reads,% WT,% Mut\n")  
        
        fastq_files = [file_name for file_name in os.listdir(folder_path) if file_name.endswith('.fastq')]
        if not fastq_files:
            print("No FASTQ files found in the specified folder.")
            return

        for file_name in fastq_files:
            fastq_file = os.path.join(folder_path, file_name)
            total_reads, reads_with_wt, reads_with_mut = count_reads_wt_and_mut(fastq_file, wt_seq, mut_seq)
            
            # Calculate percentages
            pct_wt = calculate_percentage(total_reads, reads_with_wt)
            pct_mut = calculate_percentage(total_reads, reads_with_mut)
            
            # Write results to the output file
            out_f.write(f"{file_name},{total_reads},{reads_with_wt},{reads_with_mut},{pct_wt:.2f},{pct_mut:.2f}\n")
            print(f"Processed file: {file_name}")

# Example usage
folder_path = r'/HD/input'
wt_seq = 'AGTGAATAATTA'  # Wild-type (WT) sequence
mut_seq = 'AGTGAACAATTA'  # Mutated sequence
output_file = r'/HD/output.csv'
  # Specify the output file path
# Process all FASTQ files in the folder
process_all_fastq_in_folder(folder_path, wt_seq, mut_seq, output_file)
