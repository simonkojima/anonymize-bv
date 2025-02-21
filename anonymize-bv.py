import os
import argparse
import datetime

import mne
import mne_bids

def mkdir(dir):
    isExist = os.path.exists(dir)
    if not isExist:
        os.makedirs(dir)
        
def get_daysback(vhdr, date):
    raw = mne.io.read_raw_brainvision(vhdr)
    meas_date = raw.info['meas_date'].replace(tzinfo=None)
    delta = meas_date - date
    
    return delta.days

def anonymize_bv(dir, date, original_fnames = None, new_fnames = None):

    if original_fnames is None:
        files = os.listdir(dir)
    else:
        files = original_fnames

    mkdir(os.path.join(dir, "anonymized"))
    
    for idx, file in enumerate(files):
        if ".vhdr" not in file:
            continue
    
        if new_fnames is not None:
            new_fname = new_fnames[idx]
        else:
            new_fname = file

        daysback = get_daysback(vhdr = os.path.join(dir, file), date = date)
        mne_bids.copyfiles.copyfile_brainvision(os.path.join(dir, file),
                                                os.path.join(dir, "anonymized", new_fname),
                                                anonymize = {"daysback":daysback, "keephis":False})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type = str)
    parser.add_argument("--date", type = int, nargs=3, default = [1920,1,1])
    
    args = parser.parse_args()
    
    date = datetime.datetime(args.date[0], args.date[1], args.date[2])
    print(date)

    anonymize_bv(dir = args.dir, date = date)
    
    
    
    
    