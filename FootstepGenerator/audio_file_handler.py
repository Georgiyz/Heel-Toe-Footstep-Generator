import os
import pydub
import random


def generate_heel_toe_file():
    heel_toe_segment = _stitch_heel_toe()
    heel_toe_segment.export("media/stitched_pairs/stitched_pair.wav",
                            format="wav")


def _stitch_heel_toe():
    '''Returns a wav file of a stitched heel and toe file pair'''
    pair_paths = _random_select_file_pair()
    heel_segment = pydub.AudioSegment.from_file(pair_paths[0])
    toe_segment = pydub.AudioSegment.from_file(pair_paths[1])

    stitched_heel_toe = heel_segment + toe_segment

    return stitched_heel_toe
    
    
def _random_select_file_pair():
    '''
    Returns two strings, one containing the file paths for heel and the other for toe.
    File paths will come in heel-toe order.
    '''
    heel_directory_path = "media/heel"
    heel_files_in_directory = [f for f in os.listdir(heel_directory_path)
                               if os.path.isfile(os.path.join(heel_directory_path, f))]
    
    toe_directory_path = "media/toe"
    toe_files_in_directory = [f for f in os.listdir(toe_directory_path)
                              if os.path.isfile(os.path.join(toe_directory_path, f))]

    if not heel_files_in_directory:
        print("No files found in the specified directory.")
        return None
    
    if not toe_files_in_directory:
        print("No files found in the specified directory.")
        return None

    heel_file = random.choice(heel_files_in_directory)
    toe_file = random.choice(toe_files_in_directory)

    print(heel_file + " " + toe_file)

    return os.path.join(heel_directory_path, heel_file), os.path.join(toe_directory_path, toe_file)
