import glob
import dicom2nifti
from os.path import expanduser, join
import settings
import os


def dcm_to_nii_converter(dicom_directory):
    directory = dicom_directory.split("\\")
    parent_dir = settings.Resources_nifti
    path = os.path.join(parent_dir, directory[-1])

    os.mkdir(path)

    output_folder = path
    print(path)
    dicom2nifti.convert_directory(dicom_directory, output_folder, compression=True, reorient=True)


if __name__ == '__main__':
    for d in glob.glob('C:\\Users\\S\\Downloads\\Compressed\\2\\*'):
        print(d)
        try:
            dcm_to_nii_converter(d)
        except:
            print('err')

# from nipype.interfaces.dcm2nii import Dcm2niix
# converter = Dcm2niix()
# converter.inputs.source_dir = dicom_directory
# converter.inputs.compression = 5
# converter.inputs.output_dir = 'ds005'
# converter.cmdline
#
# converter.run()
