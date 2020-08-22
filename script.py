import numpy as np
from functions import  apply_mask
from masks import make_lungmask
from tqdm import tqdm

from plotly_3d import make_mesh, plotly_3d

output_path  = "/Users/obaydaba/Downloads/lung001/"

# transverse_plane_imgs =np.load(output_path+'fullimages_{}.npy'.format(0))

# lungs = []
# for img in tqdm(transverse_plane_imgs):
#     lungs.append(make_lungmask(img))
    

# np.save(output_path + "lungs_%d.npy" % 0, lungs)



################
lungs =np.load(output_path+'lungs_0.npy')
verts, faces  = make_mesh(lungs)

plotly_3d(verts, faces)