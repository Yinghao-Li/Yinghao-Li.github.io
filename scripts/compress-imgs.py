import os
import sys

from PIL import Image
from tqdm.auto import tqdm
from typing import Optional
from dataclasses import dataclass, field
from transformers import HfArgumentParser


@dataclass
class Args:
    input_dir: str = field(
        metadata={"help": "The path to the image files."}
    )
    output_dir: Optional[str] = field(
        default=None,
        metadata={"help": "The output folder where the compressed images are saved. "
                          "If not specified, the input folder is used."},
    )
    quality: Optional[int] = field(
        default=50,
        metadata={"help": "The quality of the compressed images."}
    )
    prefix: Optional[str] = field(
        default=None,
        metadata={"help": "The prefix of the compressed images. "
                          "If neither this nor `output_dir` is specified, the original images will be overritten."}
    )


def compress_images(args: Args):
    if not args.output_dir:
        output_dir = args.input_dir
    else:
        output_dir = args.output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    if not args.prefix:
        args.prefix = ""

    for f in tqdm(os.listdir(args.input_dir)):
        file_suffix = f.split(".")[-1].lower()
        if file_suffix in ["jpg", "jpeg"]:
            img = Image.open(os.path.join(args.input_dir, f))
            img.save(os.path.join(output_dir, args.prefix + f), quality=args.quality)


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

    compress_images(args)
