import os
import sys
import glob
import pyperclip as pc

from typing import Optional
from dataclasses import dataclass, field
from transformers import HfArgumentParser


@dataclass
class Args:
    input_dir: str = field(
        metadata={"help": "The path to the image files."}
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={"help": "The suffix of the files which we are acquiring paths. "
                          "If not specified, all files in input folder will be visited."},
    )

def ref_images(args: Args):
    path_list = list()
    for f in glob.glob(os.path.join(args.input_dir, f"*.{args.suffix}" if args.suffix else "*")):
        path_list.append(os.path.normpath(os.path.abspath(f)))
    path_list.sort()
    temp_path = path_list[0]
    img_folder_idx = temp_path.split(os.sep).index("images")

    path_str_list = list()
    for path in path_list:
        path_str = "/".join(["{{base_path}}"] + path.split(os.sep)[img_folder_idx:])
        path_str_list.append(path_str)

    path_ref_list = list()
    for path_str in path_str_list:
        path_ref_list.append(f"![]({path_str})")
    path_ref_str = '\n\n'.join(path_ref_list)
    pc.copy(path_ref_str)

    return path_ref_str


if __name__ == "__main__":
    parser = HfArgumentParser(Args)
    if len(sys.argv) == 2 and sys.argv[1].endswith(".json"):
        # If we pass only one argument to the script and it's the path to a json file,
        # let's parse it to get our arguments.
        args, = parser.parse_json_file(
            json_file=os.path.abspath(sys.argv[1])
        )
    else:
        args, = parser.parse_args_into_dataclasses()

    ref_images(args)
