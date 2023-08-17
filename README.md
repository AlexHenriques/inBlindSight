# Blinding Tool for Experimental Research

![GitHub](https://img.shields.io/github/license/alexhenriques/IDBlindingTool)
![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)

### Blinding refers to concealing group allocation from the experimenter to reduce biases arising from participants' expectations, ensuring the reproducibility of your research findings.

This tool provides a user-friendly solution to assist researchers in conducting blinded experiments by randomly assigning unique IDs to labels.

To get started, follow the installation and usage instructions below.

## Features

- Randomly assign unique IDs to labels for blinded experiments.
- Rename files using randomly generated ID-label pairs.
- Ublind file names using previously generated ID-label pairs.
- Export ID-label pairs to a CSV file for record-keeping.

## Getting Started

### Prerequisites

- Install Python 3.6 or higher.
- Install Git

### Installation

In a terminal:
1. Clone this repository to your local machine `git clone https://github.com/AlexHenriques/IDBlindingTool.git`
3. Open a terminal and navigate to the repository's directory `cd IDBlindingTool`.
5. Run the script using the command `python blinding_tool.py`.

## Usage

1. Choose the mode:
   - (1) Assign IDs to labels at random and optionally rename corresponding files.
   - (2) Rename files using existing ID-label pairs.
   - (3) Unblind the files using the ID-label pairs.

2. Follow the prompts to input labels, IDs, and paths as needed.
3. ID-label pairs can be displayed or exported to a CSV file.

## Important Notes!

- List must have the following format: **item1,item2,...itemn**
- Ensure that your file names **precisely match** the IDs or labels (including case and spaces).
- If creating a file, ensure the name doesn't conflict with an ID.
- The tool supports both Windows and macOS operating systems.
- At no point are the ID-label pairs revealed to the user **without** their consent.

## Suggestions

- Every experimental unit/observation should be blinded, not the groups.
- Ideally, repeat blinding for each analysis to avoid associations between variables based on prior knowledge.
- Technically, you can assign any term to a label. You may rename groups names for a triple-blind approach.

## Credits

- The idea of using Pokémon names for labeling was inspired by Nuno Henrique Franco, who suggested this creative approach

## Author

- Alexandre Henriques
- Contact: alexandresshenriques@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

