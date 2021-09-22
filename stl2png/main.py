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
parser.add_argument("--stl", dest="stl", help="the stl file to convert", required=True)
parser.add_argument("--png", dest="png", help="the png file to create", required=True)

if __name__ == "__main__":
    args = parser.parse_args()

    mesh = Mesh.from_file(args.stl)
    # plot the image
    vtkplotlib.mesh_plot(mesh, opacity=0.5)

    # adjust the position
    # this is hard. so I commented it out because lazy
    # vtkplotlib.view(camera_position=[args.x, args.y, args.z])

    # write the image out
    vtkplotlib.save_fig(args.png)

    # pad ego
    print(f"Saved {args.stl} as {args.png} successfully!")
