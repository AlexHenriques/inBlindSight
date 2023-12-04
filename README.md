# ID Blinding Tool

![GitHub](https://img.shields.io/github/license/alexhenriques/IDBlindingTool)

The ID Blinding Tool is a citable and user-friendly sofware designed to support blinded data analysis. 
Its primary function involves the random assignment of unique identifiers (IDs) to corresponding labels and renames files accordingly. 
This process is crucial to prevent bias, ensure anonymity, and maintain data integrity in various experimental settings.

## Features

- **Random ID-Label Assignment**: Assigns unique IDs to labels and exports the ID-label pairs to an Excel file.
- **Data Blinding and Unblinding**: Facilitates blinding and unblinding of data by renaming cells in Excel files or 
renaming files in folders using the generated ID-label pairs.

## How to Install and Run the Program

To begin using the ID Blinding Tool, follow these steps:

**Windows**

1. **Download**: Get the latest .exe file [here](https://github.com/AlexHenriques/IDBlindingTool/releases).
2. **Installation**: Simply, run the downloaded file (ID_Blinding_Tool.exe) and follow the installation steps.
3. **Function Selection**: Select the desired function, such as Randomly Assign IDs to Labels or Rename Files.
4. **Guidance**: Find help within the tool if needed~.

**macOS**

1. **Download**: Click on the green "Code" button and download the ZIP file.
2. **Installation**: 
   1. Install [Python](https://www.python.org/downloads/macos/) 3.6 or higher.
   2. In a terminal, go to the extracted directory using `cd "/path/to/the/directory"`
   3. Then, execute `pip install -r requirements.txt`
3. **Run**: Execute `python ID_Blinding_Tool.py`
4. **Function Selection**: Select the desired function, such as Randomly Assign IDs to Labels or Rename Files.
5. **Guidance**: Find help within the tool if needed.


### How does it randomly assign IDs to Labels?

The ID Blinding Tool pairs identifiers with labels through the following steps:

1. **Eliminating Duplicates**: Ensures that the lists of IDs and labels do not contain duplicates.
2. **Random Label Selection**: Randomly selects the required number of labels from a list of available labels.
3. **Pairing IDs and Labels**: Establishes random connections between IDs and labels, creating a key for subsequent use.

```python
random_label_selection = random.sample(labels_list, len(ids_list))
id_label_pairs = dict(zip(ids_list, random_label_selection))
```

## Contributions and Troubleshooting

If you have ideas to enhance the tool's functionality or encounter any issues, please report it via the Issues section.

## Author and Contact

- Author: Alexandre Henriques
- Contact: alexandresshenriques@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
