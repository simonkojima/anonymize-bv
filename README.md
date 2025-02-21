# anonymize-bv
A script for anonymizing vhdr EEG files.

# Requirements
- python 3.x
- mne
- mne-bids

# Usage
```shell
# recording date will be 1920.1.1
# The anonymized files will be saved in "specified_path/anonymized"
python anonymize-bv.py PATH_TO_DIRECTORY_CONTAINS_VHDR_FILES

# you can specify recording date with --date option
python anonymize-bv.py PATH_TO_DIRECTORY_CONTAINS_VHDR_FILES --date 2000 1 1
```