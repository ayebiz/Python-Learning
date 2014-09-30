import os
import tempfile
import shutil

name = raw_input("What would you like to name it? \n")
nameSav = name + ".png"
tmpdir = tempfile.mkdtemp()                   # create a temporary directory
tmpfile = os.path.join(tempdir, 'tmp.svg')    # name of file to save SVG to
ts = turtle.getscreen().getcanvas()
canvasvg.saveall(tmpfile, ts)
with open(tmpfile) as svg_input, open(nameSav, 'wb') as png_output:
    cairosvg.svg2png(bytestring=svg_input.read(), write_to=png_output)
shutil.rmtree(tmpdir)     # clean up temp file(s)