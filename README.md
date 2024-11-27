
# mtDNA Heteroplasmy Analysis Tool

## Overview
This package provides tools for analyzing mitochondrial DNA heteroplasmy from FASTQ files. 
Installation time: < 5minutes. Run time < 1minute
## System Requirements
- **Operating System**: Linux, macOS, or Windows
- **Python Version**: Python 3.12.4
- **Dependencies**:
  - BioPython
  - pandas
  - numpy
  - matplotlib


## Installation Guide
1. Clone the repository:
   ```bash
   git clone https://github.com/GreletLab/mtDNA-heteroplasmy.git
   cd mtDNA-heteroplasmy
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Verify the installation by running the test script:
   ```bash
   python test_script.py
   ```

## Demo
A sample FASTQ file (`sample.fastq`) is provided to test the software. To run the analysis:
```bash
python mtDNA-heteroplasmy.py --input sample.fastq --output results.txt
```
This will process the sample data and generate an output file containing the heteroplasmy analysis results.

## Instructions for Use
1. Prepare your input FASTQ file and place it in the working directory.
2. Run the script with the following command:
   ```bash
   python mtDNA-heteroplasmy.py --input <path_to_your_fastq_file> --output <output_file_name>
   ```
3. Options:
   - `--input`: Path to the folder containing the FASTQ files.
   - `--output`: Name of the file where results will be saved.

