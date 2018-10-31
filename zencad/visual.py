import zencad
import zencad.shower
import numpy as np
from pyservoce import Scene, Viewer

from PIL import Image

from evalcache.lazyfile import LazyFile

lazyfile = LazyFile()

@lazyfile("path")
def screen(model, path, size=(800,600)):
	scn = Scene()
	scn.add(model)
	viewer = Viewer(scn)
	view = viewer.create_view()
	view.set_virtual_window(size[0], size[1])
	view.fit_all()

	raw = view.rawarray()
	npixels = np.reshape(np.asarray(raw), (size[1],size[0],3))
	nnnpixels = np.flip(npixels, 0).reshape((size[0] * size[1] * 3))

	rawiter = iter(nnnpixels)
	pixels = list(zip(rawiter, rawiter, rawiter))
		
	image = Image.new("RGB", (size[0], size[1]))
	image.putdata(pixels)

	image.save(path)