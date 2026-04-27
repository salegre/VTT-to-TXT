from os import listdir, remove
from os.path import isfile, join
from re import sub, search
from time import sleep

def write_txt(fname, data):
    out_folder = "output/"
    fname = fname.replace(".vtt", ".txt").replace(".srt", ".txt")
    with open(out_folder + fname, "w", encoding="utf-8") as f:
        f.write(data)

def get_files(dir):
    return [f for f in listdir(dir) if isfile(join(dir, f)) and (f.endswith(".vtt") or f.endswith(".srt"))]

def reset_output():
    out_folder = "output/"
    for f in listdir(out_folder):
        remove(out_folder+f)

def main(in_folder):
    in_files = get_files(in_folder)
    for fname in in_files:
        with open(in_folder + fname, "r", encoding="utf-8-sig") as f:
            output = ""
            current_speaker = None
            next = False
            for line in f:
                if next:
                    if line == "\n":
                        next = False
                        continue
                    
                    # Extract speaker from <v Speaker Name> tag
                    speaker_match = search(r"<v ([^>]*)>", line)
                    if speaker_match:
                        new_speaker = speaker_match.group(1)
                        if new_speaker != current_speaker:
                            if output:
                                # Ensure we start a new paragraph for a new speaker
                                output = output.rstrip() + "\n\n"
                            output += new_speaker + ": "
                            current_speaker = new_speaker
                        # Remove the speaker opening tag specifically
                        line = sub(r"<v [^>]*>", "", line)
                    
                    # Remove all other tags (like </v>, <i>, etc.)
                    line = sub(r"<[^>]*>", "", line)
                    output += line
                    continue
                
                if "-->" in line:
                    next = True
            
            output = output.strip()
            words = output.split()
            write_txt("[{} words] {}".format(len(words), fname), output)
            print("Successfully converted file: {}".format(fname))

        
reset_output()
in_folder = "input/"
main(in_folder)

secs = 3
print("Fininshed.\nClosing program in {} seconds.".format(secs))
sleep(secs)
