from os.path import join
import numpy as np
from dipy.io.image import load_nifti, save_nifti
from dipy.segment.mask import median_otsu
from dipy.io.image import load_nifti
import matplotlib.pyplot as plt
from dipy.core.histeq import histeq
from src import settings

s1 = 'Series 15-ep2d_DTI_Tra_Shim_noPAT_AP_TRACEW/7_ep2d_dti_tra_shim_nopat_ap_tracew.nii.gz'
s2 = 'Series 13-t1_mprage_tra_p2_iso_1.0/2_t1_mprage_tra_p2_iso_10.nii.gz'
s3 = 'Series 11-t2_space_dark-fluid_sag_p2_iso/4_t2_space_dark-fluid_sag_p2_iso.nii.gz'

d = s3
fdwi = join(settings.Resources_nifti, d)
data, affine, img = load_nifti(fdwi, return_img=True)

data = np.squeeze(data)
a = 10
b = 6

b0_mask, mask = median_otsu(data, median_radius=a, numpass=b)

sli = data.shape[2] // 2
plt.figure('Brain segmentation')
plt.subplot(1, 2, 1).set_axis_off()
plt.imshow(histeq(data[:, :, sli].astype('float')).T,
           cmap='gray', origin='lower')

plt.subplot(1, 2, 2).set_axis_off()
plt.imshow(histeq(b0_mask[:, :, sli].astype('float')).T,
           cmap='gray', origin='lower')

plt.savefig(d[:11] + str(a) + str(b) + '.png')

