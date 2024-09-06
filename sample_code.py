import os
import nibabel

def downsample_by_slicing(input_file="", output_file="", slice_interval=1):
    # Load the high-resolution NIfTI image
    img = nibabel.load(input_file)
    data = img.get_fdata()
    affine = img.affine
    header = img.header

    # Select every nth slice in the z-dimension
    downsampled_data = data[::slice_interval, :, :]

    # Adjust the affine transformation matrix to reflect the new slice spacing
    new_affine = affine.copy()
    new_affine[0, 0] *= slice_interval  # update the z-spacing

    # Create a new NIfTI image
    new_header = header.copy()
    new_zooms = list(header.get_zooms())
    new_zooms[0] *= slice_interval  # update the z-spacing
    new_header.set_zooms(new_zooms)

    downsampled_img = nibabel.Nifti1Image(downsampled_data, affine=new_affine, header=new_header)

    # Save the downsampled image
    nibabel.save(downsampled_img, output_file)

# base_path = "C:/Users/mnwoki/Downloads/Convert nii Zip/Convert nii"
# abs_mri_high_res_img_path = os.path.join(base_path, "updated-sub-HC001_ses-01_acq-inv1_T1map.nii.gz")
# abs_mri_low_res_img_path = os.path.join(base_path, "low-updated-res-sub-HC001_ses-01_acq-inv1_T1map.nii.gz")

# downsample_by_slicing(input_file=abs_mri_high_res_img_path, output_file=abs_mri_low_res_img_path, slice_interval=5)

downsample_by_slicing(input_file='sub-HC001_ses-01_acq-mp2rage_T1map_updated2.nii.gz', output_file='sub-HC001_ses-01_acq-mp2rage_T1map_updated2_sampled_manually.nii.gz', slice_interval=5)
