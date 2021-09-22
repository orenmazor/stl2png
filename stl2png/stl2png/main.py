"""stl2png.

    a simple tool to convert stl files to png.

    input:
        --stl
            the stl file that you want screen captured
        --orientation
            the coordinates from which to take a picture
        --png
            the path of the png file that you'd like written
            """
import argparse

from stl.mesh import Mesh
import vtkplotlib

import argparse

parser = argparse.ArgumentParser(description="Convert an stl to a png.")
parser.add_argument("--stl", dest="stl", help="the stl file to convert")
parser.add_argument("--png", dest="png", help="the png file to create")
parser.add_argument(
    "--orientation",
    dest="orientation",
    help="the angle to orient before taking a photo",
)

if __name__ == "__main__":
    args = parser.parse_args()
    if not args.stl or not args.png:
        parser.print_help()

    mesh = Mesh.from_file(args.stl)
    vtkplotlib.mesh_plot(mesh)
    vtkplotlib.save_fig(args.png)
    print(f"Saved {args.stl} as {args.png}")
