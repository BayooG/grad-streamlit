import os
import numpy as np
import streamlit as st

import matplotlib.pyplot as plt

from functions import load_scan,get_pixels_hu, resample, apply_mask
from plotly_3d import make_mesh, plotly_3d


data_path = "/Users/obaydaba/Desktop/NBIA/CPTAC-LSCC/C3L-01000/06-09-2011-MSKT organov grudnoy k-18628/4.000000-STD 1.25mm-95297"
output_path = working_path = "/Users/obaydaba/Downloads/lung001/"


# ==================load the data==================

# if new_slides :
    # slides = load_scan(data_path) #transverse plane
    # ndarray = get_pixels_hu(slides)
    # imgs_after_resamp, spacing = resample(ndarray, slides, [1,1,1])
#else:
transverse_plane_imgs =np.load(output_path+'fullimages_{}.npy'.format(0))
lungs = np.load(output_path+'lungs_0.npy')
data = {
    'transverse' : transverse_plane_imgs, #transverse_plane_imgs
    'coronal' : transverse_plane_imgs.swapaxes(0,1), #coronal_plane_imgs
    'sagittal' : transverse_plane_imgs.swapaxes(0,2).swapaxes(1,2), #sagittal_plane_imgs
    'lungs': lungs,    
}



# ==================streamlit==================

#sidebar
selected_plane = st.sidebar.selectbox('Select plane', list(data.keys()))
slider = st.sidebar.slider('Select a value', min_value=0, max_value= len(data[selected_plane])-1)
slides_plane = st.sidebar.checkbox("Would you like to see slides?")
histogram_checkbox = st.sidebar.checkbox("Would you like to see histogram?")

#main window
st.title("anotomy project")
st.write('Selected plane: ', selected_plane)

# masked = apply_mask(data[selected_plane],'lungmask')
if slides_plane:
    st.write('image index', slider)
    plot = plt.imshow(data[selected_plane][slider], cmap='gray')
    the_plot = st.pyplot(plt)

# st.bar_chart()

#3d lungs 
verts, faces  = make_mesh(data['lungs'])

st.plotly_chart(plotly_3d(verts, faces))

# ==================histogram==================
if histogram_checkbox:
    st.write('image histogram')
    plt.hist(data['lungs'].flatten(), bins=50, color='c')
    plt.xlabel("Hounsfield Units (HU)")
    plt.ylabel("Frequency")
    histo_plot = st.pyplot(plt)

#============== select files ===============#



# def file_selector(folder_path='.'):
#     filenames = os.listdir(folder_path)
#     selected_filename = st.selectbox('Select a file', filenames)
#     return os.path.join(folder_path, selected_filename)

# filename = file_selector()
# st.write('You selected `%s`' % filename)

# st.file_uploader('upload dicom series',type='dcm')